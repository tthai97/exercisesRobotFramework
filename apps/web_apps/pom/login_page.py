'''
Created on Mar 31, 2020

@author: nmdong
login page
'''
from robot.api import logger

from selenium.webdriver.common.by import By

class login_page():
    '''this class will define all locators and function on Login Page'''
    
    def __init__(self):
        self.USERNAME_TF = "input.username"                             #CSS
        self.PASSWORD_TF = "input.password"                             #CSS
        self.LOGIN_BTN = "button.mb-4.auth-button.btn.btn-primary"    #CSS
        self.PROJECT_TITLE ="//div[@class='project-header row']"
        self.CREATE_ACCOUNT_BTN ="a.auth-link" 
        self.URL_TITLE_TXT = "React App"
        self.INVALID_USERNAME_TXT ="//div[@class='mb-3 input-group']//div[@class='help-block invalid-feedback']"
        self.INVALID_PASSWORD_TXT ="//div[@class='mb-4 input-group']//div[@class='help-block invalid-feedback']" 
        self.INVALID_USERNAME_PASSWORD_TXT ="//*[text()='Username or Password invalid']"   
  
    def loading_login_page(self, driver, timeOut):
        login_ele = self.driver.find_element(By.CSS_SELECTOR, self.USERNAME_TF)
        i = 0;
        while i < timeOut:
            time.sleep(1)
            i = i + 1
            if avatar_ele.size() > 0:
                print("Loading avatar page successfully")
                return True
            else:
                print("Loading avatar page failse")
        return False        
    
    def input_username_login(self, driver, username):
        element = driver.find_element(By.CSS_SELECTOR, self.USERNAME_TF)
        element.send_keys(username)
        logger.info("input username in login page successfully")
         
    def input_password_login(self, driver, password):
        element = driver.find_element(By.CSS_SELECTOR, self.PASSWORD_TF)
        element.send_keys(password)
        logger.info("input password successfully")
         
    def click_login_button(self, driver):
        element = driver.find_element(By.CSS_SELECTOR, self.LOGIN_BTN)
        element.click()
        logger.info("click login button successfully")
    
    def click_create_account_button(self, driver):
        element = driver.find_element(By.CSS_SELECTOR, self.CREATE_ACCOUNT_BTN)
        element.click()
        logger.info("click create account button successfully")
    