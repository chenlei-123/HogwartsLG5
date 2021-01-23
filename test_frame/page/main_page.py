# 点击通讯录
from appium.webdriver.common.mobileby import MobileBy

from test_frame.basepage import BasePage
from test_frame.page.addresslist_page import AddressListPage


class MainPage(BasePage):

    def click_addresslist(self):
        self.find((MobileBy.XPATH, '//*[@text="通讯录"]')).click()
        self.find((MobileBy.XPATH, "//*[@text='我的客户']")).click()
        return AddressListPage(self.driver)
