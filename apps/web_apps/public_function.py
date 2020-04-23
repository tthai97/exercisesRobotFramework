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

class public_function(object):
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

# parent: div.tab-pane.active > div.project-item > div.row
# 
# exemple get: div.tab-pane.active > div.project-item:nth-child(1) > div > div:nth-child(1) > a > span



    def find_element_by_TEXT(self, stringParent, stringElement, stringText):
        elements = driver.find_elements(By.CSS_SELECTOR, stringParent)
        
        
        
        
        
        
        
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

        