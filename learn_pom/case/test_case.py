'''
    测试用例类：用于执行所有的测试用例
'''
import os
import sys

path = os.getcwd()
sys.path.append(path)

import unittest
from selenium import webdriver
from ddt import ddt,file_data
from page_object.login_page import LoginPage
from page_object.order_page import OrderPage
# sys.path.append(r'\AutoCode\learn-Python\learn_pom')

@ddt
class Case(unittest.TestCase):
    # 用例1：登录
    # 未封装数据
    #  def test_01_login(self):
    #     driver =webdriver.Chrome()
    #     usr = 'zzauto'
    #     pwd = 'zz123456'
    #     lp = LoginPage(driver)
    #     lp.login(usr,pwd)

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.lp = LoginPage(cls.driver)
        cls.op =OrderPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    # 用例1：登录
    # 封装数据ddt传入
    @file_data('../data/user.yaml')
    def test_01_login(self,usr,pwd):
        self.lp.login(usr,pwd)


    # 用例2：下单
    def test_02_order(self):
        self.op.order()

if __name__ == '__main__':
    unittest.main()
