#!/usr/bin/python
# -*- coding:utf8 -*-

#17.3 测试

import unittest
import look_over_repository

class TestPythonRepos(unittest.TestCase):
    """测试文件python_repos.py"""

    def test_get_status_code(self):
        my_status_code = look_over_repository.get_status_code()
        self.assertEqual(str(my_status_code),"200")

    def test_get_repos_number(self):
        my_repos_number = look_over_repository.get_repos_number()
        self.assertLess(400000,my_repos_number)

    def test_get_repos_returned_number(self):
        my_repos_returned_number = \
            look_over_repository.get_repos_returned_number()
        self.assertLess(30,my_repos_returned_number)

if __name__== '__main__':
    unittest.main()