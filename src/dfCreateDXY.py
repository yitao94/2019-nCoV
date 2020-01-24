# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 23:13:31 2020

@author: YITAJIN
"""

import os
import sys
sys.path.append("..") #goes to upper directory
import json

from src.areaCode import *
from src.CHN_prov import CHN_PROV_CODE, CHN_PROV_NAME

import pandas as pd

#DXY_realtime as dataframe
DXY_rt_df = pd.DataFrame(CHN_PROV_NAME, columns = ["PROV_NAME"], index=CHN_PROV_CODE)
DXY_rt_df["default"] = [[0, 0, 0, 0] for chn_prov_i in CHN_PROV_NAME] #[total_comfirmed, new_confirmed, modified_timestamp, time_difference]
#DXY_rt_df.loc[0,["default"]]=[[0,0]]


DXY_fileaddr = os.getcwd().replace("src","data")+r"\DXY_RT.csv"
DXY_rt_df.to_csv(DXY_fileaddr, index_label = "PROV_CODE") #index_label
#DXY_rt_df.columns


#r =  pd.read_csv("DXY_RT.csv", index_col = "PROV_CODE")

