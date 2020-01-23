# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 22:38:05 2020

func:
    list all chinese province code and name in sorted lists for importing by other outer .py script

return:
    CHN_PROV_CODE, CHN_PROV_NAME

@author: YITAJIN
"""

from src.areaCode import *

CHN_PROV_CODE = [11,12,13,14,15,21,22,23,31,32,33,34,35,36,37,41,42,43,44,45,46,50,51,52,53,54,61,62,63,64,65,71,81,82]
CHN_PROV_NAME = ['BEIJING','TIANJIN','HEBEI','SHANXI','NEIMENGGU','LIAONING','JILIN','HEILONGJIANG','SHANGHAI','JIANGSU','ZHEJIANG','ANHUI','FUJIAN','JIANGXI','SHANDONG','HENAN','HUBEI','HUNAN','GUANGZHOU','GUANGXI','HAINAN','CHONGQING','SICHUAN','GUIZHOU','YUNAN','XIZANG','SHAANXI','GANSU','QINGHAI','NINGXIA','XIJIANG','TAIWAN','HONGKONG','MACAO']

if __name__ == '__main__':
    CHN_prov_code_list = []
    for CHN_prov_code_i in CHN.keys():
        if isinstance(CHN_prov_code_i,int):
            CHN_prov_code_list.append(CHN_prov_code_i)
    CHN_prov_code_list.sort()
    
    CHN_prov_name_list = []
    for CHN_prov_name_i in CHN_prov_code_list:
        CHN_prov_name_list.append(CHN[CHN_prov_name_i])