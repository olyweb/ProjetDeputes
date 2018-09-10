#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 15:31:15 2018

@author: olivier

analysis of cvs file
"""

from os import path

def launch_analysis(data_file):
    directory = path.dirname(__file__) # we get the rigth path
    path_to_file = path.join(directory, "../data", data_file)
    
    with open(path_to_file, 'r') as f:
        preview = f.readline() # read the first line
        
        print("Preview of the file :{}".format(preview))
   
    
if __name__ == '__main__':
    launch_analysis('current_mps.csv')