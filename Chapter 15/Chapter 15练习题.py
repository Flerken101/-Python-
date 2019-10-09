#!/usr/bin/python
# -*- coding:utf8 -*-

"""15-1 立方：数字的三次方被称为其立方。请绘制一个图形，显示前5个整数的立方值。
再绘制一个图形，显示前面5000个整数的立方值。"""
#前5个整数的立方值
import matplotlib.pyplot as plt

input_value = [1,2,3,4,5]
cubes = [1,8,27,64,125]
plt.plot(input_value,cubes ,linewidth=3,color=(0,0,0.8))

#设置图表标题并给坐标轴加上标签
plt.title("Cubes  Number",fontsize=20)
plt.xlabel("Value",fontsize=15)
plt.ylabel("Cubes ",fontsize=15)

#设置刻度标记的大小
plt.tick_params(axis="both",which="major",labelsize=15)

plt.show()

#前面5000个整数的立方值
import matplotlib.pyplot as plt

input_values = list(range(1,5001))
cubes = [input_value**3 for input_value in input_values]

plt.plot(input_values,cubes ,linewidth=3,color=(0,0,0.8))

#设置图表标题并给坐标轴加上标签
plt.title("Cubes  Number",fontsize=20)
plt.xlabel("Value",fontsize=15)
plt.ylabel("Cubes ",fontsize=15)

#设置刻度标记的大小
plt.tick_params(axis="both",which="major",labelsize=15)

plt.show()


#15-2 彩色立方：给你前面绘制的立方图指定颜色映射

##前5个整数的立方值颜色映射
import matplotlib.pyplot as plt

x_values = [1,2,3,4,5]
y_values = [x_value**3 for x_value in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,
            edgecolors="none",s=15)

#设置图表标题及给坐标轴加上标签
plt.title("Cubes Number",fontsize=24)
plt.xlabel("Value",fontsize=20)
plt.ylabel('Cube of value',fontsize=20)

#设置刻度标记大小
plt.tick_params(axis="both",which="major",labelsize=10)

plt.show()

#前面5000个整数的立方值颜色映射

import matplotlib.pyplot as plt

x_values = list(range(1,5001))
y_values = [x_value**3 for x_value in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,
            edgecolors="none",s=15)

#设置图表标题及给坐标轴加上标签
plt.title("Cubes Number",fontsize=24)
plt.xlabel("Value",fontsize=20)
plt.ylabel('Cube of value',fontsize=20)

#设置刻度标记大小
plt.tick_params(axis="both",which="major",labelsize=10)

#设置坐标轴的取值范围
plt.axis([0,5000,0,125000000000])

plt.show()

'''15-3 分子运动：修改rw_visual.py，将其中的plt.scatter()替换为plt.plot()，
为模拟花粉在水滴表面的运动路径，向plt.plot()传递rw.x_values和rw.y_values，
并指定实参值linewidth。使用5000个点而不是50000个点。'''
import matplotlib.pyplot as plt
from random_walk import Randomwalk

#创建一个随机漫步实例
rw = Randomwalk(5000)

rw.fill_walk()
plt.figure(dpi=128,figsize=(10,6))
plt.plot(rw.x_values,rw.y_values,linewidth=1)

#设置图表标题
plt.title("Random Walk",fontsize=10)

#隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()

"""15-4 改进的随机漫步：在类RandomWalk中，x_step 和 y_step 是根据相同的条件生成的：
从列表【1，-1】中随机地选择方向，并经列表【0,1,2,3,4】中随机地选择距离。
请修改这些列表中的值，看看对随机漫步路径有何影响。尝试使用更长距离选择列表，
如0~8；或者将-1从x或y方向列表中删除"""

"""如果将-1均从x，方向列表中删除，则随机漫步几乎呈现为一条直线。
若从x或y的一个列表中删除，
则会只会在x轴或者y轴的正方向做随机漫步。"""

"""15-5 重构：方法fill_walk()很长。请新建一个名为get_step()的方法，
用于确定每次漫步的距离和方向，并计算这次漫步将如何移动。然后，在fill_work()中调用get_step()两次：
x_step = self.get_step()
y_step = self.get_step()
通过这样的重构，可缩小fill_walk() 的规模，让这个方法阅读和理解起来更容易"""

from random import choice

class Randomwalk():
    """一个生成随机漫步数据的类"""

    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有随机漫步都始于（0,0）
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """确定每次漫步的方向和距离"""

        # 决定前进方向以及沿这个方向前进的距离
        x_direction = choice([1, -1])
        x_distance = choice(list(range(1, 5)))
        x_step = x_direction * x_distance
        return x_step

        y_direction = choice([-1,1])
        y_distance = choice(list(range(1, 5)))
        y_step = y_direction * y_distance
        return y_step

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

