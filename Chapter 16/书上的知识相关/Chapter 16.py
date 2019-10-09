#!/usr/bin/python
# -*- coding:utf8 -*-

#16.1 CSV文件格式
#16.1.1分析CSV文件头

import csv

filename = "sitka_weather_07-2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

#16.1.2打印文件头及其位置
import csv

filename = "sitka_weather_07-2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

for index,column_header in enumerate(header_row):
    print(index,column_header)

#16.1.3 提取并读取数据（读取每天的最高气温）

import csv

filename = "sitka_weather_07-2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    for row in reader:
        highs.append(row[1])

    print(highs)

#将字符串转化为整数
import csv
filename = "sitka_weather_07-2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)

    print(highs)

#16.1.4 绘制气温图表

import csv
import matplotlib.pyplot as plt

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)

# 根据数据绘制图形
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(highs, c='red')

# 设置图形格式
plt.title("Daily high temperatures,July 2014", fontsize=24)
plt.xlabel("", fontsize=16)
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis="both", which='major', labelsize=10)

plt.show()

#16.1.5 模块datetime
from datetime import datetime
first_date = datetime.strptime('2014-7-1','%Y-%m-%d')
print(first_date)
print(type(first_date))

#16.1.6 在图表中添加日期
import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "sitka_weather_07-2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates,highs = [],[]
    for row in reader:
        current_date = datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)

#根据数据绘制图形
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red')

#设置图形的格式
plt.title("Daily high temperatures,July 2014",fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)',fontsize=16)
plt.tick_params(axis="both",which='major',labelsize=10)

plt.show()

#16.1.7 涵盖更长的时间

import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "sitka_weather_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #从文件中获取日期、最高气温
    datetimes,highs = [],[]
    for row in reader:
        current_date = datetime.strptime(row[0],"%Y-%m-%d")
        datetimes.append(current_date)

        high = int(row[1])
        highs.append(high)

#根据数据绘制图形
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(datetimes,highs,linewidth=1)

#设置图表格式
plt.title("Daily high temperatures - 2014",fontsize=24)
plt.xlabel("",fontsize=14)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)",fontsize=14)
plt.tick_params(axis="both",which='major',labelsize=10)

plt.show()

#16.1.8 再绘制一个数据系列
import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "sitka_weather_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #从文件中提取日期，最高温度和最低温度
    dates,highs,lows = [],[],[]
    for row in reader:
        current_date = datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)

#根据数据绘制图形
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,linewidth=1)
plt.plot(dates,lows,linewidth=1)

#设置图表格式
plt.title("Daliy high and low temperatures - 2014",fontsize=24)
plt.xlabel("",fontsize=15)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)",fontsize=15)
plt.tick_params(axis='both',which='major',labelsize=10)

plt.show()

#16.1.9 给图表区域着色

import csv
import matplotlib.pyplot as plt
from datetime import datetime

# 从数据文件中提取日期，最高气温与最低气温
dates, highs, lows = [], [], []
filename = "sitka_weather_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图表格式
plt.title("Daliy high and low temperatures - 2014", fontsize=15)
plt.xlabel("", fontsize=15)
fig.autofmt_xdate()
plt.ylabel("Temperatures(F)", fontsize=15)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()

"""函数next()的参数是迭代器（iterator）和一个default ，即next(iterator, default) ，
default是迭代器已经到了最末端，再调用next()函数的输出值。不填这个参数的话，
到了最末端还用next()的话会报错。因此在python编程：从入门到实践里面的代码输入的
是scv文件的迭代器，其指向文件的第一行，用了next之后，此迭代器指向文件的第二行，进行读取。"""

#16.1.10 错误检查
"""用16.1.9的程序生成吉利福尼亚死亡谷的气温图时，会发生值错误，因为该文件中没有记录
2014年2月16日的数据，Python无法将空字符串转换为整数。"""


#添加异常处理程序

import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "death_valley_2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(date, "missing data")
        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图表格式
plt.title("Daily high and low temperatures - 2014\nDeath Valley,CA",
          fontsize=25)
plt.xlabel('', fontsize=15)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=15)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()

#16.2 制作世界人口地图：JSON格式

#16.2.1 下载世界人口数据

#16.2.2提取相关的数据
import json

#将数据加载到内存中
filename = "population_json.json"
with open(filename) as f:
    pop_data = json.load(f)

#打印每个国家2016年的人口数量
for pop_dict in pop_data:
    if pop_dict['Year'] == '2016':
        country_name = pop_dict["Country Name"]
        population = pop_dict['Value']
        print(country_name + "："+ population)


#16.2.3 将字符串转换为数字值
import json

#将文件加载到内存中
filename = "population_json.json"
with open(filename) as f:
    pop_data = json.load(f)

