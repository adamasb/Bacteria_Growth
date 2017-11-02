# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 12:08:05 2017

@author: adams
"""

import numpy as np
import pandas as pd

def dataLoad(filename):
    
    filein = open(filename, "r") # Opens the file for reading
    lines = filein.readlines() # Reads all lines into an array
    
    
    rows = len(lines)
    
    # we create three empty arrays with the length of the columns from the original file
    temp = np.zeros(rows)
    growth = np.zeros(rows)
    bacteria = np.zeros(rows)
    
    # we assign each value in every row to our empty arrays
    
    for i in range(rows):
        a,b,c = lines[i].split()
        temp[i] = a
        growth[i] = b
        bacteria[i] = c
        
        # errror handling, we check if the values from the file are within the limits, if not we output error message and remove the line
        if (temp[i] < 10 or temp[i] > 60):
            temp[i],growth[i],bacteria[i] = 0,0,0
            print("error, the temperature from line", i , "was out of bounds")
        
        elif (growth[i] < 0):
            temp[i],growth[i],bacteria[i] = 0,0,0
            print("error, the growth rate from line", i , "was out of bounds")
        
        elif (bacteria[i] < 1 or bacteria[i] > 4):
            temp[i],growth[i],bacteria[i] = 0,0,0
            print("error, the bacteria from line", i , "was out of bounds")
            
    #remove all lines with errors
    temp,growth,bacteria = temp[temp!=0],growth[growth!=0],bacteria[bacteria!=0]
    
    
    # put all the sigle vectors together into a vertical matrix
    data = np.vstack((temp,growth,bacteria))
    
    #transpose the matrix to achieve correct format
    data = data.T
    
    
    
    return data
