# -*- coding: utf-8 -*-
"""
Date:           Created on Thu Apr 11 08:21:06 2019
Name:           Armand Moussaouyi and Derek Cotton
Description:    OpenXC
"""

#import re

class Car:
    '''Basic car class'''
    
    def __init__(self, make = 'Chevrolet', model = 'Malibu Classic',year = '2005', port = '127.0.0.1'):
        '''Constructor'''
        self.make = make
        self.model = model
        self.year = year
        self.XC_port = port
        
        # data reading variables
        self.car_speed = 0
        self.engine_speed = 0
        self.voltage_level = 0
        self.current_level = 0
        self.pressure_level = 0
    
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
        return self.car_speed
    
    '''
    Engine speed
    '''
    def getEngineSpeed(self):
        return self.engine_speed
    
    '''
    Voltage level
    '''
    def getVoltageLevel(self):
        return self.voltage_level
    
    '''
    Current level
    '''
    def getCurrentLevel(self):
        return self.current_level
    
    '''
    Pressure level
    '''
    def getPressureLevel(self):
        return self.pressure_level
    
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
        
    def trim_sample_data(self, string_list):
        _data = []
        for i in string_list:
            if (len(i) > 0 and i != ':'):
                _data.append(i)
                
        return _data
    
    def get_live_trace(ip_address, port_number):
        import socket
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip_address, port_number))
            # calling instruction function
            data = s.recv(1024)
            print('Received', repr(data))       # test server
            return data
        
        
    #--------------------------------------------------------------------------
    # Read the UAS id trace from sample file
    #--------------------------------------------------------------------------
    def read_uas_trace(self):
        data = []
        file = open('uas_ids.txt', 'r')
        if file.mode == 'r':
            for line in file:
                line = line.replace('{'  , '')
                line = line.replace('}'  , '')
                line = line.replace('['  , '')
                line = line.replace(']'  , '')
                line = line.replace('\t' , '')
                line = line.replace(','  , '')
                line = line.replace('\n' , '')
                #line = line.rstrip('\n')
                data_points =  line.split(' ')
                
                data_array = self.trim_sample_data(data_points)
                if len(data_array) > 3:
                    if data_array[0] == '0x08':
                       self.car_speed = float(data_array[2])        # get the speed and convert it from string to float
                       print('Speed: ', self.car_speed)
                       
                    if data_array[0] == '0x07':
                        self.engine_speed = float(data_array[2])
                        print('Engine speed: ', self.engine_speed)
                        
                    if data_array[0] == '0x0A':
                        self.voltage_level = float(data_array[2])
                        print('Voltage: ', self.voltage_level)
                        
                    if data_array[0] == '0x0D':
                        self.current_level = float(data_array[2])
                        print('Current level: ', self.current_level)
                        
                    if data_array[0] == '0xA9':
                        self.pressure_level = float(data_array[2])
                        print('Pressure: ', self.pressure_level)
                    
                data.append(line)
            return data
        else:
            return 'No valid trace found!'
   
    #--------------------------------------------------------------------------
    # Read dtc trace from sample file
    #--------------------------------------------------------------------------     
    def read_dtc_trace(self):
        data = []
        #regx = re.compile(r'\W')
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
    
    
        