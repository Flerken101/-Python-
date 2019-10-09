"""一个可用于表示汽车的类"""

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