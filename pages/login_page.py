from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/", "No login url" 

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.login_form), "No autorizacion form"
        assert True

    def should_be_register_form(self):
        self.is_element_present(*LoginPageLocators.register_form), "No register form"
        assert True
    def register_new_user(self,email,password):
        mail = self.browser.find_element(*LoginPageLocators.email)
        mail.send_keys(email)
        pass1 = self.browser.find_element(*LoginPageLocators.passw1)
        pass1.send_keys(password)
        pass2 = self.browser.find_element(*LoginPageLocators.passw2)
        pass2.send_keys(password)
        clck=self.browser.find_element(*LoginPageLocators.click)
        clck.click()
        

