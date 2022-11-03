import unittest
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from ddt import ddt,data,unpack


# 定义一个继承于TestCase类的类
@ddt
class Demo(unittest.TestCase):
    # 前置条件
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    # 后置条件
    def tearDown(self) -> None:
        sleep(3)
        self.driver.quit()

    # 测试用例1
    @data(('http://www.baidu.com','游泳的鱼'),
          ('http://www.baidu.com','小龙女'),
          ('http://www.baidu.com','APIfox'))
    @unpack
    def test_1(self,url,text):
        self.driver.get(url)
        self.driver.find_element(By.ID,'kw').send_keys(text)
        self.driver.find_element(By.ID,'su').click()
        # self.assertEqual('su','aa',msg='不一样')

    # # 测试用例2
    # def test_2(self):
    #     self.driver.get('http://www.baidu.com')
    #     self.driver.find_element(By.ID,'kw').send_keys('乔峰')
    #     self.driver.find_element(By.ID,'su').click()

    # # 测试用例3
    # def test_3(self):
    #     self.driver.get('http://www.baidu.com')
    #     self.driver.find_element(By.ID,'kw').send_keys('小龙女')
    #     self.driver.find_element(By.ID,'su').click()
    #     self.plus()

    # 此函数不会执行，因为没有以test开头，不是测试用例，默认是普通函数，可被其他测试用例调用
    def plus(self):
        print('plus')

# unittest运行函数
if __name__ == '__main__':
    unittest.main()