from selenium.webdriver.common.by import By
"""msg_list"""
new_msg_btn = By.ID, "com.android.mms:id/action_compose_new"
"""new_msg"""
recipient=By.ID,"com.android.mms:id/recipients_editor"
text_content=By.ID,"com.android.mms:id/embedded_text_editor"
send_btn=By.XPATH,"//*[@content-desc='发送']"