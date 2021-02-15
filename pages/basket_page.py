from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketClickLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class BasketPage(BasePage):
    def see_to_basket(self):
        assert self.is_not_element_present(*BasketClickLocators.see_basket), \
        "Success message is presented, but should not be"
    def basket_null(self):
        assert self.is_element_present(*BasketClickLocators.basket_is_null), \
        "Success message is presented, but should not be"