#!/usr/bin/python
# -*- coding:utf8 -*-









'''10-13 验证用户：最后一个remember_me.py版本假设用户要么已输入其用户名，
要么是首次运行该程序。我们应修改这个程序，以应对这样的情形： 
当前和最后一次运行该程序的用户并非同一个人。为此，在greet_user()中打印欢迎用户
回来的消息前，先询问他用户名是否是对的。如果不对，就调用get_new_username()让用户输入正确的用户名。'''

import json


def get_stored_username():
    """如果储存了用户名，就获取它"""
    try:
        with open("username.json") as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = input("What's your name? ")
    filename = "username.json"
    with open(filename, "w") as file_object:
        json.dump(username, file_object)
    return username


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Is your username " + username.title() +"? ")
        repeat = input("yes or no? \n")
        if repeat == "yes":
            print("Welcome back," + username + "!")
        else:
            username = get_new_username()
            print("We will remember you when you conme back," + username + "!")
    else:
        username = get_new_username()
        print("We will remember you when you conme back," + username + "!")


greet_user()




























