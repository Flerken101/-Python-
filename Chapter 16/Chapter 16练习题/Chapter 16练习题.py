#!/usr/bin/python
# -*- coding:utf8 -*-

#16.2  比较锡卡特和死亡谷的气温
import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename_v = "death_valley_2014.csv"
with open(filename_v) as v:
    reader_v = csv.reader(v)
    header_row_v = next(reader_v)

    dates_v, highs_v, lows_v = [], [], []
    for row_v in reader_v:
        try:
            date_v = datetime.strptime(row_v[0], "%Y-%m-%d")
            high_v = int(row_v[1])
            low_v = int(row_v[3])
        except ValueError:
            print(date_v, "missing data")
        else:
            dates_v.append(date_v)
            highs_v.append(high_v)
            lows_v.append(low_v)

filename_s = "sitka_weather_2014.csv"
with open(filename_s) as s:
    reader_s = csv.reader(s)
    header_row_s = next(reader_s)

    dates_s, highs_s, lows_s = [], [], []
    for row_s in reader_s:
        try:
            date_s = datetime.strptime(row_s[0], "%Y-%m-%d")
            high_s = int(row_s[1])
            low_s = int(row_s[3])
        except ValueError:
            print(date_s,"missing data")
        else:
            dates_s.append(date_s)
            highs_s.append(high_s)
            lows_s.append(low_s)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates_v, highs_v, c='red', alpha=0.5)
plt.plot(dates_v, lows_v, c='blue', alpha=0.5)
plt.fill_between(dates_v, highs_v, lows_v, facecolor='blue', alpha=0.1)

plt.plot(dates_s, highs_s, c='yellow', alpha=0.5)
plt.plot(dates_s, lows_s, c='black', alpha=0.5)
plt.fill_between(dates_s, highs_s, lows_s, facecolor='blue', alpha=0.1)

# 设置图表格式
plt.title("Daily high and low temperatures - 2014\nDeath Valley,CA and Sitka",
          fontsize=25)
plt.xlabel('', fontsize=15)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=15)
plt.yticks([20,30,40,50,60,70,80,90,100])
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()

#16.5 涵盖所有国家
from pygal_maps_world.i18n import COUNTRIES

def get_country_code(name):
    """根据指定的国家，返回Pygal使用的两个字母的国别码"""
    for code,country_name in COUNTRIES.items():
        if country_name == name:
            return code
        elif country_name == 'Bolivia':
            return 'bo'
        elif country_name == 'Congo, Dem. Rep.':
            return 'cd'
        elif country_name == 'Congo, Rep.':
            return 'cg'
        elif country_name == 'Dominica':
            return 'do'
        elif country_name == 'Egypt, Arab Rep.':
            return 'eg'
        elif country_name == 'Gambia, The':
            return 'gm'
        elif country_name == 'Hong Kong SAR, China':
            return 'hk'
        elif country_name == 'Iran, Islamic Rep.':
            return 'ir'
        elif country_name == 'Korea, Dem. Rep.':
            return 'kp'
        elif country_name == 'Korea, Rep.':
            return 'kr'
        elif country_name == 'Kyrgyz Republic':
            return 'kg'
        elif country_name == 'Lao PDR':
            return 'la'
        elif country_name == 'Libya':
            return 'ly'
        elif country_name == 'Macao SAR, China':
            return 'mo'
        elif country_name == 'Macedonia, FYR':
            return 'mk'
        elif country_name == 'Moldova':
            return 'md'
        elif country_name == 'Slovak Republic':
            return 'sk'
        elif country_name == 'Tanzania':
            return 'tz'
        elif country_name == 'Venezuela, RB':
            return 've'
        elif country_name == 'Vietnam':
            return 'vn'
        elif country_name == 'Yemen, Rep.':
            return 'ye'
        # 未找到则返回None
        return None

#16.8 测试模块country_codes

import unittest
from country_codes import get_country_code

class TeatCountryCodes(unittest.TestCase):
    """针对country_codes.py的测试"""

    def test_get_country_code(self):
        """能否正确地返回两位国别码"""
        code = get_country_code("Andorra")
        self.assertEqual(code,"ad")

unittest.main()