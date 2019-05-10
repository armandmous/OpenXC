# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 09:38:15 2019

@author: arman
"""
from tkinter import ttk
import tkinter as tk
from tkinter import scrolledtext
#import wx               # Import wxPython GUI toolkit 
import Car

# TODO: Assign global variables


class Dashboard():
    print('Opening Dashboard...')
    def __init__(self):
        self.win = tk.Tk()                  # create a window object
        self.window_title = 'Dashboard'     # create window's title
        self.chevy = Car.Car()              # create a car object
        
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
        self.field1 = ttk.Entry(self.lFrame, width = 20, textvariable = self.field1_variable).grid(column = 0, row = 1)
        self.field2 = ttk.Entry(self.lFrame, width = 20, textvariable = self.field2_variable).grid(column = 1, row = 1)
        self.field3 = ttk.Entry(self.lFrame, width = 20, textvariable = self.field3_variable).grid(column = 2, row = 1)
        self.field4 = ttk.Entry(self.lFrame, width = 20, textvariable = self.field4_variable).grid(column = 3, row = 1)
        # apply button
        self.action = ttk.Button(self.lFrame, text="Apply", command = self.apply).grid(column = 4, row = 1) 
        
        
        #----------------------------------------------------------------------
        # Create and initialize variables holding vehicle information
        # Create container (frame) that holds labels displaying vehicle information
        #----------------------------------------------------------------------
        # TODO: Create and add Labels
        self.make = self.chevy.getMake()
        self.mode = self.chevy.getModel()
        self.year = self.chevy.getYear()
        self.port = self.chevy.getPortNumber()
        
        self.speed = self.chevy.getSpeed()
        
        # Create a container to hold labels
        self.l1Frame = ttk.LabelFrame(self.win, text='Vehicle')
        self.l1Frame.grid(column = 0, row = 1, padx = 15, pady = 15)
        self.label1 = ttk.Label(self.l1Frame, text="Make :  " + self.make).grid(column = 0, row = 0)
        self.label2 = ttk.Label(self.l1Frame, text="Model:  " + self.mode).grid(column = 0, row = 1)
        self.label3 = ttk.Label(self.l1Frame, text="Year :  " + str(self.year)).grid(column = 0, row = 2)
        self.label4 = ttk.Label(self.l1Frame, text="PORT :  " + str(self.port)).grid(column = 0, row = 3)
        
        self.label5 = ttk.Label(self.l1Frame, text="Speed :  " ).grid(column = 1, row = 0)
        self.label6 = ttk.Label(self.l1Frame, text="Feat1 :  " ).grid(column = 1, row = 1)
        self.label7 = ttk.Label(self.l1Frame, text="Feat2 :  " ).grid(column = 1, row = 2)
        self.label8 = ttk.Label(self.l1Frame, text="Feat3 :  " ).grid(column = 1, row = 3)
        
        self.label9 = ttk.Label(self.l1Frame, text="Feat4 :  " ).grid(column = 2, row = 0)
        self.label10 = ttk.Label(self.l1Frame, text="Feat5 :  ").grid(column = 2, row = 1)
        self.label11 = ttk.Label(self.l1Frame, text="Feat6 :  ").grid(column = 2, row = 2)
        self.label12 = ttk.Label(self.l1Frame, text="Feat7 :  ").grid(column = 2, row = 3)
        
        #----------------------------------------------------------------------
        # Create a text area with specific size
        #----------------------------------------------------------------------
        # TODO: implement live trace screen
        self.l2Frame = ttk.LabelFrame(self.win, text='Feed Live Trace...')
        self.l2Frame.grid(column = 0, row = 2, padx = 15, pady = 15)
        self.scrolW  = 70                          
        self.scrolH  = 25
        self.scr = scrolledtext.ScrolledText(self.l2Frame, width = self.scrolW, height = self.scrolH, wrap = tk.WORD)
        self.scr.grid(column = 0, columnspan = 3)
        
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
        print('button pressed!!')
        print('Make entered : ' + self.field1_variable.get())
        print('model entered: ' + self.field2_variable.get())
        print('Year entered : ' + self.field3_variable.get())
        print('Port entered : ' + self.field4_variable.get())
        self.scr(text = self.chevy.read_trace())
