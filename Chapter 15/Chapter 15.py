#!/usr/bin/python
# -*- coding:utf8 -*-

import matplotlib

#15.1安装matplotlib
#  已经安装成功

#15.2绘制简单的折线图（平方数序列）
import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
plt.plot(squares)
plt.show()

#15.2.1修改标签文字和线条粗细

import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
plt.plot(squares,linewidth=5)

#设置图表标题，并给坐标轴加上标签
plt.title("Square Number",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis="both",labelsize=24)

plt.show()

#15.2.2矫正图形

import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_values,squares,linewidth=5)

#设置图表标题并给坐标轴加上标签
plt.title("Square Number",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel('Square of value',fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis="both",labelsize=14)

plt.show()

#15.2.3使用scatter()绘制散点图并设置其样式

#绘制单个点
import matplotlib.pyplot as plt

plt.scatter(2,4)
plt.show()

#设置单个点的输出样式
import matplotlib.pyplot as plt

plt.scatter(2,4,s=200)

#设置图表标题并给坐标轴加上标签
plt.title("Square Number",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis="both",which='major',labelsize=10)

plt.show()

#15.2.4使用scatter()绘制一些列点

import matplotlib.pyplot as plt

x_value = [1,2,3,4,5]
y_value = [1,4,9,16,25]

plt.scatter(x_value,y_value,s=100)

#设置图表标题和轴标签
plt.title("Square Number",fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis="both",which="major",labelsize=10)

plt.show()

#15.2.5自动计算数据

import matplotlib.pyplot as plt

x_value = list(range(1,1001))
y_value = [x**2 for x in x_value]

plt.scatter(x_value,y_value,s=40)

#设置图表标题并给坐标轴加上标签
plt.title("Square Number",fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis="both",which="major",labelsize=10)

#设置每个坐标轴的取值范围
plt.axis([0,1000,0,1100000])

plt.show()


#15.2.6 删除数据点的轮廓

import matplotlib.pyplot as plt

x_value = list(range(1,1001))
y_value = [x**2 for x in x_value]

plt.scatter(x_value,y_value,edgecolors="none",s=40)

#设置图表的标题及坐标轴标签
plt.title("Square Number",fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis="both",which="major0",labelsize=10)

#设置每个坐标轴的取值范围
plt.axis([0,1000,0,1100000])

plt.show()

#15.2.7 自定义颜色

#方法一：传递参数，直接指定
import matplotlib.pyplot as plt

x_value = list(range(1,1001))
y_value = [x**2 for x in x_value]

plt.scatter(x_value,y_value,color="red",edgecolors="none",s=40)

#设置图表的标题及坐标轴标签
plt.title("Square Number",fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis="both",which="major0",labelsize=10)

#设置每个坐标轴的取值范围
plt.axis([0,1000,0,1100000])

plt.show()

#方法二：使用RGB颜色模式
import matplotlib.pyplot as plt

x_value = list(range(1,1001))
y_value = [x**2 for x in x_value]

plt.scatter(x_value,y_value,c=(0.9,0.5,0.2),edgecolors="none",s=40)

#设置图表的标题并给坐标轴加上标签
plt.title("Square Number",fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis="both",which='major',labelsize=10)

#设置坐标轴的取值范围
plt.axis([0,1000,0,1100000])

plt.show()

#15.2.8 使用颜色映射

import matplotlib.pyplot as plt

x_value = list(range(1,1001))
y_value = [x**2 for x in x_value]

plt.scatter(x_value,y_value,c=y_value,cmap=plt.cm.Blues,edgecolors="none",s=40)

#设置图表的标题并给坐标轴加上标签
plt.title("Square Number",fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis="both",which='major',labelsize=10)

#设置坐标轴的取值范围
plt.axis([0,1000,0,1100000])

plt.show()

#15.2.9 自动保存图表

import matplotlib.pyplot as plt

x_value = list(range(1,1001))
y_value = [x**2 for x in x_value]

plt.scatter(x_value,y_value,c=y_value,cmap=plt.cm.Blues,edgecolors="none",s=40)

#设置图表的标题并给坐标轴加上标签
plt.title("Square Number",fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis="both",which='major',labelsize=10)

#设置坐标轴的取值范围
plt.axis([0,1000,0,1100000])

plt.savefig("squares_plot.png",bbox_inches="tight")

#15.3 随机漫步
#每次行走都是完全随机的，没有明确的方向，结果是由一系列随机决策决定的

# 15.3.2 选择方向（构造fill_walk()函数）
#15.3.1 创建Randomwalk()类
#15.3.2 选择方向

# 15.3.3绘制随机漫步图
import matplotlib.pyplot as plt

from random_walk import Randomwalk

#创建一个Randomwalk实例，并将其包含的点都绘制出来
rw = Randomwalk()
rw.fill_walk()
plt.scatter(rw.x_values,rw.y_values,edgecolors="none",s=15)
plt.show()

#15.3.4 模拟多次随机漫步
import matplotlib.pyplot as plt
from random_walk import Randomwalk

while True:
    rw = Randomwalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values,edgecolor="none",s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n) ")
    if keep_running == "n":
        break

#15.3.5 设置随机漫步图的样式
#15.3.6给点着色

import matplotlib.pyplot as plt
from random_walk import Randomwalk

