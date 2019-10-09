#!/usr/bin/python
# -*- coding:utf8 -*-

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
