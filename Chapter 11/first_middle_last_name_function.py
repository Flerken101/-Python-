#!/usr/bin/python
# -*- coding:utf8 -*-

def get_formatted_name(first,middle,last):
    """返回完整的姓名"""
    full_name = first + " " + middle + " " + last
    return full_name.title()