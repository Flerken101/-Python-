"""一组用于表示燃油汽车和电动车的类"""

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
		
		