#!/usr/bin/python
# -*- coding:utf8 -*-

class Employee():
    """一次描述雇员信息的简单尝试"""

    def __init__(self,first_name,last_name):
        """初始化描述雇员信息的属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = 1000000

    def give_raise(self,a=0):
        """将年薪增加特定的值，否则默认增加$5000"""
        if a != 0:
            self.salary += a
        else:
            self.salary += 5000
        return self.salary