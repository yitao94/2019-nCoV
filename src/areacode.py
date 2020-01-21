# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 21:53:33 2020

source:
    1. "fanwen.jianlimoban.net/466535/",
    2. "www.ccb.com/cn/OtherResource/bankroll/html/code_help.html",
    3. "https://www.chahaoba.com/全国电话区号",
    4. "https://baike.baidu.com/item/世界各国和地区名称代码/6560023?fr=aladdin"],

@author: YITAJIN
"""

# === country code list ===
# === A ===
AUS = {
    "COUN_CODE" : 036,
}, # Australia
AUT = {
    "COUN_CODE" : 040,
}, # Austria

# === B ===
BRA = {
    "COUN_CODE" : 076,
}, # Brazil

# === C ===
CAN = {
    "COUN_CODE" : 124,
}, # Canada
CHN = {
    "COUN_CODE" : 156,
    # === CITY/PROVINCE A ===
    "AH" : {
        "PROV_CODE" : 34,
        "HF" : 0551, # Hefei city 
    }, # Anhui province

    # === CITY/PROVINCE B ===
    "BJ" : {
        "PROV_CODE" : 11,
        "BJ" : 010,
    }, # Beijing city
    
    # === CITY/PROVINCE C ===
    "CQ" : {
        "PROV_CODE" : 50,
        "CQ" : 023,
    }, # Chongqing city
    
    # === CITY/PROVINCE D ===
    
    # === CITY/PROVINCE E ===
    
    # === CITY/PROVINCE F ===
    "FJ" : {
        "PROV_CODE" : 35,
        "FZ" : 0591, # Fuzhou city
    }, # Fujian province

    # === CITY/PROVINCE G ===
    "GD" : {
        "PROV_CODE" : 44,
        "GZ" : 020, # Guangzhou city
    }, # Guangdong province
    "GS" : {
        "PROV_CODE" : 62,
        "LZ" : 0931, # Lanzhou city
    }, # Gansu province
    "GX" : {
        "PROV_CODE" : 45,
        "NN" : 0771, # Nanning city
        "GL" : 0773, # Guilin city
    }, # Guangxi province
    "GZ" : {
        "PROV_CODE" : 52,
        "GY" : 0851, # Guiyang city
    }, # Guizhou province

    # === CITY/PROVINCE H ===
    "HB" : {
        "PROV_CODE" : 42,
        "WH" : 027, # Wuhan city
    }, # Hubei province
    "HBB" : {
        "PROV_CODE" : 13,
        "SJZ" : 0311, # Shijiazhuang city
        "JJK" : 0313, # Zhangjiakou city
        "XT" : 0319, # Xingtai city
    }, # Hebei province
    "HLJ" : {
        "PROV_CODE" : 23,
        "HEB" : 0451, # Harbin city
    }, # Heilongjiang province
    "HN" : {
        "PROV_CODE" : 41,
        "ZZ" : 0371, # Zhengzhou city
    }, # Henan province
    "HNN" : {
        "PROV_CODE" : 46,
        "HN" : 0898, # Hainan
    }, # Hainan province
    "HNNN" : {
        "PROV_CODE" : 43,
        "CS" : 0731, # Changsha city
    }, # Hunan province
    
    # === CITY/PROVINCE I ===
    
    # === CITY/PROVINCE J ===
    "JL" : {
        "PROV_CODE" : 22,
        "CC" : 0431, # Changchun city
        "JL" : 0432, # Jilin city
    }, # Jilin province
    "JS" : {
        "PROV_CODE" : 32,
        "NJ" : 025, # Nanjing city
        "NT" : 0513, # Nantong city
    }, # Jiangsu province
    "JX" : {
        "PROV_CODE" : 36,
        "NC" : 0791, # Nanchang city
    }, # Jiangxi province

    # === CITY/PROVINCE K ===
    
    # === CITY/PROVINCE L ===
    "LN" : {
        "PROV_CODE" : 21,
        "SY" : 024, # Shenyang city
    }, # Liaoning province

    # === CITY/PROVINCE M ===
    
    # === CITY/PROVINCE N ===
    "NMG" : {
        "PROV_CODE" : 15,
        "HHHT" : 0417,
    }, # Neimenggu province
    "NX" : {
        "PROV_CODE" : 64,
        "YC" : 0951, # Yinchuan city
    }, # Ningxia province

    # === CITY/PROVINCE O ===
    
    # === CITY/PROVINCE P ===
    
    # === CITY/PROVINCE Q ===
    "QH" : {
        "PROV_CODE" : 63,
        "XN" : 0971, # Xining city 
    }, # Qinghai province

    # === CITY/PROVINCE R ===
    
    # === CITY/PROVINCE S ===
    "SC" : {
        "PROV_CODE" : 51,
        "CD" : 028, # Chengdu city
    }, # Sichuan province
    "SD" : {
        "PROV_CODE" : 37,
        "JN" : 0531, # Jinan city
    }, # Shandong province
    "SH" : {
        "PROV_CODE" : 31,
        "SH" : 021,
    }, # Shanghai city
    "SX" : {
        "PROV_CODE" : 14,
        "TY" : 0351, # Taiyuan city
    }, # Shanxi province
    "SXX" : {
        "PROV_CODE" : 61,
        "XA" : 029, # Xi'an city
    }, # Shaanxi province

    # === CITY/PROVINCE T ===
    "TJ" : {
        "PROV_CODE" : 12, 
        "TJ" : 022, # Tianjin
    }, # Tianjin city
    
    # === CITY/PROVINCE U ===
    
    # === CITY/PROVINCE V ===
    
    # === CITY/PROVINCE W ===
    
    # === CITY/PROVINCE X ===
    "XJ" : {
        "PROV_CODE" : 65,
        "WLMQ" : 0991, # Wulumuqi city
    }, # Xinjiang province
    "XZ" : {
        "PROV_CODE" : 54,
        "LS" : 0891, # Lasa city
    }, # Xizhang province

    # === CITY/PROVINCE Y ===
    "YN" : {
        "PROV_CODE" : 53,
        "KM" : 0871, # Kunming city
    }, # Yunan province

    # === CITY/PROVINCE Z ===
    "ZJ" : {
        "PROV_CODE" : 33,
        "HZ" : 0571, # Hangzhou city
    }, # Zhejiang province    

}, # P.R. CHINA - mainland

# === D ===
DEU = {
    "COUN_CODE" : 276,    
}, # Germany

# === E ===

# === F ===
FRA = {
    "COUN_CODE" : 250,
}, # France

# === G ===
GBR = {
    "COUN_CODE" : 826,
}, # the United Kingdom

# === H ===
HKG = {
    "COUN_CODE" : 344,
}, # Hongkong - CN

# === I ===
IDN = {
    "COUN_CODE" : 360,
}, # Indonesia
IND = {
    "COUN_CODE" : 356,
}, # India

# === J ===
JPN = {
    "COUN_CODE" : 392,
}, # Japan

# === K ===
KOR = {
    "COUN_CODE" : 410,
}, # the Republic of Korea

# === L ===

# === M ===
MAC = {
    "COUN_CODE" : 446,
}, # Macao - CN
MMR = {
    "COUN_CODE" : 104,
}, # Myanmar
MYS = {
    "COUN_CODE" : 458,
}, # Malaysia

# === N ===
NPL = {
    "COUN_CODE" : 524,
}, # Nepal

# === O ===

# === P ===
PAK = {
    "COUN_CODE" : 586,
}, # Pakistan
PHL = {
    "COUN_CODE" : 608,
}, # the Philippines

# === Q ===

# === R ===

# === S ===
SGP = {
    "COUN_CODE" : 702,
}, # Singapore

# === T ===
THA = {
    "COUN_CODE" : 764,
}, # Thailand
TWN = {
    "COUN_CODE" : 158,
}, # Taiwan - CN

# === U ===
USA = {
    "COUN_CODE" : 840,
}, # the United States

# === V ===
VHM = {
    "COUN_CODE" : 704,
} # Viet Nam

# === W ===

# === X ===

# === Y ===

# === Z ===