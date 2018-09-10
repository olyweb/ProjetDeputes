#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 15:07:30 2018

@author: olivier
"""

from argparse import ArgumentParser
import analysis.csv as c_an
import analysis.xml as x_an


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument('-e', '--extension', help="""Type of file, cvs or xml ?""")
    parser.add_argument('-d', '--datafile', help="""File to be used""")
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()
    datafile = args.datafile
    if not datafile:
        print(" You must use '-- datafile' option to precise file")
    elif args.extension == 'csv':
        c_an.launch_analysis(datafile)
    elif args.extension == 'xml':
        x_an.launch_analysis(datafile)