#!/usr/bin/python
# -*- coding:utf8 -*-

def get_formatted_name(first,last,middle=""):
    """返回完整的姓名"""
    if middle:
        full_name = first + " " + middle + " " + last
    else:
        full_name = first + " " + last

    return full_name.title()