#打印每个国家2016年的人口数量
for pop_dict in pop_data:
    if pop_dict['Year'] == "2016":
        country_name = pop_dict["Country Name"]
        population = int(float(pop_dict['Value']))
        print(country_name + ":" + str(population))

#16.2.4 获取两个字母的国别码
from pygal_maps_world.i18n import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code,COUNTRIES[country_code])

#编写获取国别码的函数
from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """根据指定的国家，返回Pygal使用的两个字母的国别码"""
    for code,name in COUNTRIES.items():
        if name == country_name:
            return code
        #如果没有找到指定的国家，就返回None
        return None

    print(get_country_code('Andorra'))
    print(get_country_code('United Arab Emirates'))

#导入函数
import json
from country_codes import get_country_code

#将数据加载到一个列表中
filename = 'population_json.json'
with open(filename) as f:
    pop_data = json.load(f)

#打印每个国家2010年的人口数量
for pop_dict in pop_data:
    if pop_dict['Year'] == '2016':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            print(code + ":" + str(population))
        else:
            print("ERROR - " + country_name)

#16.2.5 制作世界地图

import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()
wm.title = "North,Central,and South America"

wm.add('North America',['ca','mx','us'])
wm.add("Central America",['bz','cr','gt','hn','ni','pa','sv'])
wm.add("South America",['ar','bo','br','cl','co','ec','gf','gy','pe','py',
                        'sr','uy','ve'])

wm.render_to_file('americas.svg')


#16.2.6 在世界地图上呈现数字数据
import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()
wm.title = 'Populations of Countries in North America'
wm.add('North America',{'ca':341260000,'us':309349000,'mx':113423000})

wm.render_to_file('na_populations.svg')

#16.2.7 绘制完整的世界人口地图
import json
import pygal_maps_world.maps
from country_codes import get_country_code

#将数据加载到列表中
filename = 'population_json.json'
with open(filename) as f:
    pop_data = json.load(f)

#打印每个国家2016年的人口数量
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2016':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict["Value"]))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

wm = pygal_maps_world.maps.World()
wm.title = 'World Population in 2016,by country'
wm.add('2016',cc_populations)

wm.render_to_file('world_population.svg')


#16.2.8 根据人口数量将国家分组
import json
from country_codes import get_country_code
import pygal_maps_world.maps

#将数据读取到内存中
filename = "population_json.json"
with open(filename) as f:
    pop_data = json.load(f)

#创建一个包含人口数量的字典
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2016':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        country_code = get_country_code(country_name)
        if country_code:
            cc_populations[country_code] = population

#根据人口数量将所有的国家分成三组
cc_pops_1,cc_pops_2,cc_pops_3 = {},{},{}
for cc,pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 10000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

#看看每组分别包含多少个国家
print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))

wm = pygal_maps_world.maps.World()
wm.title = 'World Population in 2010,by Country'
wm.add('0-10m',cc_pops_1)
wm.add('10m-1bn',cc_pops_2)
wm.add('>1bn',cc_pops_3)

wm.render_to_file('world_population.svg')

#16.2..9 使用pygal设置世界地图的样式
import json
import pygal_maps_world.maps
from country_codes import get_country_code
from pygal.style import RotateStyle

#将数据加载到列表中
filename = "population_json.json"
with open(filename) as f:
    pop_data = json.load(f)

#创建一个包含人口数量的字典
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        country_code = get_country_code(country_name)
        if country_code:
            cc_populations[country_code] = population

#根据人口数量将国家分组
cc_pops_1,cc_pops_2,cc_pops_3 = {},{},{}
for cc,pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

#看看每组分别包含多少个国家
print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))

wm_style = RotateStyle('#336699')
wm = pygal_maps_world.maps.World(style=wm_style)
wm.title = "World Population in 2010,by country"
wm.add('0-10m',cc_pops_1)
wm.add('10m-1bn',cc_pops_2)
wm.add(">1bn",cc_pops_3)

wm.render_to_file("World Population in 2010,by country")

#16.2.10 加亮颜色主题
import json
from country_codes import get_country_code
import pygal_maps_world.maps
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

# 加载数据
filename = "population_json.json"
with open(filename) as f:
    pop_data = json.load(f)

# 创建一个包含人口数量的字典
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict["Country Name"]
        population = int(float(pop_dict['Value']))
        country_code = get_country_code(country_name)
        if country_code:
            cc_populations[country_code] = population

# 根据人口数量将所有国家分组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# 设置世界地图样式
wm_style = RS('#336699', base_style=LCS)
wm = pygal_maps_world.maps.World(style=wm_style)
wm.title = "World Population in 2010,by country"
wm.add("0-10m", cc_pops_1)
wm.add("10m-1bn", cc_pops_2)
wm.add(">1bn", cc_pops_3)

wm.render_to_file("world_population.svg")

