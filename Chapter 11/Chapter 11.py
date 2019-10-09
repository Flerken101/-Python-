#!/usr/bin/python
# -*- coding:utf8 -*-

#11.1测试函数
#先定义一个接受名和姓并返回整洁姓的函数
def get_formatted_name(first,last):
    """返回完整的姓名"""
    full_name = first + " "  + last
    return full_name.title()

#再编写一个使用这个函数的程序
from name_founction import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == "q":
        break
    last = input("Please give me a last name: ")
    if last == "q":
        break

    formatted_name = get_formatted_name(first,last)
    print("\tNeatly formatted name: " + formatted_name + ".")

#11.1.1单元测试和测试用例
#11.1.2可通过的测试
#检查函数get_formatted_name()在给定名和姓是能否正确的工作

import unittest
from name_founction import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试函数get_formatted_name()"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name("janis","joplin")
        self.assertEqual(formatted_name,"Janis Joplin")


unittest.main()

#11.1.3不能通过的测试
#用刚才一样的测试去测试first_middle_last_name_function.py

import unittest
from first_middle_last_name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """测试new_name_function.py"""

    def test_get_first_last_name(self):
        """能够正确处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name("janis", "joplin")
        self.assertEqual(formatted_name, "Janis Joplin")


unittest.main()

#11.1.4测试未通过时怎么办

#不应修改测试，而应该修复导致测试不能通过的代码

#将first_middle_last_name_function.py修改后的函数存入new_name_function.py中

import unittest
from new_name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """测试new_name_function.py"""

    def test_get_first_middle_last_name(self):
        """测试是否能正确处理像Janis Joplin这样的姓名"""
        full_name = get_formatted_name("janis", "joplin")
        self.assertEqual(full_name,"Janis Joplin")

unittest.main()

#11.1.5添加新测试

#在类NameTestCase中添加一个新方法用于测试中间名
#要注意在new_name_function.py中get_formatted_name()函数的参数位置有变化

import unittest
from new_name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """测试new_name_function.py"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        full_name = get_formatted_name("janis", "joplin")
        self.assertEqual(full_name, "Janis Joplin")

    def test_first_middle_last_name(self):
        """能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗"""
        formatted_name = get_formatted_name("wolfgang",  "mozart","amadeus")
        self.assertEqual(formatted_name, "Wolfgang Amadeus Mozart")


unittest.main()

#11.2测试类
#11.2.1各种断言的方法
#11.2.2 一个要测试的类

#创建一个帮助管理匿名调查的类

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
        print("Survey results: ")
        for response in self.responses:
            print("\tresponse")


#再编写一个使用他的程序

from survey import AnonymousSurvey

# 定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "What language did you first learn speak? "
my_survey = AnonymousSurvey(question)
print("Enter 'q' to quit:")

# 显示并存储答案
my_survey.show_question()

# 加一个循环,收集多份答案并存储
print("\n")
while True:
    response = input("Response:")
    if response == "q":
        break
    my_survey.store_response(response)

# 展示调查结果
my_survey.show_result()

#11.2.3 测试 AnonymousSurvey类
#先测试该类行为的一个方面:当用户面对问题只提供了同一个答案时，这个答案也能被妥善存储
import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """测试survey.py"""

    def test_single_response(self):
        """测试类AnonymousSurvey能否正确地处理单个答案"""
        question = "What language did you first learn speak? "
        my_survey = AnonymousSurvey(question)
        response = "Chinese"
        my_survey.store_response(response)

        self.assertIn("Chinese",my_survey.responses)


unittest.main()


#增加一个测试，测试当用户提供三个答案时，也将被妥善地处理

import unittest
from survey import AnonymousSurvey


class SurveyTestCase(unittest.TestCase):
    """测试survey.py"""

    def test_single_response(self):
        """测试当用户提供单个答案时能否被妥善存储"""
        question = "What language did you first learn speak? "
        my_survey = AnonymousSurvey(question)
        response = "Chinese"
        my_survey.store_response(response)

        self.assertIn("Chinese", my_survey.responses)

    def test_three_responses(self):
        """测试当用户提供三个答案时能否被妥善存储"""
        question = "What language did you first learn speak? "
        my_survey = AnonymousSurvey(question)
        my_responses = ['Chinese', "English", "Spanish"]
        for my_response in my_responses:
            my_survey.store_response(my_response)
            self.assertIn(my_response, my_survey.responses)


unittest.main()

#11.2.4 方法Setup

#使用SetUp()来创建一个调查对象和一组答案，共其他两个单元测试使用
import unittest
from survey import AnonymousSurvey


class SurveyAnonymousSurvey(unittest.TestCase):
    """测试survey.py"""

    def setUp(self):
        """创建一个调查问题和一组答案，供使用的单元测试使用"""

        question = "What language did you first learn speak? "
        # 将实例与答案列表都储存在属性中，以便他们可以在这个类的任何地方使用
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Chinese', "English", "Spanish"]

    def test_single_response(self):
        """测试当被调查对象提供单个答案时，是否能被妥善处理"""
        response = self.responses[0]
        self.my_survey.store_response(response)
        self.assertIn(response, self.my_survey.responses)

    def test_three_responses(self):
        """测试当被调查对象提供三个答案时，能否被妥善存储"""
        for response in self.responses:
            self.my_survey.store_response(response)
            self.assertIn(response, self.my_survey.responses)


unittest.main()
