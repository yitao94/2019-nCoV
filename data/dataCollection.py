# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 12:04:08 2020

template:
"
 : {
            "source" : "",
            "title" : "",
            "description" : "",
            "post_insit" : "",
            "post_time" : datetime.datetime(2020, 1, , , , ),
            "new_confirmed" : ,
            "new_dead" : ,
            "new_cured" : ,
            "still_isolated" : ,
            "total_confirmed" : ,
            "still_severe" : ,
            "total_isolated" : ,
            "total_isolated_dism" : ,
            "total_isolated_med" : ,
            "total_cured" : ,
            "total_dead" : ,
        },
"

@author: YITAJIN
"""

import time
import datetime
import sys
sys.path.append("..") #goes to upper directory
from src.areaCode import *

# data by city/country list
# === city/country A ===
# === city/country B ===
DATA_BEIJING = {
    "citycode" : str(CHN["COUN_CODE"])+"_"+str(CHN["BJ"]["PROV_CODE"]),
    "cityname" : "CHN_BJ",
    "source" : "http://wjw.beijing.gov.cn/xwzx_20031/wnxw/",
    "timeline" : {
        20200121 : {
            "source" : "http://wjw.beijing.gov.cn/xwzx_20031/wnxw/202001/t20200121_1620353.html",
            "title" : "我市新增5例新型冠状病毒感染的肺炎病例",
            "description" : "",
            "post_insit" : "Beijing Municipal Health Commission",
            "post_time" : datetime.datetime(2020, 1, 21, 23, 59, 59), #default, 23:59:59
            "new_confirmed" : 5,
            "new_dead" : 0,
            "new_cured" : 0,
            "still_isolated" : 21,
            "total_confirmed" : 1+2+1+1+2+2+1, # Xicheng, Haidian, Fengtai, Tongzhou, Daxing, Changping, Outside
            "still_severe" : 0,
            "total_isolated" : 21,
            "total_isolated_dism" : 0,
            "total_isolated_med" : 0,
            "total_cured" : 0,
            "total_dead" : 0,
        },
    }
}
# === city/country C ===
# === city/country D ===
# === city/country E ===
# === city/country F ===
# === city/country G ===
DATA_GUANGDONG = {
    "citycode" : str(CHN["COUN_CODE"])+"_"+str(CHN["GD"]["PROV_CODE"]),
    "cityname" : "CHN_GD",
    "source" : "http://wsjkw.gd.gov.cn/zwyw_yqxx/",
    "timeline" : {
        20200119 : {
            "source" : "http://wsjkw.gd.gov.cn/zwyw_yqxx/content/post_2876057.html",
            "title" : "国家卫生健康委确认我省首例输入性新型冠状病毒感染的肺炎确诊病例",
            "description" : "",
            "post_insit" : "Health Commission of Guangdong Province",
            "post_time" : datetime.datetime(2020, 1, 20, 2, 51, 59),
            "new_confirmed" : 1,
            "new_dead" : 0,
            "new_cured" : 0,
            "still_isolated" : 0,
            "total_confirmed" : 0,
            "still_severe" : 0,
            "total_isolated" : 0,
            "total_isolated_dism" : 0,
            "total_isolated_med" : 0,
            "total_cured" : 0,
            "total_dead" : 0,
        },
        20200120 : {
            "source" : "http://wsjkw.gd.gov.cn/zwyw_yqxx/content/post_2876926.html",
            "title" : "我省积极应对新型冠状病毒感染的肺炎疫情",
            "description" : "",
            "post_insit" : "Health Commission of Guangdong Province",
            "post_time" : datetime.datetime(2020, 1, 20, 20, 0, 37),
            "new_confirmed" : 8+3+1+1, # Shenzhen, Zhuhai, Zhenjiang, Huizhou
            "new_dead" : 0,
            "new_cured" : 0,
            "still_isolated" : 0,
            "total_confirmed" : 13+1,
            "still_severe" : 4+2, # severe, much severe
            "total_isolated" : 0,
            "total_isolated_dism" : 0,
            "total_isolated_med" : 0,
            "total_cured" : 0,
            "total_dead" : 0,
        },
        20200121 : {
            "source" : "http://wsjkw.gd.gov.cn/zwyw_yqxx/content/post_2877668.html",
            "title" : "广东省新型冠状病毒感染的肺炎疫情通报",
            "description" : "",
            "post_insit" : "Health Commission of Guangdong Province",
            "post_time" : datetime.datetime(2020, 1, 21, 22, 13, 11),
            "new_confirmed" : 3, #Shenzhen, Zhuhai, Zhenjiang
            "new_dead" : 0,
            "new_cured" : 0,
            "still_isolated" : 4,
            "total_confirmed" : 17,
            "still_severe" : 5+2, # severe, much severe
            "total_isolated" : 4,
            "total_isolated_dism" : 0,
            "total_isolated_med" : 0,
            "total_cured" : 0,
            "total_dead" : 0,
        },
        20200122 : {
            "source" : "http://wsjkw.gd.gov.cn/zwyw_yqxx/content/post_2877905.html",
            "title" : "广东省新型冠状病毒感染的肺炎疫情通报 （2020年1月22日）",
            "description" : "",
            "post_insit" : "Health Commission of Guangdong Province",
            "post_time" : datetime.datetime(2020, 1, 22, 12, 16, 50),
            "new_confirmed" : 2+4+11+2, #Guangzhou, Shenzhen, Foshan, Shaoguan
            "new_dead" : 0,
            "new_cured" : 0,
            "still_isolated" : 1,
            "total_confirmed" : 26,
            "still_severe" : 7+3, # severe, much severe
            "total_isolated" : 1,
            "total_isolated_dism" : 0,
            "total_isolated_med" : 0,
            "total_cured" : 0,
            "total_dead" : 0,
        },
    }
}
# === city/country H ===
# === city/country I ===
# === city/country J ===
# === city/country K ===
# === city/country L ===
# === city/country M ===
# === city/country N ===
# === city/country O ===
# === city/country P ===
# === city/country Q ===
# === city/country R ===
# === city/country S ===
DATA_SHANGHAI = {
    "citycode" : str(CHN["COUN_CODE"])+"_"+str(CHN["SH"]["PROV_CODE"]),
    "cityname" : "CHN_SH",
    "source" : "http://wsjkw.sh.gov.cn/xwfb/index.html",
    "timeline" : {
        20200120 : {
            "source" : "http://wsjkw.sh.gov.cn/xwfb/20200121/5b01c1a678df4faab338d9ed1efdc958.html",
            "title" : "国家卫健委确认上海首例输入性 新型冠状病毒感染的肺炎确诊病例",
            "description" : "First comfirmed case detected in Shanghai",
            "post_insit" : "Shanghai Municipal Health Commission",
            "post_insit2" : "Shanghai Municipal Administrator of Traditional Chinese Medicine",
            "post_time" : datetime.datetime(2020, 1, 20, 23, 59, 59), #unknow about detail time, default is 23:59:59
            "new_confirmed" : 1,
            "new_dead" : 0,
            "new_cured" : 0,
            "still_isolated" : 2,
            "total_confirmed" : 1,
            "still_severe" : 0,
            "total_isolated" : 2,
            "total_isolated_dism" : 0,
            "total_isolated_med" : 0,
            "total_cured" : 0,
            "total_dead" : 0,
        },
        20200121 : {
            "source" : "http://wsjkw.sh.gov.cn/xwfb/20200121/8fa3da87b0014c9db1308c76cbfe835f.html",
            "title" : "上海确诊第二例输入性 新型冠状病毒感染的肺炎病例",
            "description" : "Second comfirmed case detected in Shanghai",
            "post_insit" : "Shanghai Municipal Health Commission",
            "post_insit2" : "Shanghai Municipal Administrator of Traditional Chinese Medicine",
            "post_time" : datetime.datetime(2020, 1, 21, 11, 59, 59), #unexact, ambiguous
            "new_confirmed" : 1,
            "new_dead" : 0,
            "new_cured" : 0,
            "still_isolated" : 4,
            "total_confirmed" : 2,
            "still_severe" : 0,
            "total_isolated" : 4,
            "total_isolated_dism" : 0,
            "total_isolated_med" : 0,
            "total_cured" : 0,
            "total_dead" : 0,
        },
        20200121.1 : {
            "source" : "http://wsjkw.sh.gov.cn/xwfb/20200121/353b563cdb594b23a19d6e0d37908a11.html",
            "title" : "上海新增4例新型冠状病毒感染的肺炎确诊病例",
            "description" : "",
            "post_insit" : "Shanghai Municipal Health Commission",
            "post_insit2" : "Shanghai Municipal Administrator of Traditional Chinese Medicine",
            "post_time" : datetime.datetime(2020, 1, 21, 19, 0, 0),
            "new_confirmed" : 2+2, # Shanghai, Wuhan
            "new_dead" : 0,
            "new_cured" : 0,
            "still_isolated" : 3,
            "total_confirmed" : 6,
            "still_severe" : 0,
            "total_isolated" : 3,
            "total_isolated_dism" : 0,
            "total_isolated_med" : 0,
            "total_cured" : 0,
            "total_dead" : 0,
        },
        20200122 : {
            "source" : "http://wsjkw.sh.gov.cn/xwfb/20200122/979db31a7a67464195ab3c6421207746.html",
            "title" : "上海新增3例新型冠状病毒感染的肺炎确诊病例",
            "description" : "",
            "post_insit" : "Shanghai Municipal Health Commission",
            "post_insit2" : "Shanghai Municipal Administrator of Traditional Chinese Medicine",
            "post_time" : datetime.datetime(2020, 1, 22, 23, 59, 59), #default
            "new_confirmed" : 3,
            "new_dead" : 0,
            "new_cured" : 0,
            "still_isolated" : 10,
            "total_confirmed" : 9,
            "still_severe" : 0,
            "total_isolated" : 10,
            "total_isolated_dism" : 0,
            "total_isolated_med" : 0,
            "total_cured" : 0,
            "total_dead" : 0,
        },
    }
}
# === city/country T ===
DATA_TIANJIN = {
    "citycode" : str(CHN["COUN_CODE"])+"_"+str(CHN["TJ"]["PROV_CODE"]),
    "cityname" : "CHN_TJ",
    "source" : "http://wsjk.tj.gov.cn/col/col14/index.html",
    "timeline" : {
        20200121 : {
            "source" : "wsjk.tj.gov.cn/art/2020/1/21/art_14_70132.html",
            "title" : "天津确诊2例新型冠状病毒感染的肺炎病例",
            "description" : "",
            "post_insit" : "Tianjin Municipal Health Commission",
            "post_time" : datetime.datetime(2020, 1, 21, 23, 59, 59), # default
            "new_confirmed" : 2,
            "new_dead" : 0,
            "new_cured" : 0,
            "still_isolated" : 0,
            "total_confirmed" : 2,
            "still_severe" : 0,
            "total_isolated" : 0,
            "total_isolated_dism" : 0,
            "total_isolated_med" : 0,
            "total_cured" : 0,
            "total_dead" : 0,
        }
    }
}

# === city/country U ===
# === city/country V ===
# === city/country W ===
DATA_WUHAN = {
    "citycode" : str(CHN["COUN_CODE"])+"_"+str(CHN["HB"]["PROV_CODE"])+"_"+str(CHN["HB"]["WH"]),
    "cityname" : "CHN_HB_WH",
    "source" : "http://wjw.wuhan.gov.cn/front/web/list2nd/no/710",
    "timeline" : { # timeline of report issued
        20191231 : {
            "source" : "http://wjw.wuhaHB_WH,n.gov.cn/front/web/showDetail/2019123108989",
            "title" : "武汉市卫健委关于当前我市肺炎疫情的情况通报",
            "description" : "",
            "post_insit" : "Wuhan Municipal Health Commission", # post insititute
            "post_time" : datetime.datetime(2019, 12, 31, 13, 38, 5), # local time in Beijing
            "new_confirmed" : 0,
            "new_dead" : 0,
            "new_cured" : 0,
            "still_isolated" : 0,
            "total_confirmed" : 27,
            "still_severe" : 7,
            "total_isolated" : 0,
            "total_isolated_dism" : 0,
            "total_isolated_med" : 0,
            "total_cured" : 0,
            "total_dead" : 0,
        },
        20200103 : {
            "source" : "http://wjw.wuhan.gov.cn/front/web/showDetail/2020010309017",
            "title" : "武汉市卫健委关于不明原因的病毒性肺炎情况通报",
            "description" : "",
            "post_insit" : "Wuhan Municipal Health Commission",
            "post_time" : datetime.datetime(2020, 1, 3, 17, 0, 42),
            "new_confirmed" : 0,
            "new_dead" : 0,
            "new_cured" : 0,
            "still_isolated" : 0,
            "total_confirmed" : 44,
            "still_severe" : 11,
            "total_isolated" : 121,
            "total_isolated_dism" : 0,
            "total_isolated_med" : 0,
            "total_cured" : 0,
            "total_dead" : 0,
        },
        20200105 : {
            "source" : "http://wjw.wuhan.gov.cn/front/web/showDetail/2020010509020",
            "title" : "武汉市卫生健康委员会关于不明原因的病毒性肺炎情况通报",
            "description" : "",
            "post_insit" : "Wuhan Municipal Health Commission",
            "post_time" : datetime.datetime(2020, 1, 5, 20, 33, 24),
            "new_confirmed" : 0,
            "new_dead" : 0,
            "new_cured" : 0,
            "still_isolated" : 0,
            "total_confirmed" : 57,
            "still_severe" : 7,
            "total_isolated" : 163,
            "total_isolated_dism" : 0,
            "total_isolated_med" : 0,
            "total_cured" : 0,
            "total_dead" : 0,
        },
        20200111 : {
            "source" : "http://wjw.wuhan.gov.cn/front/web/showDetail/2020011109035",
            "title" : "武汉市卫生健康委关于不明原因的病毒性肺炎情况通报",
            "description" : "",
            "post_insit" : "Wuhan Municipal Health Commission",
            "post_time" : datetime.datetime(2020, 1, 11, 7, 4, 11),
            "new_confirmed" : 0,
            "new_dead" : 0,
            "new_cured" : 0,
            "still_isolated" : 0,
            "total_confirmed" : 41,
            "still_severe" : 7,
            "total_isolated" : 739,
            "total_isolated_dism" : 0,
            "total_isolated_med" : 419, # isolated of medical people
            "total_cured" : 2,
            "total_dead" : 1,
        },
        20200112 : {
            "source" : "http://wjw.wuhan.gov.cn/front/web/showDetail/2020011209037",
            "title" : "武汉市卫生健康委员会关于新型冠状病毒感染的肺炎情况通报",
            "description" : "Determine the type of virus is called nCoV, short of 'the novel coronavirus'", 
            "post_insit" : "Wuhan Municipal Health Commission",
            "post_time" : datetime.datetime(2020, 1, 12, 20, 10, 13),
            "new_confirmed" : 0,
            "new_dead" : 0,
            "new_cured" : 4,
            "still_isolated" : 717,
            "total_confirmed" : 41,
            "still_severe" : 7,
            "total_isolated" : 763,
            "total_isolated_dism" : 46, # isolation dismissed
            "total_isolated_med" : None,
            "total_cured" : 6,
            "total_dead" : 1,
        },
        20200113 : {
            "source" : "http://wjw.wuhan.gov.cn/front/web/showDetail/2020011309038",
            "title" : "武汉市卫生健康委员会关于新型冠状病毒感染的肺炎情况通报",
            "description" : "",
            "post_insit" : "Wuhan Municipal Health Commission",
            "post_time" : datetime.datetime(2020, 1, 13, 19, 0, 19),
            "new_confirmed" : 0,
            "new_dead" : 0,
            "new_cured" : 1,
            "still_isolated" : 687,
            "total_confirmed" : 41,
            "still_severe" : 6,
            "total_isolated" : 763,
            "total_isolated_dism" : 76,
            "total_isolated_med" : None,
            "total_cured" : 7,
            "total_dead" : 1,
        },
        20200114 : {
            "source" : "http://wjw.wuhan.gov.cn/front/web/showDetail/2020011409039",
            "title" : "武汉市卫生健康委员会关于新型冠状病毒感染的肺炎情况通报",
            "description" : "First comfirmed case out of mainland China",
            "post_insit" : "Wuhan Municipal Health Commission",
            "post_time" : datetime.datetime(2020, 1, 14, 22, 5, 36),
            "new_confirmed" : 0,
            "new_dead" : 0,
            "new_cured" : 0,
            "still_isolated" : 576,
            "total_confirmed" : 41,
            "still_severe" : 6,
            "total_isolated" : 763,
            "total_isolated_dism" : 187,
            "total_isolated_med" : None,
            "total_cured" : 7,
            "total_dead" : 1,
        },
        20200115 : {
            "source" : "http://wjw.wuhan.gov.cn/front/web/showDetail/2020011509046",
            "title" : "武汉市卫生健康委员会关于新型冠状病毒感染的肺炎情况通报",
            "description" : "",
            "post_insit" : "Wuhan Municipal Health Commission",
            "post_time" : datetime.datetime(2020, 1, 15, 21, 39, 12),
            "new_confirmed" : 0,
            "new_dead" : 0,
            "new_cured" : 0,
            "still_isolated" : 313,
            "total_confirmed" : 41,
            "still_severe" : 6,
            "total_isolated" : 763,
            "total_isolated_dism" : 450,
            "total_isolated_med" : None,
            "total_cured" : 7,
            "total_dead" : 1,
        },
        20200116 : {
            "source" : "http://wjw.wuhan.gov.cn/front/web/showDetail/2020011609057",
            "title" : "武汉市卫生健康委员会关于新型冠状病毒感染的肺炎情况通报",
            "description" : "New dead is 69-year-old, was fever on 20191231, went to hospital on 20200104, dead on 20200115T004500",
            "post_insit" : "Wuhan Municipal Health Commission",
            "post_time" : datetime.datetime(2020, 1, 16, 23, 55, 45),
            "new_confirmed" : 0,
            "new_dead" : 1,
            "new_cured" : 5,
            "still_isolated" : 119,
            "total_confirmed" : 41,
            "still_severe" : None,
            "total_isolated" : 763,
            "total_isolated_dism" : 644,
            "total_isolated_med" : None,
            "total_cured" : 12,
            "total_dead" : 2,
        },
        20200117 : {
            "source" : "http://wjw.wuhan.gov.cn/front/web/showDetail/2020011809064",
            "title" : "武汉市卫生健康委员会关于新型冠状病毒感染的肺炎情况通报",
            "description" : "New comfirmed case happened during from Jan. 5th to 8th, Case in Japan has been cured",
            "post_insit" : "Wuhan Municipal Health Commission",
            "post_time" : datetime.datetime(2020, 1, 18, 0, 10, 55),
            "new_confirmed" : 4,
            "new_dead" : 0,
            "new_cured" : 3,
            "still_isolated" : 98,
            "total_confirmed" : 45,
            "still_severe" : 5,
            "total_isolated" : 763,
            "total_isolated_dism" : 665,
            "total_isolated_med" : None,
            "total_cured" : 15,
            "total_dead" : 2,
        },
        20200118 : {
            "source" : "http://wjw.wuhan.gov.cn/front/web/showDetail/2020011909074",
            "title" : "武汉市卫生健康委员会关于新型冠状病毒感染的肺炎情况通报",
            "description" : "Optimized checking dose used for sample",
            "post_insit" : "Wuhan Municipal Health Commission",
            "post_time" : datetime.datetime(2020, 1, 19, 0, 43, 34),
            "new_confirmed" : 17,
            "new_dead" : 0,
            "new_cured" : 4,
            "still_isolated" : 82,
            "total_confirmed" : 62,
            "still_severe" : 8,
            "total_isolated" : 763,
            "total_isolated_dism" : 681,
            "total_isolated_med" : None,
            "total_cured" : 19,
            "total_dead" : 2,
        },
        20200119 : {
            "source" : "http://wjw.wuhan.gov.cn/front/web/showDetail/2020012009077",
            "title" : "武汉市卫生健康委员会关于新型冠状病毒感染的肺炎情况通报",
            "description" : "",
            "post_insit" : "Wuhan Municipal Health Commission",
            "post_time" : datetime.datetime(2020, 1, 20, 2, 42, 40),
            "new_confirmed" : 59+77, #20200118, 0~24, 59; #20200119, 0~22, 77
            "new_dead" : 1,
            "new_cured" : 5+1+1, #20200118, 0~24, 5; #20200119, 0~22, 1; #20200119, 22~24, 1
            "still_isolated" : 90,
            "total_confirmed" : 198,
            "still_severe" : 35+9, # severe, much severe
            "total_isolated" : 817,
            "total_isolated_dism" : 727,
            "total_isolated_med" : None,
            "total_cured" : 25,
            "total_dead" : 3,
        },
        20200121 : {
            "source" : "http://wjw.wuhan.gov.cn/front/web/showDetail/2020012109085",
            "title" : "武汉市卫生健康委员会关于新型冠状病毒感染的肺炎情况通报",
            "description" : "",
            "post_insit" : "Wuhan Municipal Health Commission",
            "post_time" : datetime.datetime(2020, 1, 20, 2, 42, 40),
            "new_confirmed" : 60,
            "new_dead" : 2,
            "new_cured" : 0,
            "still_isolated" : 249,
            "total_confirmed" : 258,
            "still_severe" : 51+12, # severe, much severe
            "total_isolated" : 988,
            "total_isolated_dism" : 739,
            "total_isolated_med" : None,
            "total_cured" : 25,
            "total_dead" : 6,
        },
    }
}

# === city/country X ===
# === city/country Y ===
# === city/country Z ===
# === city/country misc ===
