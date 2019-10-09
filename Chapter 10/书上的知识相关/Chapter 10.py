
#10.1从文件中读取数据
#10.1.1读取整个文件

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

#删除字符串末尾的空白
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

#10.1.2文件路径
#相对文件路径
with open("text_files/pi_digits.txt") as file_object:
    content = file_object.read()
    print(content)

with open("text_files\pi_digits.txt") as file_object:
    content = file_object.read()
    print(content)

#绝对文件路径
with open('D:\Pycharm\other_files\pi_digits.txt') as file_object:
    content = file_object.read()
    print(content)

#将文件路径存储在变量中
file_path = 'D:\Pycharm\other_files\pi_digits.txt'

with open(file_path) as file_object:
    content = file_object.read()
    print(content)

#10.1.3逐行读取（对文件对象使用for循环）
file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    for line in file_object:
        print(line)

#删除文件每行末尾与由print()语句产生的换行符

with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.strip())

#10.1.4 创建一个包含文件各行内容的列表
#不去掉空白
filename = "pi_digits.txt"

with open(filename) as file_object_1:
    lines_1 = file_object_1.readlines()

for line in lines_1:
    print(line)

#去掉尾部空白（因为还没有去掉没行开头的空格，故结果不能转换为浮点数）
filename = "pi_digits.txt"

print('\n')
with open(filename) as file_object_2:
    lines_2 = file_object_2.readlines()

for line in lines_2:
    print(line.rstrip())

#去掉两端空白
filename = "pi_digits.txt"

print('\n')
with open(filename) as file_object_3:
    lines_3 = file_object_3.readlines()

for line in lines_3:
    print(line.strip())

#10.1.5 使用文件内容
#创建一个包含文件中储存的所有数字但没有任何空格的字符串
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

#去掉每行开头的空格
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string =""
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
#转换为浮点数
print(type(float(pi_string)))

#注意：Python在读取文本文件时会将其中所有文本都解读为字符串

#10.1.6 包含一百万位的大型文件（此处只用包含π的前五十位）
filename = 'pi_fifty_digits.txt'

with open(filename) as file_name:
    lines = file_name.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

#10.1.7圆周率值中包含你的生日吗
filename = 'pi_fifty_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

birthday = input('Enter your birthday,in the form mmddyy: ')
if birthday in pi_string:
    print('Your birthday appears in the first fifty digits of pi!')
else:
    print("Your birthday does not appear in the first fifty digits of pi!")


#10.2写入文件
#10.2.1写入空文件
#如果以写入模式打开已存在的文件，Python将在返回文件对象前清空该文件
filename = "programming.txt"

with open(filename,"w") as file_object:
    file_object.write("I love progranmming.")

#10.2.2写入多行
#注意：函数write()不会在你写入的文本末尾添加换行符
filename = 'programming.txt'

with open(filename,"w")  as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

#9.2.3附加到文件
#以附加模式打开已存在的文件时，Python不会在返回文件对象前清空文件
filename = 'programming.txt'

with open(filename,"a") as file_object:
    file_object.write("I also love finding meaning in large databases.\n")
    file_object.write("I love creating apps that can run in a browser.")

#10.3 异常
#10.3.1 处理ZeroDivisionError异常

print(5/0)

#10.3.2 使用try-except代码块
#将可能发生异常的代码块放到try-exceptz代码块中
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

#10.3.3 使用异常避免崩溃
#使用try-except代码块，捕获错误后程序将继续运行，而且还可以避免用户看到你不想让他们看到的内容

print("Give me two numbers,and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst name: ")
    if first_number == 'q':
        break
    secend_number = input("Secent number: ")
    if secend_number == "q":
        break

    answer = int(first_number) / int(secend_number)
    print(answer)

