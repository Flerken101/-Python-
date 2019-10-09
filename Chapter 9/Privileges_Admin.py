
from user import User

b = ["can add post", "can delete post", "can ban user"]

class Privileges():
    """一次模拟权限的简单尝试"""

    def __init__(self):
        """初始化描述权限的属性"""
        self.privileges = b


    def show_privileges(self):
        """显示管理员的权限"""
        for privilege in self.privileges:
            print("You " + privilege + ".")

class Admin(User):
    """管理员用户的独特之处"""

    def __init__(
            self, first_name, last_name, login_attempts,location):
        """先初始化父类点的属性，再初始化管理员用户的属性"""
        super().__init__(first_name, last_name, login_attempts,location)
        self.privileges = Privileges()
