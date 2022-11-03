from time import sleep

class BasePage(object):
    def __init__(self,url,driver):
        self.url = url
        self.driver = driver

    def open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def locator_element(self,*locator):
        el = self.driver.find_element(*locator)
        return el

    def quit(self):
        sleep(2)
        self.driver.quit()
