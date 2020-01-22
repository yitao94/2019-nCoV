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
    "COUN_CODE" : 36,
} # Australia
AUT = {
    "COUN_CODE" : 40,
} # Austria

# === B ===
BRA = {
    "COUN_CODE" : 76,
} # Brazil

# === C ===
CAN = {
    "COUN_CODE" : 124,
} # Canada
CHN = {
    "COUN_CODE" : 156,
    # === CITY/PROVINCE A ===
    "AH" : {
        "PROV_CODE" : 34,
        "HF" : 551, # Hefei city 
    }, # Anhui province

    # === CITY/PROVINCE B ===
    "BJ" : {
        "PROV_CODE" : 11,
        "BJ" : 10,
    }, # Beijing city
    
    # === CITY/PROVINCE C ===
    "CQ" : {
        "PROV_CODE" : 50,
        "CQ" : 23,
    }, # Chongqing city
    
    # === CITY/PROVINCE D ===
    
    # === CITY/PROVINCE E ===
    
    # === CITY/PROVINCE F ===
    "FJ" : {
        "PROV_CODE" : 35,
        "FZ" : 591, # Fuzhou city
    }, # Fujian province

    # === CITY/PROVINCE G ===
    "GD" : {
        "PROV_CODE" : 44,
        "GZ" : 20, # Guangzhou city
    }, # Guangdong province
    "GS" : {
        "PROV_CODE" : 62,
        "LZ" : 931, # Lanzhou city
    }, # Gansu province
    "GX" : {
        "PROV_CODE" : 45,
        "NN" : 771, # Nanning city
        "GL" : 773, # Guilin city
    }, # Guangxi province
    "GZ" : {
        "PROV_CODE" : 52,
        "GY" : 851, # Guiyang city
    }, # Guizhou province

    # === CITY/PROVINCE H ===
    "HB" : {
        "PROV_CODE" : 42,
        "WH" : 27, # Wuhan city
    }, # Hubei province
    "HBB" : {
        "PROV_CODE" : 13,
        "SJZ" : 311, # Shijiazhuang city
        "JJK" : 313, # Zhangjiakou city
        "XT" : 319, # Xingtai city
    }, # Hebei province
    "HLJ" : {
        "PROV_CODE" : 23,
        "HEB" : 451, # Harbin city
    }, # Heilongjiang province
    "HN" : {
        "PROV_CODE" : 41,
        "ZZ" : 371, # Zhengzhou city
    }, # Henan province
    "HNN" : {
        "PROV_CODE" : 46,
        "HN" : 898, # Hainan
    }, # Hainan province
    "HNNN" : {
        "PROV_CODE" : 43,
        "CS" : 731, # Changsha city
    }, # Hunan province
    
    # === CITY/PROVINCE I ===
    
    # === CITY/PROVINCE J ===
    "JL" : {
        "PROV_CODE" : 22,
        "CC" : 431, # Changchun city
        "JL" : 432, # Jilin city
    }, # Jilin province
    "JS" : {
        "PROV_CODE" : 32,
        "NJ" : 25, # Nanjing city
        "NT" : 513, # Nantong city
    }, # Jiangsu province
    "JX" : {
        "PROV_CODE" : 36,
        "NC" : 791, # Nanchang city
    }, # Jiangxi province

    # === CITY/PROVINCE K ===
    
    # === CITY/PROVINCE L ===
    "LN" : {
        "PROV_CODE" : 21,
        "SY" : 24, # Shenyang city
    }, # Liaoning province

    # === CITY/PROVINCE M ===
    
    # === CITY/PROVINCE N ===
    "NMG" : {
        "PROV_CODE" : 15,
        "HHHT" : 417,
    }, # Neimenggu province
    "NX" : {
        "PROV_CODE" : 64,
        "YC" : 951, # Yinchuan city
    }, # Ningxia province

    # === CITY/PROVINCE O ===
    
    # === CITY/PROVINCE P ===
    
    # === CITY/PROVINCE Q ===
    "QH" : {
        "PROV_CODE" : 63,
        "XN" : 971, # Xining city 
    }, # Qinghai province

    # === CITY/PROVINCE R ===
    
    # === CITY/PROVINCE S ===
    "SC" : {
        "PROV_CODE" : 51,
        "CD" : 28, # Chengdu city
    }, # Sichuan province
    "SD" : {
        "PROV_CODE" : 37,
        "JN" : 531, # Jinan city
    }, # Shandong province
    "SH" : {
        "PROV_CODE" : 31,
        "SH" : 21,
    }, # Shanghai city
    "SX" : {
        "PROV_CODE" : 14,
        "TY" : 351, # Taiyuan city
    }, # Shanxi province
    "SXX" : {
        "PROV_CODE" : 61,
        "XA" : 29, # Xi'an city
    }, # Shaanxi province

    # === CITY/PROVINCE T ===
    "TJ" : {
        "PROV_CODE" : 12, 
        "TJ" : 22, # Tianjin
    }, # Tianjin city
    
    # === CITY/PROVINCE U ===
    
    # === CITY/PROVINCE V ===
    
    # === CITY/PROVINCE W ===
    
    # === CITY/PROVINCE X ===
    "XJ" : {
        "PROV_CODE" : 65,
        "WLMQ" : 991, # Wulumuqi city
    }, # Xinjiang province
    "XZ" : {
        "PROV_CODE" : 54,
        "LS" : 891, # Lasa city
    }, # Xizhang province

    # === CITY/PROVINCE Y ===
    "YN" : {
        "PROV_CODE" : 53,
        "KM" : 871, # Kunming city
    }, # Yunan province

    # === CITY/PROVINCE Z ===
    "ZJ" : {
        "PROV_CODE" : 33,
        "HZ" : 571, # Hangzhou city
    }, # Zhejiang province    

} # P.R. CHINA - mainland

# === D ===
DEU = {
    "COUN_CODE" : 276,    
} # Germany

# === E ===

# === F ===
FRA = {
    "COUN_CODE" : 250,
} # France

# === G ===
GBR = {
    "COUN_CODE" : 826,
} # the United Kingdom

# === H ===
HKG = {
    "COUN_CODE" : 344,
} # Hongkong - CN

# === I ===
IDN = {
    "COUN_CODE" : 360,
} # Indonesia
IND = {
    "COUN_CODE" : 356,
} # India

# === J ===
JPN = {
    "COUN_CODE" : 392,
} # Japan

# === K ===
KOR = {
    "COUN_CODE" : 410,
} # the Republic of Korea

# === L ===

# === M ===
MAC = {
    "COUN_CODE" : 446,
} # Macao - CN
MMR = {
    "COUN_CODE" : 104,
} # Myanmar
MYS = {
    "COUN_CODE" : 458,
} # Malaysia

# === N ===
NPL = {
    "COUN_CODE" : 524,
} # Nepal

# === O ===

# === P ===
PAK = {
    "COUN_CODE" : 586,
} # Pakistan
PHL = {
    "COUN_CODE" : 608,
} # the Philippines

# === Q ===

# === R ===

# === S ===
SGP = {
    "COUN_CODE" : 702,
} # Singapore

# === T ===
THA = {
    "COUN_CODE" : 764,
} # Thailand
TWN = {
    "COUN_CODE" : 158,
} # Taiwan - CN

# === U ===
USA = {
    "COUN_CODE" : 840,
} # the United States

# === V ===
VHM = {
    "COUN_CODE" : 704,
} # Viet Nam

# === W ===

# === X ===

# === Y ===

# === Z ===