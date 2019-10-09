class Restaruant():
    """一次模拟餐馆的简单尝试"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化描述餐馆的属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """简单描述餐馆的名字及主营菜品"""
        print("The " + self.restaurant_name.title() + " is mainly engaged in " +
              self.cuisine_type + ".")

    def open_restaurant(self):
        """打印一条消息指出餐馆正在营业"""
        print("The restaurant is open now.")

    def guests_number(self):
        """打印一条关于接待客人人数的消息"""
        print('This restaurant has received ' + str(self.number_served) +
              " guests.")

    def set_number_served(self, a):
        """将接待过的客人人数设置为特定的值"""
        if a >= self.number_served:
            self.number_served += a
        else:
            print("Please try again.")

    def increment_number_served(self, b):
        """将餐馆接待过的人数增加特定的值"""
        print("I think " + restaruant.restaurant_name.title() +
              " can accommodate " + str(b) + " guests today.")
        self.number_served += b
