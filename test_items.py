import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_guest_should_see_login_link(browser):
    browser.get(link)
    event = EC.element_to_be_clickable((By.CLASS_NAME, "btn-add-to-basket"))
    WebDriverWait(browser, 7).until(event)
    time.sleep(5)
