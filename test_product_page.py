import pytest
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time
import random



def test_guest_can_add_product_to_basket(browser):
    link=f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_product_page()
    page.solve_quiz_and_get_code()
    page.add_success_book()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link=f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_product_page()
    page.solve_quiz_and_get_code()
    #time.sleep(1000)
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link=f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link=f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_product_page()
    page.solve_quiz_and_get_code()
    page.should_invise()

@pytest.mark.need_review
class TestUseProductPage():
    @pytest.mark.parametrize('num', ["0","1", "2","3","4","5","6","7","8","9"])
    def test_guest_can_add_product_to_basket(self,browser,num):
        link=f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_product_page()
        page.solve_quiz_and_get_code()
        page.add_success_book()
    def test_user_can_add_product_to_basket(self,browser):
        link=f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_product_page()
        page.solve_quiz_and_get_code()
        time.sleep(10)
        page.add_success_book()
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasketPage(browser, link)   
        page.open()
        page.click_to_basket()
        page.see_to_basket()
        page.basket_null()
    def test_guest_should_see_login_page_on_product_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        email = str(time.time()) + "@fakemail.org"
        password='admin*'+str(random.randint(1234,5467382))+'OPS'
        link ='http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        page=LoginPage(browser,link)
        page.open()
        page.register_new_user(email,password)
        page.should_be_authorized_user()
        
    def test_user_cant_see_success_message(self,browser):
        link=f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
    def test_user_can_add_product_to_basket(self,browser):
        link=f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_product_page()
        page.solve_quiz_and_get_code()
        time.sleep(10)
        page.add_success_book()
