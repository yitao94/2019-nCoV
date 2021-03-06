# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 00:12:25 2020

@author: YITAJIN
"""
import time

def utc2str(utc_now=time.gmtime()):
    utc_str =  str(utc_now[0]*100**2+utc_now[1]*100+utc_now[2])+"_"+str(utc_now[3]*100**2+utc_now[4]*100+utc_now[5])# timestamp
    if utc_now[3]<10 and utc_now[3]>0:
        utc_str =  str(utc_now[0]*100**2+utc_now[1]*100+utc_now[2])+"_0"+str(utc_now[3]*100**2+utc_now[4]*100+utc_now[5])
    elif utc_now[3] == 0:
        utc_str =  str(utc_now[0]*100**2+utc_now[1]*100+utc_now[2])+"_00"+str(utc_now[3]*100**2+utc_now[4]*100+utc_now[5])# timestamp
    
    return utc_str

def str2list(listinstr="[]", split_sign=","):
    """func:
        convert str to list
        e.g.:
            "[0, 2]" -> list([0,2])
    update:
        consider None in the string
    """
    old_str = listinstr.replace("[","").replace("]","").replace(" ","")
    old_str_list = old_str.split(split_sign)
    new_str_list = []
    for list_i in old_str_list:
        if list_i == "None":
            new_str_list.append(None)
        else:
            new_str_list.append(int(float(list_i)))
        
    #new_str_list = [int(float(list_i)) for list_i in new_str_list]
    return new_str_list