import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base_pages.base_page import BasePage
from utilities.locators import LoginPageLocators
from utilities.customLogger import LogGenerate

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  # inherited base class attributes and methods
        
        self.driver = driver
        self.locators = LoginPageLocators
        
    def open_page(self, url):
        self.driver.get(url)
        
    def logo(self):
        wait = WebDriverWait(self.driver, 10)  # Wait up to 10 seconds
        return wait.until(EC.presence_of_element_located(self.locators.homepage_logo))

    def enter_signup_usrname(self, username):
        self.find_element(*self.locators.username_signup).send_keys(username)   
        
    def enter_signup_password(self, password):
        self.find_element(*self.locators.password_signup).send_keys(password)
        
    def click_signup(self):
        self.find_element(*self.locators.signup_button).click()

    def signup_msg(self):
        logger = LogGenerate.logger_file()
        
        msg = self.driver.switch_to.alert.text
        logger.info(f"Alert message: {msg}")
        
        # Accept the alert popup
        self.driver.switch_to.alert.accept()
        return msg
        
    def enter_usrname(self, username):
        userName = self.find_element(*self.locators.username_login)  
        userName.clear()
        userName.send_keys(username) 
        
    def enter_password(self, password):
        passwrd = self.find_element(*self.locators.password_login)
        passwrd.clear()
        passwrd.send_keys(password) 
        
    def login_msg(self):
        msg = self.find_element(*self.locators.welcome_msg)
        return msg.text
        
    def click_login(self):
        self.find_element(*self.locators.login_button).click()
        
    def choose_file_click(self, upload_file_path):
        wait = WebDriverWait(self.driver, 20)
        choose = wait.until(EC.presence_of_element_located(self.locators.choose_file))
        choose.send_keys(upload_file_path)
        
    def upload_file_button(self):
        wait = WebDriverWait(self.driver, 20)
        upload = wait.until(EC.element_to_be_clickable(self.locators.upload_file))
        upload.click()
        
    def upload_file_msg(self):
        msg = self.find_element(*self.locators.upload_msg)
        return msg.text
        
    def logout_button(self):
        self.find_element(*self.locators.logout_button).click()