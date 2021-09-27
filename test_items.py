import time

from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_there_is_a_button_add_item_to_basket(browser):
    browser.get(link)
    time.sleep(5)
    assert browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
