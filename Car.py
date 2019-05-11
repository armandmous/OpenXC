# -*- coding: utf-8 -*-
"""
Date:           Created on Thu Apr 11 08:21:06 2019
Name:           Armand Moussaouyi and Derek Cotton
Description:    OpenXC
"""

import re

class Car:
    '''Basic car class'''
    
    def __init__(self, make = 'Chevrolet', model = 'Malibu Classic',year = '2005', port = '127.0.0.1'):
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
    def engine_speed(self):
        print('Getting engine speed ...')
        
    #--------------------------------------------------------------------------
    # Read the UAS id trace from sample file
    #--------------------------------------------------------------------------
    def read_uas_trace(self):
        data = []
        file = open('uas_ids.txt', 'r')
        if file.mode == 'r':
            for line in file:
                line = line.replace('{', '')
                line = line.replace('}', '')
                line = line.replace('[', '')
                line = line.replace(']', '')
                line = line.replace('\t', '')
                line = line.replace(',', '')
                #line = line.rstrip('\n')
                data.append(line)
            return data
        else:
            return 'No valid trace found!'
   
    #--------------------------------------------------------------------------
    # Read dtc trace from sample file
    #--------------------------------------------------------------------------     
    def read_dtc_trace(self):
        data = []
        regx = re.compile(r'\W')
        file = open('dtc.txt', 'r')
        if file.mode == 'r':
            for line in file:
                #line = line.rstrip('\n')
                #line = regx.sub('', line)
                line = line.replace('{', '')
                line = line.replace('}', '')
                line = line.replace('[', '')
                line = line.replace(']', '')
                line = line.replace('\t', '')
                line = line.replace(',', '')
                data.append(line)
            return data
        else:
            return ['No valid trace found!']
    
    
        