# CONTAINS: Browser fixture setup and teardown
from selenium.webdriver import Firefox

def before_all(context):
    context.browser = Firefox()

def after_all(context):
    # context.browser.quit()
    context.browser = None