# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 09:38:15 2019

@author: arman
"""
from tkinter import ttk
import tkinter as tk
import Car

# TODO: Assign global variables
win = tk.Tk()
aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0) 

def main():
    print('Running OpenXC Dashboard...')
    
    # setting up our gui title
    window_title = 'Dashboard'
    chevy = Car.Car('Chevy', 'Malibu', 283944390, 2005)
    window_title = chevy.getMake() + ' ' + chevy.getModel() + ' ' + window_title
    

    # TODO: Create window
    #win = tk.Tk()
    
    # TODO: Create and add Labels
    label1 = ttk.Label(win, text="Make:  " + chevy.getMake() + '\t'  ).grid(column=0, row=0)
    label2 = ttk.Label(win, text="Model:  " + chevy.getModel() + '\t' ).grid(column=1, row=0)
    label3 = ttk.Label(win, text="Year:  " + str(chevy.getYear()) + '\t' ).grid(column=2, row=0)
    label4 = ttk.Label(win, text="PORT:  " + str(chevy.getPortNumber()) + '\t' ).grid(column=3, row=0)
    
    # TODO: Add buttons
    action = ttk.Button(win, text="Click Me!", command=clickMe)  
    action.grid(column=1, row=1)
    
    # TODO:  Run our gui until the program is interrupted by closing the window
    win.title(window_title)
    win.mainloop()
    
# Button Click Event Callback Function     
def clickMe():
    action.configure(text="** I have been Clicked! **")
    alabel.configure(foreground='red')
   
 
if __name__ == '__main__':
    main()