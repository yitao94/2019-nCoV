# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:23:46 2020

source:
    1. The data source is coming from compilation of Dingxiang Yisheng @ Dingxiang Yuan society 

toolchain:
    1. Python爬虫入门教程：超级简单的Python爬虫教程 [http://c.biancheng.net/view/2011.html]
    2. DXY-2019-nCoV-Crawler [https://github.com/BlankerL/DXY-2019-nCoV-Crawler/blob/master/crawler.py]
@author: YITAJIN
"""

import time
import calendar
import datetime
import re
import os
import json
import logging

import sys
sys.path.append("..") #goes to upper directory

import requests
from bs4 import BeautifulSoup
from analysisDXY import *

URL_DX = r"https://3g.dxy.cn/newh5/view/pneumonia"

#logging definition

#logging.basicConfig(filename=os.getcwd()+r"\log\crawlerDX.log", filemode="a", level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger("crawlerDX_logger")
logger.setLevel(logging.DEBUG)

loggingFH = logging.FileHandler(os.getcwd()+r"\log\crawlerDX.log", "a") #filehandler
loggingSH = logging.StreamHandler() #streamhandler
loggingFH.setLevel(logging.INFO)
loggingSH.setLevel(logging.INFO)

loggingFormat = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
loggingFH.setFormatter(loggingFormat)
loggingSH.setFormatter(loggingFormat)

logger.addHandler(loggingFH)
logger.addHandler(loggingSH)

logger.info("[running] program starts")
logger.info("[environment] current location: {}".format(os.getcwd()))

def main():
    DX_html = requests.get(URL_DX)  
    
    DX_html.encoding='utf-8'
    DX_html_soup = BeautifulSoup(DX_html.content, 'lxml')
      
    #print(strhtml.text)
    
    DX_script_listByCountry = str(DX_html_soup.find('script', attrs={'id': 'getListByCountryTypeService1'}))
    DX_content_listByCountry = re.search(r'\[(.*?)\]', DX_script_listByCountry).group()
    utc_now = time.gmtime()
    DX_utc_str =  str(utc_now[0]*100**2+utc_now[1]*100+utc_now[2])+"_"+str(utc_now[3]*100**2+utc_now[4]*100+utc_now[5])# timestamp
    if utc_now[3] < 10:
        DX_utc_str = DX_utc_str.split("_")[0]+"_0"+DX_utc_str.split("_")[1] #consider the case of hour value less than 10, 2-digit
    
    # file saving per hour
    with open(os.getcwd()+r"\data\DXYjson\DXY_"+DX_utc_str+".json",'w',encoding='utf-8') as f:
        f.write(DX_content_listByCountry.replace(",",",\n"))
        #print("[done] file - {} saved.".format("DXY_"+DX_utc_str+".json"))
        logger.info("[done] file - {} saved.".format("DXY_"+DX_utc_str+".json"))
    f.close()
    
    # compilation only content by city list- file saving
    with open(os.getcwd()+r"\arc\DXY_bycity_compilation.json", "a",encoding='utf-8') as f:
        f.write(DX_content_listByCountry)
        f.write("\n")
        #print("[update] file - {} updated - {}".format("DXY_bycity_compilation.json", str(datetime.datetime.now())))
        logger.info("[update] file - {} updated - {}".format("DXY_bycity_compilation.json", str(datetime.datetime.now())))
    f.close()
    
    # compilation full content - file saving
    with open(os.getcwd()+r"\arc\DXY_full_compilation.json", "a",encoding='utf-8') as f:
        f.write("\n{} START - {} {}\n".format("="*10, DX_utc_str, "="*10))
        f.write(str(DX_html_soup))
        f.write("\n{} END - {} {}\n".format("="*10, DX_utc_str, "="*10))
        #print("[update] file - {} updated - {}".format("DXY_full_compilation.json", str(datetime.datetime.now())))
        logger.info("[update] file - {} updated - {}".format("DXY_full_compilation.json", str(datetime.datetime.now())))
    f.close()
    
    DX_content_dict = json.loads(DX_content_listByCountry)
    return DX_content_listByCountry, DX_content_dict

if __name__ == '__main__':
    while True:
        try:
            #read csv as df
            DXY_df = read_csvasdf()
            #read json
            #DXY_rt_dict = read_json()
            DXY_rt_content, DXY_rt_dict = main()
            #update df
            DXY_df_update = update_df(DXY_df, DXY_rt_dict)
            print(DXY_df_update.loc[:,[DXY_df_update.columns[0], DXY_df_update.columns[-1]]])
            #save df as csv
            save_df2csv(DXY_df_update)
            time.sleep(60*60) #20min
        except requests.exceptions.ConnectionError:
            #print("[error] cannot connect url: {} - {}".format(URL_DX,str(datetime.datetime.now())))
            logger.info("[error] cannot connect url: {} - {}".format(URL_DX,str(datetime.datetime.now())))
            time.sleep(60)
            
        
# =============================================================================
#     while True:
#         main()
#         time.sleep(60*60)
# =============================================================================
