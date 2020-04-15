'''create account page'''
# from selenium import webdriver
from robot.api import logger

from selenium.webdriver.common.by import By

class create_account_page():
    '''this class will define all locators and function on Create Account Page'''
    
    def __init__(self):
        self.USERNAME_TXT = "input.username"                    #CSS
        self.PASSWORD_TXT = "input.password"                    #CSS
        self.EMAIL_TXT = "input.email"                          #CSS
        self.FULLNAME_XT = "input.fullName"                     #CSS
        self.CONFIRM_PASSWORD_TXT = "input.confirm-password"    #CSS
        #self.CREATE_ACCOUNT_BTN = "//a[@href='/register']"
        self.REGISTER_BTN = "button.mb-4.auth-button.btn.btn-primary"   #CSS
        self.I_HAVE_ACCOUNT_BTN = "//a[@href='/login']"
        self.PASSWORD_MISMATCH = "//*[contains(text(), 'Please enter the same password as above')]"
        self.ENTER_INVALID_USERNAME = "//*[contains(text(), 'Please enter username.')]"
        self.ENTER_INVALID_PASSWORD = "//*[contains(text(), 'Please enter password.')]"
        self.ENTER_INVALID_FULLNAME = "//*[contains(text(), 'Please enter fullName.')]"
        self.ENTER_INVALID_EMAIL = "//*[contains(text(), 'Please enter email.')]"
        self.INVALID_CONFIRMPASSWORD = "//*[contains(text(), 'Please enter confirmPassword.')]"
        self.INVALID_EMAIL = "//*[contains(text(), 'Please enter a valid email address')]"
        self.DUPLICATE_ACCOUNT = "//*[contains(text(), 'This field must be unique.')]"
  
    def click_register_button(self, driver):
        '''click create button in create account page'''
        logger.info("start click create button")
        element = driver.find_element(By.CSS_SELECTOR ,self.REGISTER_BTN)
        element.click()
        logger.info("click register button successully")
         
    def input_username_create_page(self, driver, username):
        element = driver.find_element(By.CSS_SELECTOR, self.USERNAME_TXT)
        element.send_keys(username)
        logger.info("input username successfully")
         
    def input_password_create_page(self, driver, password):
        element = driver.find_element(By.CSS_SELECTOR, self.PASSWORD_TXT)
        element.send_keys(password)
        logger.info("input password successfully")
    
    def input_confirm_password_create_page(self, driver, password):
        element = driver.find_element(By.CSS_SELECTOR, self.CONFIRM_PASSWORD_TXT)
        element.send_keys(password)
        logger.info("input confirm password successfully")
        
    def input_full_name_create_page(self, driver, password):
        element = driver.find_element(By.CSS_SELECTOR, self.FULLNAME_XT)
        element.send_keys(password)
        logger.info("input full name successfully")
        
    def input_email_create_page(self, driver, password):
        element = driver.find_element(By.CSS_SELECTOR, self.EMAIL_TXT)
        element.send_keys(password)
        logger.info("input email successfully")
        
    def click_i_have_account_button(self, driver):
        driver.find_element(By.XPATH, self.I_HAVE_ACCOUNT_BTN).click()
        logger.info("Click I have account button successfully")
    
        