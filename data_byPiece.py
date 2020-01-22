# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 09:55:07 2020

goal:
    1. data recording from piece of News
    2. create .json file for showing

tool:
    1. dict(zip(['one', 'two', 'three'], [[1,2,3], 2, 3]))
    2. 

@author: YITAJIN
"""

import sys
sys.path.append("..") #goes to upper directory
from src.areacode import *

import time
import datetime
import json
import os

dir_curr = os.getcwd()

# list of key of dict(CHN) in areacode.py
CHN_prov_list = []
for CHN_dict_i in CHN.keys():
    if CHN_dict_i == "COUN_CODE":
        CHN_coun_code = CHN["COUN_CODE"]
    else:
        CHN_prov_list.append(CHN_dict_i)
#print(CHN_coun_code, CHN_prov_list)

CHN_prov_info_list = []
for CHN_prov_i in CHN_prov_list:
    prov_i_index = str(CHN["COUN_CODE"])+"_"+str(CHN[CHN_prov_i]["PROV_CODE"])
    prov_i_name = "CHN"+"_"+ CHN_prov_i
    prov_i_new_comfirmed = 0
    prov_i_new_suspected = 0
    prov_i_new_isolated = 0
    prov_i_new_dead = 0
    prov_i_new_cured = 0
    prov_i_new_utc_time = time.gmtime()[0]*100**2+time.gmtime()[1]*100+time.gmtime()[2]
    prov_i_new_local_time = time.localtime()[0]*100**2+time.localtime()[1]*100+time.localtime()[2]
    prov_i_new_dict = dict(zip(["new_comfirmed", "new_suspected", "new_isolated", "new_dead", "new_cured"], [prov_i_new_comfirmed, prov_i_new_suspected, prov_i_new_isolated, prov_i_new_dead, prov_i_new_cured]))
    #prov_i_new = [prov_i_new_local_time, prov_i_new_comfirmed, prov_i_new_suspected, prov_i_new_isolated, prov_i_new_dead, prov_i_new_cured]
    prov_i_total_comfirmed = 0
    prov_i_total_cured = 0
    prov_i_total_dead = 0
    prov_i_total_dict = dict(zip(["total_comfirmed", "total_cured", "total_dead"], [prov_i_total_comfirmed, prov_i_total_cured, prov_i_total_dead]))
    #prov_i_total = [prov_i_total_comfirmed, prov_i_total_cured, prov_i_total_dead]
    prov_i_temp_dict = dict(zip(["prov_index", "prov_name", "new_localtime", "prov_new", "prov_total"], [prov_i_index, prov_i_name, prov_i_new_local_time, prov_i_new_dict, prov_i_total_dict]))
    CHN_prov_info_list.append(prov_i_temp_dict)
CHN_prov_info_list_in_json = json.dumps(CHN_prov_info_list)

with open(dir_curr+r"\data\data_byPiece.json",'w',encoding='utf-8') as f:
    f.write(CHN_prov_info_list_in_json.replace(" ","").replace(",",",\n"))
