
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self,driver):
        self.driver=driver

    def base_find_element(self,loc,time=30,poll=0.5):
        return WebDriverWait(self.driver,time,poll).until(lambda x:x.find_element(*loc))

    def base_click(self,loc):
        self.base_find_element(loc).click()

    def base_input_content(self,loc,value):
        self.base_find_element(loc).send_keys(value)
