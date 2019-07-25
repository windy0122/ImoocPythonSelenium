# coding=utf-8
import ddt
import unittest


# 邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息
@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    @ddt.data(
        ['email','username','password','code','assertCode','assertText']
    )