import os,sys


sys.path.append(os.getcwd())
from time import sleep
import pytest

from base.base_analyse import base_analyse


from base.base_driver import BaseDriver
from page.page import Page


class TestNewMsg:
    def setup(self):
        self.driver=BaseDriver().base_driver()
        self.page=Page(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("args",base_analyse("new_msg.yaml","test_new_msg"))
    def test_new_msg(self,args):
        self.page.page_list().page_click_new_msg()
        self.page.page_new().page_input_recipient(args["recipient"])
        self.page.page_new().page_input_msg_text(args["text"])
        sleep(2)
        self.page.page_new().page_send_btn()


