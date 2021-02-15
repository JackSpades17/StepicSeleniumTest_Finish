from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketClickLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):
    def go_to_product_page(self):
        login_link = self.browser.find_element(*BasketClickLocators.add_basket)
        login_link.click()

    def add_success_book(self):
        login_link = self.browser.find_element(*BasketClickLocators.add_success)
        success_text=login_link.text
        if 'has been added to your basket.' in success_text:
            assert True
        else:
            assert False
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketClickLocators.add_success), \
        "Success message is presented, but should not be"
    
    def should_be_success_message(self):
        assert self.is_element_present(*BasketClickLocators.add_success), \
        "Success message is presented, but should not be"

    def should_invise(self):
        assert self.is_disappeared(*BasketClickLocators.add_success), \
        "Success message is presented, but should not be"



        
