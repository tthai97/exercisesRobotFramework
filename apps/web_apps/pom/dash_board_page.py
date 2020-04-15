'''
Created on Apr 7, 2020

@author: tthai
'''
from robot.api import logger

from selenium.webdriver.common.by import By

class dash_board_page(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.LOGO_PAGE_IMG = "img.navbar-brand-full"   #CSS SELECTOR
        self.PROJECT_PAGE_HERF = "a[href='/dash-board']"        #CSS SELECTOR
        self.AVARVAR_IMG = "img.img-avatar"        #CSS SELECTOR
        self.FULLNAME_TXT = "button.new-project-btn"        #CSS SELECTOR
        self.ALL_PROJECT_NAV_LINK = "//li[@class='nav-item' and ./a/text()='All']"        #XPATH        
        self.YOUR_PROJECT_NAV_LINK = "//li[@class='nav-item' and ./a/text()='Your Project']"        #XPATH
        self.NEW_PROJECT_BTN = "button.new-project-btn"      #CSS SELECTOR
        self.CHANGE_PASSWORD_HERF ="a[href='/change-password']"
        self.PROFILE_HREF =""
        self.SETTING_HREF =""
        self.PROJECTS_HREF =""
        self.LOGOUT_HREF =""
        self.PROJECT_NAME_TXT ="input.form-control"
        self.PROJECT_DESCRIPTION_TXT ="textarea.form-control"
        self.CREATE_PROJECT_BTN = "div.modal-footer > button.btn.btn-primary"
        self.CANCEL_PROJECT_BTN = "div.modal-footer > button.btn.btn-secondary"
        
        
        self.HAVE_ACCOUNT_HREF = "a.auth-link"        #CSS SELECTOR
        
        self.PLEASE_ENTER_USERNAME = "//div[contains(text(), 'username')]"        #XPATH
        self.USERNAME_MUST_BE_UNIQUE = "//div[contains(text(), 'unique')]"        #XPATH
        self.PLEASE_ENTER_EMAIL = "//div[contains(text(), 'email')]"        #XPATH
        self.PLEASE_ENTER_FULLNAME = "//div[contains(text(), 'fullName')]"        #XPATH
        self.PLEASE_ENTER_PASSWORD = "//div[contains(text(), 'password')]"        #XPATH
        self.PLEASE_ENTER_CONFIRM_PASSWORD = "//div[contains(text(), 'confirmPassword')]"        #XPATH
        
        
    
    def input_project_name(self, driver, projectName):
        element = driver.find_element(By.CSS_SELECTOR, self.PROJECT_NAME_TXT)
        element.send_keys(projectName)
        logger.info("input project name successfully")
        
    def input_project_description(self, driver, projectDescription):
        element = driver.find_element(By.CSS_SELECTOR, self.PROJECT_DESCRIPTION_TXT)
        element.send_keys(projectDescription)
        logger.info("input project description successfully")
    
    def click_new_project_button(self, driver):
        element = driver.find_element(By.CSS_SELECTOR, self.NEW_PROJECT_BTN)
        element.click()
        logger.info("click new project button successfully")
        
    def click_create_project_button(self, driver):
        element = driver.find_element(By.CSS_SELECTOR, self.CREATE_PROJECT_BTN)
        element.click()
        logger.info("click create project button successfully")

    def click_cancel_project_button(self, driver):
        element = driver.find_element(By.CSS_SELECTOR, self.CANCEL_PROJECT_BTN)
        element.click()
        logger.info("click cancel project button successfully")
        