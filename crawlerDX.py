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

import requests
from bs4 import BeautifulSoup

URL_DX = r"https://3g.dxy.cn/newh5/view/pneumonia"

def main():
    DX_html = requests.get(URL_DX)  
    DX_html.encoding='utf-8'
    DX_html_soup = BeautifulSoup(DX_html.content, 'lxml')
      
    #print(strhtml.text)
    
    DX_script_listByCountry = str(DX_html_soup.find('script', attrs={'id': 'getListByCountryTypeService1'}))
    DX_content_listByCountry = re.search(r'\[(.*?)\]', DX_script_listByCountry).group()
    utc_now = time.gmtime()
    DX_utc_str =  str(utc_now[0]*100**2+utc_now[1]*100+utc_now[2])+"_"+str(utc_now[3]*100**2+utc_now[4]*100+utc_now[5])# timestamp
    
    # file saving per hour
    with open(os.getcwd()+r"\data\DXY_"+DX_utc_str+".json",'w',encoding='utf-8') as f:
        f.write(DX_content_listByCountry.replace(",",",\n"))
        print("[done] file - {} saved.".format("DXY_"+DX_utc_str+".json"))
    f.close()
    
    # compilation file saving
    with open(os.getcwd()+r"\arc\DXY_compilation.json", "a",encoding='utf-8') as f:
        f.write(DX_content_listByCountry)
        f.write("\n")
    f.close()
    
    #DX_content_dict = json.loads(DX_content_listByCountry)
    return DX_content_dict

if __name__ == '__main__':
    main()
# =============================================================================
#     while True:
#         main()
#         time.sleep(60*60)
# =============================================================================
