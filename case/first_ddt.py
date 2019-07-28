# coding=utf-8
import ddt
import sys
sys.path.append('../../ImoocSelenium')
from selenium import webdriver
from business.register_business import RegisterBusiness
import time
import unittest
import HTMLTestRunner
import os
from util.excel_util import ExcelUtil
ex = ExcelUtil()
data = ex.get_data


# curPath = os.path.abspath(os.path.join(os.getcwd()))
# sys.path.append(curPath)


# 邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息
@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://www.5itest.cn/register')
        self.driver.maximize_window()
        self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        time.sleep(3)
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                # file_path = os.path.join(os.getcwd() + '/report/' + case_name + '.png')
                file_path = '../report/' + case_name + '.png'
                self.driver.save_screenshot(file_path)

        self.driver.quit()
    '''
    @ddt.data(
        ['12', 'wudi', '111111', 'code1', 'user_email_error', '请输入有效的电子邮件地址'],
        ['@qq.com', 'wudi', '111111', 'code1', 'user_email_error', '请输入有效的电子邮件地址'],
        ['1287615486184@qq.com', 'wudi', '111111', 'code1', 'user_email_error', '请输入有效的电子邮件地址']
    )

    @ddt.unpack
    '''
    @ddt.data(*data)
    def test_register_case(self, data):
        email, username, password, code, assertCode, assertText = data
        email_error = self.login.register_function(email, username, password, code, assertCode, assertText)
        self.assertFalse(email_error, '测试失败')


if __name__ == '__main__':
    # file_path = os.path.join(os.getcwd() + "/report/" + "first_case.html")
    file_path = '../report/first_case.html'
    f = open(file_path, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='This is first report1',\
                                           description=u'这是我们第一次测试报告1', verbosity=2)
    runner.run(suite)
