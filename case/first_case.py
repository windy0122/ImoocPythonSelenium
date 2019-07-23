# coding=utf-8
from business.register_business import RegisterBusiness
from selenium import webdriver
import sys
import time
sys.path.append('D:\\ImoocSelenium')
import unittest
import HTMLTestRunner
import os


class FirstCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        time.sleep(2)
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                # file_path = os.path.join(os.getcwd() + '/report/' + case_name + '.png')
                file_path = '../report/' + case_name + '.png'
                self.driver.save_screenshot(file_path)

        self.driver.quit()


    def test_login_email_error(self):
        email_error = self.login.login_email_error('34', 'user111', '111111', 'test1')
        self.assertFalse(email_error)
        # if email_error == True:
        #     print('注册成功，此条case执行失败')
        # 通过assert判断是否为error

    def test_login_username_error(self):
        username_error = self.login.login_name_error('344@qq.com', '111', '111111', 'test1')
        self.assertFalse(username_error)
        # if username_error == True:
        #     print('注册成功，此条case执行失败')

    def test_login_password_error(self):
        password_error = self.login.login_password_error('79815@163.com', 'ss12', '11111', 'test1')
        self.assertFalse(password_error)
        # if password_error == True:
        #     print('注册成功，此条case执行失败')

    def test_login_code_error(self):
        code_error = self.login.login_code_error('763157@163.com', 'aa111', '111111', 'xxxxx')
        self.assertFalse(code_error)
        # if code_error == True:
        #     print('注册成功，此条case执行失败')

    def test_login_success(self):
        success = self.login.user_base('663355041@qq.com', 'ss123', '111111', 'test1')
        self.assertFalse(success)
        # if self.login.register_succes() == True:
        #     print('注册成功')

# def main():
#      first = FirstCase()


if __name__ == '__main__':
    # file_path = os.path.join(os.getcwd() + "/report/" + "first_case.html")
    # file_path = '../report/first_case.html'
    # f = open(file_path, 'wb')
    suite = unittest.TestSuite()
    # suite.addTest(FirstCase('test_login_success'))
    suite.addTest(FirstCase('test_login_email_error'))
    unittest.TextTestRunner().run(suite)

    # runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='This is first report',\
    #                                        description=u'这是我们第一次测试报告', verbosity=2)
    # runner.run(suite)





