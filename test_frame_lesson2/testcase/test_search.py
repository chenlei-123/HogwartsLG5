from test_frame_lesson2.app import App


def test_search():
    app = App()
    app.start().goto_main().goto_market_page().goto_search().search()


def test_mine():
    app = App()
    app.start().goto_main().goto_mine()
