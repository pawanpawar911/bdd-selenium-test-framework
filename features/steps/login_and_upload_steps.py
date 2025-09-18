from behave import given, when, then
from base_pages.login_and_upload_page import LoginPage
from base_pages.base_page import BasePage
from utilities.read_properties import ReadConfig
from utilities.customLogger import LogGenerate
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
    
# -----------------------------
# Common Setup
# -----------------------------
@given("I open the application")
def step_open_application(context):
    """Just a placeholder since app is already opened in before_scenario"""
    assert context.driver is not None, "WebDriver not initialized"

# -----------------------------
# Signup Scenarios
# -----------------------------
@when("I sign up with valid username and password")
def step_signup_valid(context):
    """Enter signup credentials and submit"""
    
    logger = LogGenerate.logger_file()
    try: 
        usr = ReadConfig.get_valid_usrName()
        pwd = ReadConfig.get_valid_passWord()
        context.login_page.enter_signup_usrname(usr)
        context.login_page.enter_signup_password(pwd)
        context.login_page.click_signup()
    except Exception as e:
        context.login_page.save_screenshot("login_page_signup_failure")
        logger.error(f"Sign up step failed: {e}", exc_info=True)
        raise AssertionError(f"Step failed due to: {e}")

@then("I should see a signup success message")
def step_signup_success(context):
    """Validate signup success message"""
    logger = LogGenerate.logger_file()
    try: 
        msg = context.login_page.signup_msg().strip()
        assert "Sign-up successful! Please login." in msg, f"Unexpected signup message: {msg}"

    except Exception as e:
        context.login_page.save_screenshot("login_page_signup_failure")
        logger.error(f"Signup assertion step failed: {e}", exc_info=True)
        raise AssertionError(f"Step failed due to: {e}")
    
# -----------------------------
# Login Scenarios
# -----------------------------
@when("I login with invalid username and password")
def step_login_invalid(context):
    """Attempt login with invalid credentials"""
    logger = LogGenerate.logger_file()
    try: 
        usr = ReadConfig.get_invalid_usrName()
        pwd = ReadConfig.get_invalid_passWord()
        context.login_page.enter_usrname(usr)
        context.login_page.enter_password(pwd)
        context.login_page.click_login()
    except Exception as e:
        context.login_page.save_screenshot("login_page_invalid_login_failure")
        logger.error(f"Invalid login step failed: {e}", exc_info=True)
        raise AssertionError(f"Step failed due to: {e}")
    
@then("I should see an invalid login message")
def step_invalid_login(context):
    """Validate invalid login message"""
    logger = LogGenerate.logger_file()
    try: 
        msg = context.login_page.signup_msg().strip()
        assert "Invalid username or password." in msg, f"Unexpected error message: {msg}"
    except Exception as e:
        context.login_page.save_screenshot("login_page_invalid_login_failure")
        logger.error(f"Invalid login assertion step failed: {e}", exc_info=True)
        raise AssertionError(f"Step failed due to: {e}")
        
@when("I login with valid username and password")
def step_login_valid(context):
    """Login using valid credentials"""
    logger = LogGenerate.logger_file()
    try: 
        usr = ReadConfig.get_valid_usrName()
        pwd = ReadConfig.get_valid_passWord()
        context.login_page.enter_usrname(usr)
        context.login_page.enter_password(pwd)
        context.login_page.click_login()
    except Exception as e:
        context.login_page.save_screenshot("login_page_valid_login_failure")
        logger.error(f"Valid login step failed: {e}", exc_info=True)
        raise AssertionError(f"Step failed due to: {e}")
        
@then("I should see a login success message")
def step_login_success(context):
    """Validate login success message"""
    logger = LogGenerate.logger_file()
    try: 
        msg = context.login_page.login_msg()
        assert "welcome" in msg.lower() or "success" in msg.lower(), f"Unexpected login message: {msg}"

    except Exception as e:
        context.login_page.save_screenshot("login_page_valid_login_failure")
        logger.error(f"Valid login step failed: {e}", exc_info=True)
        raise AssertionError(f"Step failed due to: {e}")
        
# -----------------------------
# File Upload Scenarios
# -----------------------------
@when('I upload a file "{file_path}"')
def step_upload_file(context, file_path):
    """Upload a file given by file_path"""
    logger = LogGenerate.logger_file()
    try: 
        context.login_page.choose_file_click(file_path)
        context.login_page.upload_file_button()
    except Exception as e:
        context.login_page.save_screenshot("upload_page_file_failure")
        print(f"Got an error: {e}")
        logger.error(f"Upload step failed: {e}", exc_info=True)
        raise AssertionError(f"Step failed due to: {e}")
        
@then("I should see a file upload success message")
def step_upload_success(context):
    """Validate upload success message"""
    logger = LogGenerate.logger_file()
    try: 
        
        context.upload_msg = WebDriverWait(context.driver, 30).until(
            lambda d: context.login_page.upload_file_msg()
        )
        logger.info(f"Upload message: {context.upload_msg}")
        assert "uploaded" in context.upload_msg.lower(), f"Unexpected upload message: {context.upload_msg}"
    except Exception as e:
        context.login_page.save_screenshot("upload_page_file_failure")
        logger.error(f"Upload assertion Step failed due to: {e}")
        raise AssertionError(f"Step failed due to: {e}")
        
@then("I should see a file too large error")
def step_file_too_large_error(context):
    """Validate file upload failure due to size"""
    logger = LogGenerate.logger_file()
    try: 
        error_msg = WebDriverWait(context.driver, 30).until(
            lambda d: context.login_page.upload_file_msg()
        )
        logger.info(f"Upload error message: {error_msg}")
        assert "too large1" in error_msg.lower(), f"Unexpected error message: {error_msg}"
    except Exception as e:
        context.login_page.save_screenshot("upload_page_file_too_large_failure")
        logger.error(f"Upload large file Step failed due to: {e}")
        raise AssertionError(f"Step failed due to: {e}")
