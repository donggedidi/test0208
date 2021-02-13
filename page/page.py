from page.page_msg_list import PageList
from page.page_new_msg import PageNewMsg


class Page():
    def __init__(self,driver):
        self.driver=driver

    def page_new(self):
        return PageNewMsg(self.driver)

    def page_list(self):
        return PageList(self.driver)