#只要程序处于活动状态，就不断地模拟随机逐步
while  True：
    rw = Randomwalk()
    rw.fill_walk()
    points_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=points_numbers,cmap=plt.cm.Blues,
                edgecolors="none",s=10)
    plt.show()

    keep_running = input("Make another walk? (y/n) ")
    if keep_running == "n":
        break

#15.3.7重新绘制起点和终点
import  matplotlib.pyplot as plt
from random_walk import  Randomwalk

while True:
    rw = Randomwalk()
    rw.fill_walk()
    points_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=points_numbers,
                cmap=plt.cm.Blues,edgecolors="none",s=10)

    #突出起点和终点
    plt.scatter(0,0,c="red",s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c="green",edgecolors="none",
                s=100)
    plt.show()

    keep_running =input("Make another walk? (y/n) ")
    if keep_running == "n"
        break

#15.3.8隐藏坐标轴
    import matplotlib.pyplot as plt
    from random_walk import Randomwalk

    while True:
        rw = Randomwalk()
        rw.fill_walk()
        points_numbers = list(range(rw.num_points))
        plt.scatter(rw.x_values, rw.y_values, c=points_numbers,
                    cmap=plt.cm.Blues, edgecolors="none", s=10)

        # 突出起点和终点
        plt.scatter(0, 0, c="red", s=100)
        plt.scatter(rw.x_values[-1], rw.y_values[-1], c="green",
                    edgecolors="none",
                    s=100)

        # 隐藏坐标轴
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)

        plt.show()

        keep_running = input("Make another walk? (y/n) ")
        if keep_running == "n":
            break

#15.3.9增加点数
import matplotlib.pyplot as plt
from random_walk import Randomwalk

while True:
    rw = Randomwalk(50000)
    rw.fill_walk()
    points_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=points_numbers,
                cmap=plt.cm.Blues, edgecolors="none", s=1)

    # 突出起点和终点
    plt.scatter(0, 0, c="red", s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c="green",
                edgecolors="none",
                s=50)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n) ")
    if keep_running == "n":
        break

#15.3.10 调整尺寸以适合屏幕

import matplotlib.pyplot as plt
from random_walk import Randomwalk

while True:
    rw = Randomwalk(50000)
    rw.fill_walk()
    plt.figure(dpi=128,figsize=(7,3))

    points_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=points_numbers,
                cmap=plt.cm.Blues, edgecolors="none", s=1)

    # 突出起点和终点
    plt.scatter(0, 0, c="red", s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c="green",
                edgecolors="none",
                s=50)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.savefig("Random_walk.png",bbox_inches='tight')

    plt.show()

    keep_running = input("Make another walk? (y/n) ")
    if keep_running == "n":
        break

#15.4 使用Pygal模拟掷骰子
#15.4.1 安装Pygal
#15.4.2 Pygal画廊
#15.4.3创建Die类

from random import randint

class Die():
    """表示一个骰子的类"""

    def __init__(self,num_sides=6):
        """骰子默认为6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面数之间的随机数"""
         return randint(1,self.num_sides)

#15.4.4 掷骰子
from die import Die

#创建一个D6
die = Die()

#掷几次骰子，并将结果出存在一个列表中
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)


#15.4.5分析结果（统计每个点数出现的频数）

from die import Die

#创建一个D6
die = Die()

#掷1000次骰子，并将结果储存在列表中
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#分析结果
frequencies = []

for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

#15.4.6绘制柱状图
import pygal
from die import Die

#创建一个D6实例
die = Die()

#模拟掷1000次骰子，并把结果储存在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#分析结果
frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#对结果进行可视化
bar = pygal.Bar()

bar.title="Result of rolling one D6 1000 times."
bar.x_labels = ["1","2","3","4","5","6"]
bar.x_title = "Result"
bar.y_title = "Frequency of Result"

bar.add("D6",frequencies)
bar.render_to_file("die_visual.svg")

#15.4.7 同时掷两个骰子
import pygal
from die import Die

# 创建两个D6骰子
die_1 = Die()
die_2 = Die()

# 模拟掷两个骰子1000次，并把每次点数之和存储到一个列表中
results = []
for roll_num in range(1000):
    result_1 = die_1.roll()
    result_2 = die_2.roll()
    result = result_1 + result_2
    results.append(result)

# 分析结果
frequencies = []
for value in range(2, die_1.num_sides + die_2.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
bar = pygal.Bar()

bar.title = "Result of rolling two D6 dice 1000 times."

bar.x_labels = []
for num in range(2, die_1.num_sides + die_2.num_sides +1):
    x_label = str(num)
    bar.x_labels.append(x_label)

bar.x_title = "Result"
bar.y_title = "Frequency of Result"

bar.add("D6 + D6", frequencies)
bar.render_to_file("die_visual.svg")

#15.4.8 同时掷两个面数不同的骰子
import pygal
from die import  Die

#创建两个不同面数的骰子实例
die_1 = Die()
die_2 = Die(10)

#模拟掷两个骰子5000次，并把每次的点数之和存储到一个列表中
results =[]
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#将数据结果可视化
bar = pygal.Bar()

bar.title = "Results of rolling a D6 and a D10  50,000 times."

bar.x_labels =[]
for num in range(2,max_result + 1):
    x_label = str(num)
    bar.x_labels.append(x_label)

bar.x_title = "Result"
bar.y_title = "Frequency of Result"

bar.add("D6 + D10",frequencies)
bar.render_to_file("dice_visual.svg")

