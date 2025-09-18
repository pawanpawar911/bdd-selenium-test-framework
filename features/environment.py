from selenium import webdriver
from utilities.read_properties import ReadConfig
from base_pages.login_and_upload_page import LoginPage
from utilities.customLogger import LogGenerate


def before_all(context):
    """Runs once before the whole test suite"""
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    logger = LogGenerate.logger_file()
    logger.info("WebDriver initialized.")


def before_scenario(context, scenario):
    """Runs before each scenario"""
    logger = LogGenerate.logger_file()
    base_url = ReadConfig.getWebURL()
    logger.info(f"Opening URL once for scenario: {scenario.name}")
    context.login_page = LoginPage(context.driver)
    context.login_page.open_page(base_url)


def after_scenario(context, scenario):
    """Optional: Clean up after each scenario"""
    logger = LogGenerate.logger_file()
    logger.info(f"Finished scenario: {scenario.name}")
    # You can also add context.driver.delete_all_cookies() here if needed.


def after_all(context):
    """Runs once after the whole test suite"""
    context.driver.quit()