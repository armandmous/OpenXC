# -*- coding: utf-8 -*-
"""
Date:           Created on Thu Apr 11 08:21:06 2019
Name:           Armand Moussaouyi and Derek Cotton
Description:    OpenXC
"""

class Car:
    '''Basic car class'''
    
    def __init__(self, make = 'Chevrolet', model = 'Malibu Classic', port = '127.0.0.1', year = '2005'):
        '''Constructor'''
        self.make = make
        self.model = model
        self.year = year
        self.XC_port = port
    
    def getMake(self):
        return self.make
    
    def getModel(self):
        return self.model
    
    def getYear(self):
        return self.year
    
    def getPortNumber(self):
        return self.XC_port
    '''
    Processing data
    '''    
    def process_data(self):
        print('Processing data...')    
        
    def readData(self, port_number):
        print('Reading data...')
        self.openXC_port = port_number
        
    '''
    Vehicle speed
    '''
    def getSpeed(self):
        print('Getting speed ...')
    
    '''
    Steering wheel angle
    '''
    def getSteeringWheelAngle(self):
        print('Getting steering wheel angle ...')
    
    '''
    Torque  at Transmission
    '''
    def getTransmissionTorque(self):
        print('Getting torque at transmission ...')
        
    '''
    Engine speed
    '''
    def getTransmissionTorque(self):
        print('Getting engine speed ...')
    
    
        