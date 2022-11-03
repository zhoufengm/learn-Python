from time import sleep
from selenium.webdriver.common.by import By
import webbrowser
from selenium import webdriver
from ddt import ddt,unpack,data
import unittest
# coding=utf-8

def readFile():
    params = []
    # 中文编码要用utf-8,用gdk会有乱码
    file = open('params.text','r',encoding='utf-8')
    for line in file.readlines():
        params.append(line.strip('\n').split(','))
    return params

@ddt
class Demo(unittest.TestCase):
     # 前置条件
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    # 后置条件
    def tearDown(self) -> None:
        sleep(3)
        self.driver.quit()

    def url_text(self):
        return 'http://www.baidu.com'


    # 测试用例1
    @data(*readFile())
    @unpack
    def test_1(self,url,locator,text):
        self.driver.get(url)
        self.driver.find_element(By.ID,locator).send_keys(text)
        self.driver.find_element(By.ID,'su').click()

if __name__ == '__main__':
    unittest.main()
