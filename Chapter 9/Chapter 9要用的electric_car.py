"""一组用于表示燃油汽车和电动车的类"""

from car import Car

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
		
		