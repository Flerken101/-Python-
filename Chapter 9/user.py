class User():
    """一次模拟用户列表的简单尝试"""

    def __init__(self, first_name, last_name, login_attempts,location):
        """初始化描述用户信息的属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts
        self.location = location

    def describe_user(self):
        """打印用户信息摘要"""
        info = self.first_name + " " + self.last_name + "   " + self.location
        return info.title()

    def greet_user(self):
        """向用户发出问候"""
        print("Hello, " + self.first_name.title() + " " +
              self.last_name.title() + "!")

    def increment_login_attempts(self):
        """将用户登录次数加1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """将用户登录次数重新设置为0"""
        if self.login_attempts != 0:
            self.login_attempts = 0
