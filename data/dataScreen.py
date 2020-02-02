# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 18:01:52 2020

func:
    screen DXY_RT.csv

@author: YITAJIN
"""

import time
import sys
sys.path.append("..") #goes to upper directory
import os


from analysisDXY import *

if __name__ == '__main__':
    while True:
        #i=os.system("cls")
        DXY_df = read_csvasdf(r"DXY_RT.csv")
        print("\r{}".format(DXY_df.loc[:, [DXY_df.columns[0], DXY_df.columns[-1]]]),end="") #all province
        #print("\r{}".format("hello world"),end="")
        time.sleep(30*60) #30mins

