from base.base import Base
import page


class PageNewMsg(Base):
    def page_input_recipient(self,recipient):
        self.base_input_content(page.recipient,recipient)

    def page_input_msg_text(self,text):
        self.base_input_content(page.text_content,text)

    def page_send_btn(self):
        self.base_click(page.send_btn)