import time

from pages.product_page import ProductPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_correct_value_in_the_allert()
    # time.sleep(1)
    page.solve_quiz_and_get_code()
    page.check_product_name_in_the_buscet()
    page.check_product_price_in_the_buscet()
    time.sleep(100)
