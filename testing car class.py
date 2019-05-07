# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 19:58:11 2019

@author: arman
"""
import Car
import Dashboard

def main():
    print('Testing car class ...')
    make = 'Chevy'
    model = 'Malibu'
    year = '2005'
    port_number = 283944390
    
    my_car = Car.Car(make, model, port_number, year)
    my_car.getSpeed()
    
    board = Dashboard.Dashboard()
    #board
    
if __name__ == ('__main__'):
    main()