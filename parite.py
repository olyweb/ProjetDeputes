#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 15:07:30 2018

@author: olivier
"""

from argparse import ArgumentParser
import analysis.csv as c_an
import analysis.xml as x_an
import logging as lg


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument('-e', '--extension', help="""Type of file, cvs or xml ?""")
    parser.add_argument('-d', '--datafile', help="""File to be used""")
    parser.add_argument('-v', '--verbose', action='store_true', help="""Make the application talk!""")
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()
    datafile = args.datafile
    if args.verbose:
        lg.basicConfig(level=lg.DEBUG)
    try:
        if datafile == None:
            raise Warning("You must use '-- datafile' option to precise file")
        else:
            try:
                if args.extension == 'csv':
                    c_an.launch_analysis(datafile)
                elif args.extension == 'xml':
                    x_an.launch_analysis(datafile)
            except FileNotFoundError as e:
                print("oups :(, fichier non trouvé : ",e)
            finally:
                lg.info("####### Analysis is over #######")
    except Warning as e:
        lg.warning(e)