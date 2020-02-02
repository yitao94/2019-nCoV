# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 23:37:17 2020

run:
    1. read old dataframe
    2. read current json file
    3. loop json and update info in df
    4. save new df

@author: YITAJIN
"""

import os
import json
import datetime
import pandas as pd
import numpy as np
import time

import sys
sys.path.append("..") #goes to upper directory
from src.tool import utc2str, str2list
from src.CHN_prov import CHN_PROV_CODE, CHN_PROV_NAME


DXY_realtime_json_addr_test = r"C:\Users\YITAJIN\RD\Project\2019-nCoV\data\DXYjson\DXY_20200124_012708.json" 

#read current dataframe
DXY_df_addr = os.getcwd()+r"\data\DXY_RT.csv"


def read_csvasdf (csv_addr = DXY_df_addr):
    df =  pd.read_csv(csv_addr, index_col = "PROV_CODE")
    return df

def read_json (json_addr=DXY_realtime_json_addr_test):
    """
    note:
        difference between json.read() and json.read()
    """
    with open(json_addr, 'r', encoding="utf-8") as f:
        json_dict = json.load(f)
    return json_dict

def update_df (df, dict_stru): 
    """
    func:
        update dictionary as structure in dataframe
    version 1 - stru - 20200124:
        [total_comfirmed, new_confirmed, modified_timestamp, time_difference]
    """
    df_last_col = df.columns[-1]
    curr_ts_str = utc2str(time.gmtime())
    df[curr_ts_str] = None
    df_curr_col = df.columns[-1]
    #print(df_last_col, df_curr_col)
    #print(df)
    old_total_confirm = str2list(df.loc[0, [df_last_col]].values[0])[0]
    old_total_dead = str2list(df.loc[0, [df_last_col]].values[0])[0+2]
    if old_total_dead == None:
        old_total_dead = 0
    old_total_cured = str2list(df.loc[0, [df_last_col]].values[0])[0+2+2]
    if old_total_cured == None:
        old_total_cured = 0
    old_total_ts = str2list(df.loc[0, [df_last_col]].values[0])[2+4]
    new_total_confirm = 0
    new_total_dead = 0
    new_total_cured = 0
    new_total_ts = 0
    for dict_i in dict_stru:
        dict_i_id = int(dict_i["provinceId"])
        if dict_i_id in CHN_PROV_CODE:
            if df.loc[dict_i_id,[df_last_col]].values and (df.loc[dict_i_id,[df_last_col]].values[0] is not np.nan): #if former column has value
                old_data_list_str = df.loc[dict_i_id, [df_last_col]].values[0]
                #print(dict_i_id, old_data_list_str)
                old_data_list = str2list(old_data_list_str)
                old_confirmed = old_data_list[0]
                old_dead = old_data_list[0+2]
                if old_dead == None:
                    old_dead = 0
                old_cured = old_data_list[0+2+2]
                if old_cured == None:
                    old_cured = 0
                old_ts = old_data_list[2+4]
                curr_confirmed = dict_i["confirmedCount"]
                new_total_confirm += curr_confirmed
                curr_dead = dict_i["deadCount"]
                curr_dead_new = curr_dead-old_dead
                new_total_dead += curr_dead
                if curr_dead == 0:
                    curr_dead = None
                    curr_dead_new = None
                curr_cured = dict_i["curedCount"]
                curr_cured_new = curr_cured-old_cured
                new_total_cured += curr_cured
                if curr_cured == 0 and curr_cured_new == 0:
                    curr_cured = None
                    curr_cured_new = None
                curr_confirmed_new = curr_confirmed-old_confirmed
                curr_ts = dict_i["modifyTime"]/1000
                if curr_ts> new_total_ts:
                    new_total_ts=curr_ts
                curr_ts_diff = int((datetime.datetime.utcfromtimestamp(curr_ts)-datetime.datetime.utcfromtimestamp(old_ts)).seconds/60/60)
                update_data_list = [curr_confirmed, curr_confirmed_new, curr_dead, curr_dead_new, curr_cured, curr_cured_new, curr_ts, curr_ts_diff]
                #time_diff =
            else: # if former column has not values, give new data list directly
                curr_confirmed = dict_i["confirmedCount"]
                curr_ts = dict_i["modifyTime"]/1000
                update_data_list = [curr_confirmed, 0, curr_ts, 0]
            df.loc[dict_i_id, [df_curr_col]] = [update_data_list]
        elif dict_i_id == 999:
            if dict_i["confirmedCount"]!=0 or dict_i["suspectedCount"]!=0 or dict_i["deadCount"]!=0 or dict_i["curedCount"]!=0:
                print("[warning] un-determined area in China, total confirmed: {}, total suspected: {}, total dead: {}, total cured: {}".format(dict_i["confirmedCount"],dict_i["suspectedCount"],dict_i["deadCount"],dict_i["curedCount"] ))
        else:
            print("[error] prov_code: {} is not in CHN_PROV_CODE".format(dict_i_id))
    curr_total_diff = int((datetime.datetime.utcfromtimestamp(new_total_ts)-datetime.datetime.utcfromtimestamp(old_total_ts)).seconds/60/60)
    update_total_list = [new_total_confirm, new_total_confirm-old_total_confirm,
                         new_total_dead, new_total_dead-old_total_dead,
                         new_total_cured, new_total_cured-old_total_cured,
                         new_total_ts, curr_total_diff]
    df.loc[0, [df_curr_col]] = [update_total_list]
    
    return df
        
        
def save_df2csv(df, csv_fileaddr=DXY_df_addr, indexLabel="PROV_CODE" ):
    df.to_csv(csv_fileaddr, index_label=indexLabel) #index_label



#save new dataframe
# DXY_df.to_csv("DXY_RT.csv", index_label = "PROV_CODE") #index_label


if __name__ == '__main__':
    DXY_df = read_csvasdf()
    DXY_rt_dict = read_json()
    DXY_df_update = update_df(DXY_df, DXY_rt_dict)
    #save_df2csv(DXY_df_update)