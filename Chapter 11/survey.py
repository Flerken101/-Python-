#!/usr/bin/python
# -*- coding:utf8 -*-

class AnonymousSurvey():
    """手机匿名调查的问卷"""

    def __init__(self,question):
        """存储一个问题，并为存储答案做准备"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_response(self,new_response):
        """储存单份调查问卷"""
        self.responses.append(new_response)

    def show_result(self):
        """"显示收集到的所有答案"""
        print("\nSurvey results: ")
        for response in self.responses:
            print("\t" + response)