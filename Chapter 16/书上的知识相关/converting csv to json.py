#!/usr/bin/python
# -*- coding:utf8 -*-

import csv
import json

csvfile = open("population_csv.csv","r")
jsonfile = open("population_json.json","w")

fieldnames = ("Country Name","Country Code",'Year',"Value")
reader = csv.DictReader(csvfile,fieldnames)
for row in reader:
    json.dump(row,jsonfile)
    jsonfile.write(",\n")

#最后还要将第一个由表头形成的字典删除，并在整体字典前后加上[]
#json的格式是：整体是一个列表，里面的元素都是字典，
# 最后一行的代码就是为了让每一元素都成为一个字典，一定要记得加逗号