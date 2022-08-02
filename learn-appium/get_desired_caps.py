from lib2to3.pgen2 import driver
import sys
from appium import webdriver

def get_desired_caps():
    capabilities = {
        "platformName": "Android",
        "platformVersion": "7.1.2",
        "deviceName": "逍遥模拟器",
        "appPackage": "com.intretech.smart",
        "appActivity": "com.intretech.boot.activity.BootActivity",
        "noRest": "True",
        #注意21503写的是逍遥模拟器的端口号
        "udid": "127.0.0.1:21503"
    }
    #注意4723写的是appium的端口号
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilities)
    return driver

#driver = get_desired_caps()
if __name__=="__main__":
    get_desired_caps()
print("连接到逍遥模拟器")