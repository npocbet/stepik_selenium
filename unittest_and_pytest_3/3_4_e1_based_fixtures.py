from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite..1")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite..1")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        print("1st case 1st test")
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        print("1st case 2nd test")
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self):
        print("start browser for test..2")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test..2")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        print("2nd case 1st test")
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        print("2nd case 2nd test")
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")
