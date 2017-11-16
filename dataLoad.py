# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 12:08:05 2017

@author: marcus & adams
"""

#-----------------------------------------------------------------------------

#imports
import numpy as np
import pandas as pd

#-----------------------------------------------------------------------------

#dataLoad function
def dataLoad(filename):
    
    #We open our file and read all lines into an array
    filein = open(filename, "r")
    lines = filein.readlines()
    
    #We define the lenght of our lines
    rows = len(lines)
    
    #We create three empty arrays with the length of the columns from the given file
    temp = np.zeros(rows)
    growth = np.zeros(rows)
    bacteria = np.zeros(rows)
    
    #We create a line between our error messages and line above (in the main script)
    print("")

#-----------------------------------------------------------------------------

    #We assign each value in every row to our empty arrays    
    for i in range(rows):
        a,b,c = lines[i].split()
        temp[i] = a
        growth[i] = b
        bacteria[i] = c
        
#-----------------------------------------------------------------------------

        #We check if the values from the file are within the limit, and if it's not we print an error message
        if (temp[i] < 10 or temp[i] > 60):
            temp[i],growth[i],bacteria[i] = 0,0,0
            print("error, the temperature from line", i+1 , "was out of bounds")
        
        elif (growth[i] < 0):
            temp[i],growth[i],bacteria[i] = 0,0,0
            print("error, the growth rate from line", i+1 , "was out of bounds")
        
        elif (bacteria[i] < 1 or bacteria[i] > 4):
            temp[i],growth[i],bacteria[i] = 0,0,0
            print("error, the bacteria from line", i+1 , "was out of bounds")
            
#-----------------------------------------------------------------------------
            
    #We remove all lines with errors
    temp,growth,bacteria = temp[temp!=0],growth[growth!=0],bacteria[bacteria!=0]
    
    #We combine all single vectors into a vertical matrix
    data = np.vstack((temp,growth,bacteria))
    
    #We transpose the matrix to achieve correct format
    data = data.T
    
    return data

#-----------------------------------------------------------------------------


