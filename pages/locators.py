from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    login_url = "http://selenium1py.pythonanywhere.com/"
    login_form = (By.CSS_SELECTOR, "#login_form")
    register_form = (By.CSS_SELECTOR, "#register_form")
    email=(By.CSS_SELECTOR,"input[name='registration-email']")
    passw1=(By.CSS_SELECTOR,"input[name='registration-password1']")
    passw2=(By.CSS_SELECTOR,"input[name='registration-password2']")
    click=(By.CSS_SELECTOR,"button[value='Register']")
class BasketClickLocators():
    add_basket=(By.CSS_SELECTOR,"#add_to_basket_form")
    add_success=(By.CLASS_NAME,"alertinner") 
    click_basket=(By.CSS_SELECTOR,"a[class='btn btn-default']")
    see_basket=(By.CSS_SELECTOR,"div[class='basket-title hidden-xs']")
    basket_is_null=(By.CSS_SELECTOR,"html body div div div div p")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")