"""15-6 自动生成标签：请修改die.py 和 dice_visual.py，将用来设置 hist.x_labels 值
的列表替换为字节自动生成这种列表的循环。如果你熟悉列表解析，可尝试将
 die_visual.py 和 dice_visual.py 中的其他 for 循环也替换为列表解析。"""

#已实现

"""15-7 两个D8骰子：请模拟同时透支两个8面骰子1000次的结果"""

import pygal
from die import Die

# 创建两个D6骰子
die_1 = Die(8)
die_2 = Die(8)

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

"""15-8 同时掷三个骰子:如果你同时掷三个D6骰子，可能得到的最小点数为3，而最大点数为18,
请通过可视化展示同时掷三个D6骰子的结果"""
import pygal
from die import Die

# 创建三个D6实例
die_1 = Die()
die_2 = Die()
die_3 = Die()

# 掷骰子多次，并将结果储存在一个列表中
results = []
for roll_num in range(5000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 将数据结果可视化
bar = pygal.Bar()

bar.title = "Results of rolling three D6 dice 5000 times."

bar.x_labels = []
for num in range(3, max_result + 1):
    x_label = str(num)
    bar.x_labels.append(x_label)

bar.x_title = "Result"
bar.y_title = "Frequency of Result"


bar.add("3 * D6", frequencies)
bar.render_to_file("three_D6_dice_visual.svg")

"""15-9 将点数相乘：同时掷两个骰子时，通常将它们的点数相加。
请通过可视化展示将两个骰子的点数相乘的结果。"""


import pygal
from die import Die

# 创建两个D6骰子
die_1 = Die(8)
die_2 = Die(8)

# 模拟掷两个骰子1000次，并把每次点数之和存储到一个列表中
results = []
for roll_num in range(1000):
    result_1 = die_1.roll()
    result_2 = die_2.roll()
    result = result_1 *  result_2
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
bar = pygal.Bar()

bar.title = "Result of rolling two D6 dice 1000 times."

bar.x_labels = []
for num in range(1, max_result +1):
    x_label = str(num)
    bar.x_labels.append(x_label)

bar.x_title = "Result"
bar.y_title = "Frequency of Result"

bar.add("D8 + D8", frequencies)
bar.render_to_file("dice_multiplication_visual.svg")

"""15-10练习使用本章介绍的两个库：尝试使用matplotlib通过可视化来模拟掷骰子的情况，
并尝试使用Pygal通过可视化来模拟随机漫步的情况。 """

#使用matplotlib通过可视化来模拟掷骰子（没理解对题意，题目的意思还是让你用柱状图，
# 见下面一位博主的答案。）

import matplotlib.pyplot as plt
from die import Die

# 创建D6骰子实例
die = Die()

# 模拟掷骰子100次，并将结果储存在一个列表中
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, 7):
    frequency = results.count(value)
    frequencies.append(frequency)

# 将数据结果可视化
x_values = list(range(1, 7))
plt.plot(x_values, frequencies, linewidth=5)

# 设置图表标题，并给坐标轴加上标签
plt.title("Results of rolling one D6 100 times", fontsize=24)
plt.xlabel("Result", fontsize=14)
plt.ylabel("Frequency", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis="both", which="major", labelsize=14)

plt.show()

#正确 使用matplotlib通过可视化来模拟掷骰子

from die import Die
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(50000):
    # result = die_1.roll()
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
# max_results = die_1.num_sides
max_results = die_1.num_sides + die_2.num_sides
X_Range = list(set(results))
for value in X_Range:
    frequency = results.count(value)
    frequencies.append(frequency)

plt.bar(X_Range, frequencies, color='Pink', align='center', label='D6+D6')
plt.xticks(X_Range)

plt.xlabel("Results", fontsize=8)
plt.ylabel("Frequencies", fontsize=8)

# 图例
pink_patch = mpatches.Patch(color='Pink', label='D6+D6')
plt.legend(handles=[pink_patch])

plt.show()

#使用Pygal通过可视化来模拟随机漫步的情况
import pygal
from random_walk import Randomwalk

rw = Randomwalk(1000)
rw.fill_walk()

xy_chart = pygal.XY(stroke=False)
xy_chart.title = "RandomWalk"
pygal.Line(include_x_axis=False, include_y_axis=False)

xy_list = []
for (x, y) in zip(rw.x_values, rw.y_values):
    xy_list.append((x, y))

xy_chart.add("data", xy_list)
xy_chart.render_to_file("RandomWalk.svg")

