from test_frame.basepage import BasePage
from test_frame.page.memberinvite_Page import MemberInvitePage


class AddressListPage(BasePage):
    def add_member(self):
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector().'
        #                          'scrollable(true).instance(0)).'
        #                          'scrollIntoView(new UiSelector().'
        #                          'text("添加成员").instance(0));').click()
        self.scroll_find("添加成员").click()
        return MemberInvitePage(self.driver)
