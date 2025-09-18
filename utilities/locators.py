from selenium.webdriver.common.by import By

# for maintainability we can seperate web objects by page name

class LoginPageLocators(object):
    
    username_signup = (By.ID, "signup-username")    
    password_signup = (By.ID, "signup-password")
    signup_button = (By.XPATH, "//button[@onclick='signup()']")
    
    username_login = (By.ID, "login-username")
    password_login = (By.ID, "login-password")
    login_button = (By.XPATH, "//button[@onclick='login()']")
    
    # choose_file = (By.ID, "profile-pic") #//input[@type='file']
    choose_file = (By.XPATH, "//input[@type='file']") #
    upload_file = (By.XPATH, "//button[@onclick='uploadProfilePic()']")
    
    upload_msg = (By.ID, "upload-msg")
    
    logout_button = (By.XPATH, "//button[@onclick='logout()']")
    
    welcome_msg = (By.ID, "welcome-msg")
    
    