#浮点数计算结果包含的小数位数可能是不确定的
print(0.2+0.1)
print(3*0.1

#10.3.4 else代码块
#try代码块成功执行的代码都应放到else代码块中

print("Give me two number ,and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    secend_number = input("Secend number: ")
    if secend_number == 'q':
        break

    try:
        answer = int(first_number) / int(secend_number)
    except ZeroDivisionError:
        print("You can't divide zero!")
    else:
        print(answer)

#10.3.5 处理FileNotFoundError异常
#文件alice.txt不存在
filename = 'alice.txt'

with open(filename) as f_ob:
    content = f_ob

#使用 try-except代码块
#错误是由函数open()导致的，因此要将try语句放到包含open()的代码行之前
filename = 'alice.txt'

try:
    with open(filename) as f_ob:
        content = f_ob
except FileNotFoundError:
    print('Sorry,the file ' + filename + ' does not exist.')

#10.3.6文本分析
#函数split以空格为分隔符将字符串拆分成多个部分，并将它们储存在一个单词列表中（有些单词可能包含标点符号）
title = "Alice in Wonderland"
print(title.split())


#计算programming.txt码大致包含多少个单词
filename = 'programming.txt'

try:
    with open(filename) as f_ob:
        content = f_ob.read()
except FileNotFoundError:
    print('Sorry, the file ' + filename + " does not exist.")
else:
    #计算文件大致包含多少个单词
    words = content.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")


#计算第九章所有的练习代码大致包含多少个单词
# （当Chapter 9文件的后缀名是.py时,注意open()函数的参数，多了encoding='gb18030',errors='ignore'）

filename = "Chapter 9.py"

try:
    with open(filename,encoding='gb18030',errors='ignore') as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("Sorry, the file "+ filename + " does not exist.")
else:
    words = contents.split()
    words_number = len(words)
    print("The text has " + str(words_number) + " words.")

#计算第九章所有的练习代码大致包含多少个单词（）
# （当Chapter 9文件的后缀名是.txt时,注意open()函数的参数,正常）

filename = "Chapter 9.txt"

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("Sorry, the file "+ filename + " does not exist.")
else:
    words = contents.split()
    words_number = len(words)
    print("The text has " + str(words_number) + " words.")


#10.3.7使用多个文件
#将计算字符个数的代码移到一个名为count_words()的函数中（重新编写注释和文档字符串）
def count_words(filename):
    """计算一个文件中大致包含多少个单词"""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("Sorry,the file " + filename + " does not exist.")
    else:
        words = contents.split()
        number_words = len(words)
        print("The file " + filename + " has about " + str(number_words) + " "
                + " words.")

count_words('programming.txt')
count_words('alice.txt')

#10.3.8 失败时一声不吭（pass 语句）
#程序在发生异常时一声不吭，就像什么也没有发生一样继续运行
def count_words(filename):
    """计算一个文件中有多少个单词"""

    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        number_words = len(words)
        print("The file " + filename + " has about " +
              str(number_words) + " words.")


count_words("programming.txt")
count_words('alice.txt')

#10.4 存储数据
#10.4.1 使用json.dump()和json.load()
import json

numbers = [2,3,5,7,11,13]

filename = "number.json"
with open(filename,"w") as f_obj:
    json.dump(numbers,f_obj)


#方法write()是将一个字符串写入文件
#函数json.dump()是将简单的Python数据结构转储到文件中

#使用json.load()将这个列表读取到内存中
import json

filename = "number.json"
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)

#10.4.2保存和读取用户生成的数据
#先存储
import json

username = input("What's your name? ")

filename = "username.json"
with open(filename,"w") as f_obj:
    json.dump(username,f_obj)
    print("We'll remember you when you come back," + username +"!")

#再读取
import json

filename = "username.json"

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back," + username + "!")

#将上面两个程序合并到一起，并使用try-except代码块
import json

filename = "username.json"

try:
    with open(filename) as file_object:
        username = json.load(file_object)
        print("Welcome back," + username + "!")
except FileNotFoundError:
    name = input("What's your name? ")

    with open(filename,"a") as f_obj:
        json.dump(name,f_obj)
        print("We will remember you when you come back," + name + "!")

#用try-except-else代码块
import json

filename = "username.json"

try:
    with open(filename) as file_object:
        username = json.load(file_object)

except FileNotFoundError:
    name = input("What's your name? ")

    with open(filename,"w") as f_obj:
        json.dump(name,f_obj)
        print("We will remember you when you come back," + name + "!")

else:
    print("Welcome back," + username + "!")

#10.4.3重构
#将上述过程放进名为greet_user()的函数中
import json

def greet_user():
    filename = "username.json"
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        username = input("What's your name? ")
        with open(filename,"w") as f_object:
            json.dump(username,f_object)
            print("We will remember you when you come back," + username + "!")
    else:
        print("Welcome back," + username + "!")

greet_user()

#重构函数greet_user()，让他不执行那么多任务
import json

def get_stored_username():
    """如果用户存储了用户名就获取它"""
    filename = "username.json"
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = input("What's your name? ")
        filename = "username.json"
        with open(filename,"w") as f_object:
            json.dump(username,f_object)
            print("We will remember you when you come back," + username+ "!")


greet_user()

#需要去掉注释和文档字符串才能运行
#解决方法：在文件最开始加上
'''#!/usr/bin/python
# -*- coding:utf8 -*-'''
import json

def get_stored_username():
    filename = "username.json"
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():

    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = input("What's your name? ")
        filename = "username.json"
        with open(filename,"w") as f_object:
            json.dump(username, f_object)
            print("We will remember you when you come back," + username + "!")


greet_user()

#将greet_user()中的另一个代码块提取出来，移到函数get_new_username()中
import json


def get_stored_username():
    filename = "username.json"
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("What's your name? ")
    filename = "username.json"
    with open(filename, "w") as file_obj:
        json.dump(username, file_obj)
        return username


def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back," + username + "!")
    else:
        username = get_new_username()
        print("We will remember you when you come back," + username + "!")

greet_user()













