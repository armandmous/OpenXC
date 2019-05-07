# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 09:38:15 2019

@author: arman
"""
from tkinter import ttk
import tkinter as tk
#import wx               # Import wxPython GUI toolkit 
import Car

# TODO: Assign global variables
win = tk.Tk()

class Dashboard():
    print('Opening Dashboard...')
    def __init__(self):
        # setting up our gui title
        window_title = 'Dashboard'
        chevy = Car.Car()
        window_title = chevy.getMake() + ' ' + chevy.getModel() + ' ' + window_title
        
        # TODO: Create window
        #win = tk.Tk()
        
        
        self.field1_variable = ''
        self.field2_variable = ''
        self.field3_variable = ''
        self.field4_variable = ''
        
        self.field1Label = ttk.Label(win, text="Enter make:").grid(column = 0, row = 0)
        self.field2Label = ttk.Label(win, text="Enter model:").grid(column = 1, row = 0)
        self.field1Label = ttk.Label(win, text="Enter Year:").grid(column = 2, row = 0)
        self.field2Label = ttk.Label(win, text="Enter Port Number:").grid(column = 3, row = 0)
        
        # TODO: text fields
        self.field1 = ttk.Entry(win, width = 20, textvariable = self.field1_variable).grid(column = 0, row = 1)
        self.field2 = ttk.Entry(win, width = 20, textvariable = self.field2_variable).grid(column = 1, row = 1)
        self.field3 = ttk.Entry(win, width = 20, textvariable = self.field3_variable).grid(column = 2, row = 1)
        self.field4 = ttk.Entry(win, width = 20, textvariable = self.field4_variable).grid(column = 3, row = 1)
        
        # apply button
        self.action = ttk.Button(win, text="Apply", command = self.apply).grid(column = 5  , row = 1) 
        
        # TODO: Create and add Labels
        self.label1 = ttk.Label(win, text="Make:  " + chevy.getMake() + '\t'  ).grid(column = 0, row = 2)
        self.label2 = ttk.Label(win, text="Model:  " + chevy.getModel() + '\t' ).grid(column = 1, row = 2)
        self.label3 = ttk.Label(win, text="Year:  " + str(chevy.getYear()) + '\t' ).grid(column = 2, row = 2)
        self.label4 = ttk.Label(win, text="PORT:  " + str(chevy.getPortNumber()) + '\t' ).grid(column = 3, row = 2)
        
        
        # TODO:  Run our gui until the program is interrupted by closing the window
        win.title(window_title)
        win.mainloop()
        
    # Button Click Event Callback Function     
    def apply(self):
        print('button pressed!!')
   
