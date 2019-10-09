#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 12:54
# @Author  : Ting
# @Site    : 
# @File    : Chapter 9.py
# @Software: PyCharm

#9.1 创建与使用类
#9.1.1创建Dog类
class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self,name,age):
        #这个方法开头和末尾各有两个下划线
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now stting.")

    def roll_over(self):
        """模拟小狗被名时打滚"""
        print(self.name.title() + " rolled over!")

#9.1.2根据类创建实例
my_dog = Dog('willie',6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

#访问属性（句点表示法）
#在Dog类中：self.name
#在实例my_dog中：my_dog.name

#调用方法（句点表示法）
my_dog.sit()
my_dog.roll_over()

#创建多个实例
my_dog = Dog('willie',6)
your_dog = Dog('lucy',3)

print("\nMy dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.roll_over()

#9.2使用类和实例
#9.2.1 Car类
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()


# 创建实例
my_new_car = Car('audi','a4',2016)
# 调用方法（两种）
print(my_new_car.get_descriptive_name())

a = my_new_car.get_descriptive_name()
print(a)

'''初始化（英语：Initialization）在计算机编程领域中指为数据对象或变量赋初值的做法，
如何初始化则取决于所用的程序语言以及所要初始化的对象的存储类型等属性。
用于进行初始化的程序结构则称为初始化器或初始化列表。初始化和变量声明是明显有区别的，
而且初始化也先于变量声明进行，但两者在实践中仍常被混淆。'''

#9.2.2 给属性指定默认值
#给Car类添加一个新属性和新方法

class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print('This car has ' + str(self.odometer_reading) + " miles on it.")

#创建实例
my_new_car = Car('audi','a4',2016)
#调用方法
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#9.2.3 修改属性的值（三种方式）
#方法一：通过实例直接访问并修改属性的值（将里程表读数设置为23）
print(my_new_car.odometer_reading)
my_new_car.odometer_reading = 23
print(my_new_car.odometer_reading)

#方法二：通过方法修改属性的值（将值传递给一个方法，由它在内部更新）
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print('This car has ' + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage):
        """将里程表读数设置为指定的值"""
        self.odometer_reading = mileage

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

#修改该属性值与类中定义的方法顺序无关，仅与调用方法的顺序有关
my_new_car.update_odometer(23)
my_new_car.read_odometer()

#方法三：通过方法对属性的值进行递增（将里程数增加100）
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车点的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + " " + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条支出汽车里程的消息"""
        print('This car has ' + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值"""
        self.odometer_reading += mileage
        print('This car has ' + str(self.odometer_reading)+" miles on it.")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles
        print('This car has ' + str(self.odometer_reading)+" miles on it.")


# 创建实例
my_used_car = Car('subaru', 'outback', 2013)
# 调用函数
print(my_used_car.get_descriptive_name())
my_used_car.read_odometer()
my_used_car.update_odometer(23500)
my_used_car.increment_odometer(100)

#添加一些逻辑，禁止任何人将里程表读数回调，方法update_odometer中的if-else结构
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print('This car has ' + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值"""
        if mileage >= 0:
            self.odometer_reading += mileage
            print(self.odometer_reading)
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, mile):
        """将里程表读数增加指定的量"""
        self.odometer_reading += mile
        print(self.odometer_reading)



# 创建实例
my_used_car = Car('subaru', 'outback', 2013)
# 调用方法
print(my_used_car.get_descriptive_name())
#用修改属性默认值的三种方法中的任意一种修改它
my_used_car.odometer_reading =23500
my_used_car.read_odometer()

my_used_car.update_odometer(-100)
my_used_car.increment_odometer(100)

#9.3继承
#9.3.1 子类的方法__init__()
#在Car类的基础上创建类ElecyricCar（只需为电动车的特有属性和行为编写代码）
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print('This car has ' + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值"""
        if mileage >= 0:
            self.odometer_reading += mileage
            print(self.odometer_reading)
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, mile):
        """将里程表读数增加指定的量"""
        self.odometer_reading += mile
        print(self.odometer_reading)

class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self,make,model,year):
        """初始化父类的属性"""
        super().__init__(make,model,year)

#创建实例
my_tesla = ElectricCar('tesla',"model s",2016)
#调用函数
print(my_tesla.get_descriptive_name())

#函数super()将父类和子类关联起来

#9.3.3 给子类定义属性和方法
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print('This car has ' + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值"""
        if mileage >= 0:
            self.odometer_reading += mileage
            print(self.odometer_reading)
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, mile):
        """将里程表读数增加指定的量"""
        self.odometer_reading += mile
        print(self.odometer_reading)

class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self,make,model,year):
        """先初始化父类的属性，再初始化电动汽车的特有属性"""
        super().__init__(make,model,year)
        #类中的每个属性都必须要有初始值，哪怕这个这个值是0或空字符串
        self.battery_size = 70

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print('This car has a ' + str(self.battery_size) + "-kwh battery.")

#创建实例
my_tesla = ElectricCar('tesla','model',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

#9.3.4 重新父类的方法（因为不熟练，敲了两遍）
#将父类Car中名为fill_gas_tank()的方法重写（指出全电动汽车（子类）中没有油箱）

#第一遍
#创建父类
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self,make,model,year=2016):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.tank_capacity = 60
        self.odometer_reading = 0

    def get_descriptive_name(self,mileage):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + " "+ self.make + " "+ self.model + " "+ \
                    str(self.odometer_reading) + " "+ str(mileage)
        return long_name

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles oon it.")

    def update_odometer(self,mile):
        """将里程表读数设置为指定的值"""
        if mile >= 0:
            self.odometer_reading += mile
        else:
            print("You can't roll bck an odomrter.")

    def increment_odometer(self,mileage):
        """将里程表指数增加特定的值"""
        self.odometer_reading += mileage

    def fill_gas_tank(self):
        """打印一条关于汽车油箱容量的消息"""
        print("This car has a " + str(self.tank_capacity) + "tank.")

#创建子类ElectricCar（继承）
class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self,make,model,year):
        """先初始化父类的属性，再初始化电动汽车特有的属性"""
        super().__init__(make,model,year)
        self.battery_size = 70

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    #重写父类中的方法fill_gas_tank()
    def fill_gas_tank(self):
        """指出电动汽车没有油箱"""
        print("This can doesn't need a gas tank!")

#创建子类的实例
my_used_car = ElectricCar("tesla",'model S',2013,80)
#调用父类中的方法
print(my_used_car.get_descriptive_name(100))
my_used_car.odometer_reading = 23500
my_used_car.read_odometer()
my_used_car.update_odometer(100)
my_used_car.increment_odometer(100)
#调用子类中的方法
my_used_car.describe_battery()
my_used_car.fill_gas_tank()

#第二遍
#创建父类
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self,make,model,tank_capacity,year=2016):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.tank_capacity = tank_capacity
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self,mile,mileage):
        """返回整洁的描述信息"""
        long_name = str(self.year) + " " + self.make + " " + self.model + " " + \
                    " " + str(self.odometer_reading) + " " + str(mile) + " " + str(mileage)
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mile):
        """将汽车里程设置为特定的值,并禁止将里程表回调"""
        if mile >= self.odometer_reading:
            self.odometer_reading = mile
        else:
            print("You can't roll bake an odometer!")

    def increment_odometer(self,mileage):
        """将里程表增加特定的值"""
        self.odometer_reading += mileage

    def fill_gas_tank(self):
        """打印关于汽车油箱的一条信息"""
        print("This car has a " + str(self.tank_capacity) + "L tank.")

#创建子类（继承）
class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self,make,model,tank_capacity,year,battery_size=100):
        """先初始化父类的属性，，再初始化电动汽车的特有属性"""
        super().__init__(make,model,tank_capacity,year)
        self.battery_size = battery_size

    #给子类定义新的方法
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    #重写父类中的方法fill_gas_tank
    def fill_gas_tank(self):
        """指出全电动汽车没有油箱"""
        print("This cas doesn't need a gsa tank.")

#创建实例
my_used_car = ElectricCar("tesla",'model-S',70,2013,80)
print(my_used_car.get_descriptive_name(23500,100))
#调用父类中的函数
my_used_car.update_odometer(25300)
print(my_used_car.get_descriptive_name(23500,100))
#调用子类的函数
my_used_car.describe_battery()
my_used_car.fill_gas_tank()


#9.3.5将实例用作属性
#创建一个名为Battery的类，并将一个Battery实例用作ElactricCar类的一个属性
class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, size=70):
        """初始化点评的属性"""
        self.size = size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.size) + "-kwh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.size == 70:
            range = 240
        elif self.size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

# Battery()即可以是类Battery的一个实例

# 父类Car
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, tank_capacity, year=2016):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.tank_capacity = tank_capacity
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self, mile, mileage):
        """返回整洁的描述信息"""
        long_name = str(self.year) + " " + self.make + " " + self.model + " " + \
                    " " + str(self.odometer_reading) + " " + str(
            mile) + " " + str(mileage)
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mile):
        """将汽车里程设置为特定的值,并禁止将里程表回调"""
        if mile >= self.odometer_reading:
            self.odometer_reading = mile
        else:
            print("You can't roll bake an odometer!")

    def increment_odometer(self, mileage):
        """将里程表增加特定的值"""
        self.odometer_reading += mileage

    def fill_gas_tank(self):
        """打印关于汽车油箱的一条信息"""
        print("This car has a " + str(self.tank_capacity) + "L tank.")


# 子类ElectricCar
# 将一个Battery实例用作ElactricCar类的一个属性
class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, tank_capacity, year=2013):
        """先初始化父类的属性，，再初始化电动汽车的特有属性"""
        super().__init__(make, model, tank_capacity, year)
        self.battery_size = Battery()

    # 给子类定义新的方法
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    # 重写父类中的方法fill_gas_tank
    def fill_gas_tank(self):
        """指出全电动汽车没有油箱"""
        print("This cas doesn't need a gsa tank.")


# 创建实例
my_tesla = ElectricCar("tesila", "model-L", 70)
# 调用方法
print(my_tesla.get_descriptive_name(23500, 100))
my_tesla.battery_size.describe_battery()
my_tesla.battery_size.get_range()

#9.4 导入类
#9.4.1导入单个类
from car import Car

my_new_car = Car('audi',"a4",70)
print(my_new_car.get_descriptive_name(25300,100))

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#9.4.2 在一个模块中储存多个类
from car_all import ElectricCar

my_tesla = ElectricCar('tesla','model-s',70,2015)

print(my_tesla.get_descriptive_name(25300,100))
my_tesla.battery_size.describe_battery()
my_tesla.battery_size.get_range()

#9.4.3从一个模块中导入多个类
from car_all import Car,ElectricCar

my_beetle = Car('volkswagen','beetle',70)
print(my_beetle.get_descriptive_name(2000,200))

my_tesla = ElectricCar('tesla','model-s',70,2015)
print(my_tesla.get_descriptive_name(25300,100))

#9.4.4 导入整个模块
import car_all

my_beetle = car_all.Car('volkswagen','beetle',70)
print(my_beetle.get_descriptive_name(20000,700))

my_tesla = car_all.ElectricCar('tesla','model-s',70,2015)
print(my_tesla.get_descriptive_name(20000,700))

#9.4.5 导入模块中所有类
#通用语法：from 模块名 import *

#9.4.6 从一个模块中导入另一个模块
#第一种导入方式（都是从模块electric_car中导入）
from electric_car import Car,ElectricCar

#第二中导入方式
from car import Car
from electric_car import ElectricCar

#创建实例并调用函数
my_beetle = Car('volkswagen','beetle',70)
print(my_beetle.get_descriptive_name(2000,200))

my_tesla = ElectricCar('tesla','model-s',70,2015)
print(my_tesla.get_descriptive_name(25300,100))

#9.4.7 自定义工作流程
'''一开始应让代码结构尽可能简单。先尽可能在一个文件中完成所有的工作确定一切都能正确运行后，
在将类移到独立的模块中。'''

#9.5 Python标准库
from collections import OrderedDict

favorite_language = OrderedDict()

favorite_language['jen'] = 'python'
favorite_language['sarah'] = 'c'
favorite_language['edward'] = 'ruby'
favorite_language['phil'] = 'python'

for name,language in favorite_language.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")


#查看Python中模块源码文件位置的方式（以collections为例）
import  collections
print(collections.__file__)