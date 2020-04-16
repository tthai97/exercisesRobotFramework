'''
Created on Mar 31, 2020

@author: nmdong

This module is used for defining parent class for ATDA keywords.

ATDA is automation test data analytics system. It could be break down into lower level if 


'''

import time
import sys
import os
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
from utils.grid_manager.selenium_driver import selenium_driver
from utils.grid_manager.grid_driver_factory import grid_driver_factory
from web_apps.pom.login_page import login_page
from web_apps.pom.create_account_page import create_account_page
from web_apps.pom.dash_board_page import dash_board_page

__version__ = '0.0.0.1'

class web_functions(object):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    """ Containing driver and all basic funciton.s

    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """

    def __init__(self):
        """Example of docstring on the __init__ method.

        Examples:
            N/A

        Args:
            desired_capabilities: - A dictionary of capabilities to request when
             starting the browser session. Required parameter.
            command_executor: - Either a string representing URL of the remote server or a custom
             remote_connection.RemoteConnection object. Defaults to 'http://127.0.0.1:4444/wd/hub'.s

        """
        print('*INFO:%d* init atda_web instance')
        CHROME = {'browserName': 'chrome', 'version': '', 'platform': 'ANY'}
        command_executor='http://127.0.0.1:4444/wd/hub'
        BuiltIn().log_to_console('Init ATDA')
        self.desired_capabilities = CHROME
        self.command_executor = command_executor
 
#     def nav_to_create_account_page(self):
#         '''navigate to creare account page'''
#         logger.info("start function navigate to create account page")
#         return create_account_page()

    def nav_to_dash_board_page(self, timeOut):
        '''navigate to dash board page'''
        logger.info("start function navigate to create account page")
        if dash_board_page().loading_avatar_page(self.driver, timeOut):
            print ("navigate to dash board page successfull")
            return True
        print ("navigate to dash board page false")
        return False
    
    def is_project_name_invalid(self):
        if dash_board_page().is_Project_name_invalid(self.driver, 2):
            print("you must be enter project name")
        else:
            print("project nam is acceptable")
    
    def is_project_name_exist(self):
        if dash_board_page().is_Project_name_invalid(self.driver, 2) == True and dash_board_page().is_project_name_empty(self.driver) == False:
            print("your project name already exist!")
        else:
            print("maybe your project name is empty!")
    
    def input_all_infomation_create_account_page(self, username, email, fullname, password, confirmPassword):
        '''input all infomation in creare account page'''
        create_account_page().input_username_create_page(self.driver, username)
        create_account_page().input_email_create_page(self.driver, email)
        create_account_page().input_full_name_create_page(self.driver, fullname)
        create_account_page().input_password_create_page(self.driver, password)
        create_account_page().input_confirm_password_create_page(self.driver, confirmPassword)
 
    def click_register_button_create_account_page(self):
        '''click register button in create account page'''
        logger.info("start function register to create account")
        create_account_page().click_register_button(self.driver)

    def add_new_project_Dash_board_page(self, projectName, projectDescription):
        '''add project in dash board page'''
        logger.info("start function add new project in dash board page")
        dash_board_page().click_new_project_button(self.driver)
        dash_board_page().input_project_name(self.driver, projectName)
        dash_board_page().input_project_description(self.driver, projectDescription)
        dash_board_page().click_create_project_button(self.driver)
    
    def input_project_name_Dash_board_page(self, projectName):
        '''input project name in dash board page'''
        logger.info("start function input project name in dash board page")
        dash_board_page().input_project_name(self.driver, projectName)
    
    def input_project_description_Dash_board_page(self, projectDescription):
        '''input project description in dash board page'''
        logger.info("start function input project description in dash board page")
        dash_board_page().input_project_description(self.driver, projectDescription)
        
    def click_cancel_project_button_Dash_board_page(self):
        '''click cancel create project button in dash board page'''
        logger.info("start function click cancel button in dash board page")
        dash_board_page().click_cancel_project_button(self.driver)
        
    def click_new_project_button_Dash_board_page(self):
        '''click new project button in dash board page'''
        logger.info("start function click new button in dash board page")
        dash_board_page().click_new_project_button(self.driver)
        
    def click_create_project_button_Dash_board_page(self):
        '''click create project button in dash board page'''
        logger.info("start function click create button in dash board page")
        dash_board_page().click_create_project_button(self.driver)
        
    def resister_new_account(self, username, email, fullname, password, confirmPassword):
        self.input_all_infomation_create_account_page(username, email, fullname, password, confirmPassword)
        self.click_register_button_create_account_page()
        
    def input_username_password_login_page(self, username, password):
        '''input username and password in login page'''
        login_page().input_username_login(self.driver, username)
        login_page().input_password_login(self.driver, password)
 
    def click_login_button(self):
        '''click login button'''
        logger.info("start function navigate to create account page")
        login_page().click_login_button(self.driver)
        
    def click_create_account_button(self):
        '''click create account button in login page'''
        logger.info("start function navigate to create account page")
        login_page().click_create_account_button(self.driver)
     
    def open_browser(self, url):
        """Launch web browser with ATDA server info
  
        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.
  
        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.
  
        Note:
            Do not include the `self` parameter in the ``Args`` section.
  
        Args:  
            url (str): Link to website
  
        """
#         BuiltIn().log_to_console('Launching browser: ' + self.desired_capabilities.get('browserName'),'')
        BuiltIn().log_to_console('Open Browser: '+str(self.desired_capabilities)+','+self.command_executor)
        self.driver = grid_driver_factory().create_driver(self.command_executor, self.desired_capabilities)
        BuiltIn().log_to_console('Open URL')
        self.driver.get(url)
#         self.driver.maximize_window()
        self.driver.set_page_load_timeout(30)
    
    def close_browser(self):
        """Close web browser
 
        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.
 
        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.
 
        Note:
            Do not include the `self` parameter in the ``Args`` section.
 
        Args:  
            url (str): Link to website
 
        """
        print('*INFO:%d* Start function close_browser' % (time.time()*1000))
        self.driver.quit()
        print('*INFO:%d* close_browser successfully' % (time.time()*1000))
