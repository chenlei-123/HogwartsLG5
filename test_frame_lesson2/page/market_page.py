
from test_frame_lesson2.basepage import BasePage
from test_frame_lesson2.page.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search(self):
        self.run_steps("../page/market_page.yaml", "goto_search")
        # self.find((By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']")).click()
        return SearchPage(self.driver)
