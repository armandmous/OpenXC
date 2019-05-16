# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 09:38:15 2019

@author: arman
"""
from tkinter import ttk
import tkinter as tk
from tkinter import scrolledtext
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#import wx               # Import wxPython GUI toolkit 
import Car

# TODO: Assign global variables


class Dashboard():
    print('Opening Dashboard...')
    def __init__(self):
        self.win = tk.Tk()                  # create a window object
        self.window_title = 'Dashboard'     # create window's title
        
        #----------------------------------------------------------------------
        # Create and initialize variable for each text field
        # data from each text field is stored in these variables
        #----------------------------------------------------------------------
        self.field1_variable = tk.StringVar()
        self.field2_variable = tk.StringVar()
        self.field3_variable = tk.StringVar()
        self.field4_variable = tk.StringVar()
        
        #----------------------------------------------------------------------
        # Create labels and the text fields and a container (frame) to hold
        #    these components
        #----------------------------------------------------------------------
        self.lFrame = ttk.LabelFrame(self.win, text='Enter Vehicle Info')
        self.lFrame.grid(column = 0, row = 0, padx = 15, pady = 15)
        self.field1Label = ttk.Label(self.lFrame, text="Enter make: ").grid(column = 0, row = 0)
        self.field2Label = ttk.Label(self.lFrame, text="Enter model:").grid(column = 1, row = 0)
        self.field1Label = ttk.Label(self.lFrame, text="Enter Year: ").grid(column = 2, row = 0)
        self.field2Label = ttk.Label(self.lFrame, text="Enter Port Number:").grid(column = 3, row = 0)
        
        # TODO: text fields
        self.field1 = ttk.Entry(self.lFrame, width = 26, textvariable = self.field1_variable).grid(column = 0, row = 1)
        self.field2 = ttk.Entry(self.lFrame, width = 26, textvariable = self.field2_variable).grid(column = 1, row = 1)
        self.field3 = ttk.Entry(self.lFrame, width = 26, textvariable = self.field3_variable).grid(column = 2, row = 1)
        self.field4 = ttk.Entry(self.lFrame, width = 26, textvariable = self.field4_variable).grid(column = 3, row = 1)
        # apply button
        self.action = ttk.Button(self.lFrame, text="Apply", command = self.apply).grid(column = 4, row = 1) 
        
        
        #----------------------------------------------------------------------
        # Create and initialize variables holding vehicle information
        # Create container (frame) that holds labels displaying vehicle information
        #----------------------------------------------------------------------
        # TODO: Create and add Labels
        self.make = ''
        self.mode = ''
        self.year = ''
        self.port = ''
        self.speed = ''
        
        # Create a container to hold labels
        self.main_frame = ttk.LabelFrame(self.win, text='Vehicle data trace...')
        self.main_frame.grid(column = 0, row = 1, padx = 15, pady = 15)
        
        
        self.l1Frame = ttk.LabelFrame(self.main_frame, text='Vehicle')
        self.l1Frame.grid(column = 0, row = 1, padx = 15, pady = 15)
        self.label1 = ttk.Label(self.l1Frame, text="Make :  ").grid(column = 0, row = 0)
        self.label2 = ttk.Label(self.l1Frame, text="Model:  ").grid(column = 0, row = 1)
        self.label3 = ttk.Label(self.l1Frame, text="Year :  ").grid(column = 0, row = 2)
        self.label4 = ttk.Label(self.l1Frame, text="PORT :  ").grid(column = 0, row = 3)
        self.l1Frame = ttk.LabelFrame(self.win, text='Vehicle')
        
        self.stat_frame = ttk.LabelFrame(self.main_frame, text='stat (x1000)')
        self.stat_frame.grid(column = 1, row = 1, padx = 15, pady = 15)
        self.label5 = ttk.Label(self.stat_frame, text="Vehicle speed :  ").grid(column = 0, row = 0)
        self.label6 = ttk.Label(self.stat_frame, text="Engine speed  :  ").grid(column = 0, row = 1)
        self.label7 = ttk.Label(self.stat_frame, text="Voltage level :  ").grid(column = 0, row = 2)
        self.label8 = ttk.Label(self.stat_frame, text="Pressure level:  ").grid(column = 0, row = 3)
        self.label8 = ttk.Label(self.stat_frame, text="Current level :  ").grid(column = 0, row = 4)
        
        self.chart_frame = ttk.LabelFrame(self.stat_frame, text='Stat')
        self.chart_frame.grid(column = 3, row = 0, padx = 15, pady = 15)
        
        #----------------------------------------------------------------------
        # Create a text area with specific size
        #----------------------------------------------------------------------
        # TODO: implement live trace screen
        self.l2Frame = ttk.LabelFrame(self.win, text='Feed Live Trace...')
        self.l2Frame.grid(column = 0, row = 2, padx = 15, pady = 15)
        self.scrolW  = 90                          
        self.scrolH  = 20
        self.scr = scrolledtext.ScrolledText(self.l2Frame, width = self.scrolW, height = self.scrolH, wrap = tk.WORD)
        self.scr.grid(column = 0, columnspan = 3)
        # clear button
        self.clear = ttk.Button(self.l2Frame, text="Clear Trace Feed", command = self.clear_trace).grid(column = 0, row = 1)
        
        #self.l3Frame = ttk.LabelFrame(self.win, text='Status')
        #self.l2Frame.grid(column = 1, row = 0, padx = 15, pady = 15)

        #----------------------------------------------------------------------
        # Display our GUI object
        #----------------------------------------------------------------------
        # TODO:  Run our gui until the program is interrupted by closing the window
        self.win.title(self.window_title)
        self.win.mainloop()
     
    #----------------------------------------------------------------------
    # Button Click Event Callback Function
    # The apply function is called when the action button is called
    #   storing data from each text field into a car object
    #   the car status data will be return from the car class object
    #----------------------------------------------------------------------
    def apply(self):
        self.scr.delete('1.0', tk.END)
        
        car_var1 = self.field1_variable.get()
        car_var2 = self.field2_variable.get()
        car_var3 = self.field3_variable.get()
        car_var4 = self.field4_variable.get()
        
        if len(car_var1) < 3:
            self.scr.insert(tk.INSERT, 'Warning:\tInvalid make / make not found\n')
        if len(car_var2) < 1:
            self.scr.insert(tk.INSERT, 'Warning:\tInvalid model / model not found\n')
        if len(car_var3) < 4:
            self.scr.insert(tk.INSERT, 'Warning:\tInvalid year / year not found\n')
        if len(car_var4) < 9:
            self.scr.insert(tk.INSERT, 'Warning:\tInvalid ip address / ip address not found\n')

        #----------------------------------------------------------------------
        # If valid is entered display the correct data
        #----------------------------------------------------------------------
        if (len(car_var1) > 2) and (len(car_var2) > 0) and (len(car_var3) > 3) and (len(car_var4) > 8):
                # create car object and update labels with car data
                self.chevy = Car.Car(car_var1, car_var2, car_var3, car_var4)   # create a car object
                self.make = self.chevy.getMake()
                self.mode = self.chevy.getModel()
                self.year = self.chevy.getYear()
                self.port = self.chevy.getPortNumber()

                self.scr.insert(tk.INSERT, self.chevy.read_dtc_trace())
                self.scr.insert(tk.INSERT, '\n\nData Trace:\n')
                self.scr.insert(tk.INSERT, '----------------------------------------------------------------------------------------\n')
                self.scr.insert(tk.INSERT, self.chevy.read_uas_trace())

                self.label1 = ttk.Label(self.l1Frame, text='Make : ' + self.make + '\t').grid(column = 0, row = 0)
                self.label2 = ttk.Label(self.l1Frame, text="Model: " + self.mode + '\t').grid(column = 0, row = 1)
                self.label3 = ttk.Label(self.l1Frame, text="Year : " + self.year + '\t').grid(column = 0, row = 2)
                self.label4 = ttk.Label(self.l1Frame, text="PORT : " + self.port + '\t').grid(column = 0, row = 3)
                
                self.label5 = ttk.Label(self.stat_frame, text="Vehicle speed : \t" + str(self.chevy.getSpeed()) + 'KPH').grid(column = 0, row = 0)
                self.label6 = ttk.Label(self.stat_frame, text="Engine speed  : \t" + str(self.chevy.getEngineSpeed()) + 'RPM' ).grid(column = 0, row = 1)
                self.label7 = ttk.Label(self.stat_frame, text="Voltage level : \t" + str(self.chevy.getVoltageLevel()) + 'Volt').grid(column = 0, row = 2)
                self.label8 = ttk.Label(self.stat_frame, text="Pressure level: \t" + str(self.chevy.getPressureLevel()) + 'KPS').grid(column = 0, row = 3)
                self.label8 = ttk.Label(self.stat_frame, text="Current level : \t" + str(self.chevy.getCurrentLevel())  + 'AMP').grid(column = 0, row = 4)
                
                
                self.label4 = ttk.Label(self.l1Frame, text="PORT : " + self.port + '\t').grid(column = 0, row = 3)
                #-------------------------------------------------------------
                fig = Figure(figsize=(12, 8), facecolor='white')
                #-------------------------------------------------------------
                # axis = fig.add_subplot(111)
                # 1 row,  1 column, only graph
                axis = fig.add_subplot(211)     # 2 rows, 1 column, Top graph 
                #-------------------------------------------------------------
                xValues = [1,2,3,4]
                yValues = [5,7,6,8]
                axis.plot(xValues, yValues)
                axis.set_xlabel('Horizontal Label')
                axis.set_ylabel('Vertical Label')
                # axis.grid()                   # default line style 
                axis.grid(linestyle='-')
        
    def clear_trace(self):
        self.scr.delete('1.0', tk.END)
