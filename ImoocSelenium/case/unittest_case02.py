# coding=utf-8
import unittest

class FirstCase02(unittest.TestCase):
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

    def test_first001(self):
        print('这是第00一个case')

    @unittest.skip('不执行第二条')
    def test_first002(self):
        print('这是第00二个case')


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase02('test_first002'))
    suite.addTest(FirstCase02('test_first001'))
    unittest.TextTestRunner().run(suite)




