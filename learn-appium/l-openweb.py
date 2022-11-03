from io import BytesIO
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

from Base_Page import BasePage

# 新生产一个ChromeDriver对象
#executable_path=r"D:\Python\Python310\chromedriver.exe"
# driver = webdriver.Chrome()

# 打开OA系统
# driver.get('https://noa.intretech.com/wui/index.html#/?_key=aae298')

# # 找到用户名输入框
# # element = driver.find_element(By.ID,'loginid')
# element = driver.find_element(By.ID,'//*[@id="loginid"]')

# # 输入用户名
# element.send_keys('YQ21911')

# # 找到密码输入框
# element = driver.find_element(By.ID,'userpassword')

# # 输入密码
# element.send_keys('Zfm!202208')

# # 找到“登录”按钮
# element_loging = driver.find_element(By.ID, 'submit')

# # 点击登录按钮
# element_loging.click()w
# sleep(3)

# 打开百度搜索
# driver = webdriver.Chrome()
# driver.get('http://baidu.com')
# element = driver.find_element(By.ID,'kw')
# element.send_keys('软件自动化测试')
# baidu_atn = driver.find_element(By.ID,'su')
# baidu_atn.click()
# sleep(3)
# # 获取第一条搜索结果
# element2 = driver.find_element(By.XPATH,'//*[@id="m6004072710_canvas"]/div/div[1]/div[1]/div/h2/a')
# # 点击链接
# element2.click()



# 小框架
class Search(BasePage):
    input_id = (By.ID,'kw')
    click_id = (By.ID,'su')
    input = '虚竹'
    def input_text(self,txt):
        self.locator_element(*self.input_id).send_keys(txt)
    
    def click_button(self):
        self.locator_element(*self.click_id).click()

    def search_text(self,txt):
        self.open()
        self.input_text(txt)
        self.click_button()

if __name__ == '__main__':
    text = '虚竹'
    url = 'http://www.baidu.com'
    driver = webdriver.Chrome()
    s = Search(url,driver)
    s.search_text(text)    