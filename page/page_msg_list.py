import page
from base.base import Base


class PageList(Base):
    def page_click_new_msg(self):
        self.base_click(page.new_msg_btn)