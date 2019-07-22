# coding=utf-8
import unittest

class FirstCase01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('所有case执行之前的前置')

    @classmethod
    def tearDownClass(cls):
        print('所有case执行之后的后置')

    def setUp(self):
        print('这是case的前置条件')

    def tearDown(self):
        print('这是case的后置条件')

    def test_first01(self):
        print('这是第一个case')

    @unittest.skip('不执行第二条')
    def test_first02(self):
        print('这是第二个case')


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase01('test_first02'))
    suite.addTest(FirstCase01('test_first01'))
    unittest.TextTestRunner().run(suite)




