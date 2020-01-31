# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 21:55:24 2020

func:
    add dead and cured unit in DXY_csv
    e.g.:
        [538, 0, 1580463165, 0] -> [538, 0, None, None, None, None, 1580463165, 0]

@author: YITAJIN
"""

import os
import sys
sys.path.append("..") #goes to upper directory
import json

from src.areaCode import *
from src.CHN_prov import CHN_PROV_CODE, CHN_PROV_NAME
from src.tool import utc2str, str2list

import pandas as pd

#read current dataframe
DXY_df_addr = os.getcwd().replace(r"\src","")+r"\data\DXY_RT.csv"

DXY_df = pd.read_csv(DXY_df_addr, index_col = "PROV_CODE")
DXY_df_last_column_name = DXY_df.columns[-1]
#print(DXY_df.loc[:, [DXY_df.columns[0], DXY_df.columns[-2]]])
#print(DXY_df.loc[:, [DXY_df.columns[0], DXY_df.columns[-1]]])

for DXY_df_index_i in DXY_df.index:
    DXY_curr_list = str2list(DXY_df.loc[DXY_df_index_i, [DXY_df_last_column_name]].values[0])
    DXY_curr_list.insert(2, None) # total dead
    DXY_curr_list.insert(3, None) # new dead
    DXY_curr_list.insert(4, None) # total cured
    DXY_curr_list.insert(5, None) # new cured
    DXY_df.loc[DXY_df_index_i, [DXY_df_last_column_name]] = [DXY_curr_list]

#print(DXY_df.loc[:, [DXY_df.columns[0], DXY_df.columns[-2]]])
#print(DXY_df.loc[:, [DXY_df.columns[0], DXY_df.columns[-1]]])
    
DXY_df.to_csv(DXY_df_addr, index_label = "PROV_CODE") #index_label