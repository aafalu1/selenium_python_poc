from behave import *
from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage
from features.pages.LoginPage import LoginPage


@given(u'the user navigates to the login page')
def step_impl(context):
    base_page=BasePage(context.driver)
    base_page.get_application_url()
    login = LoginPage(context.driver)
    login.click_myaccount()
    login.click_on_login_link_option()


@when(u'the user enters valid email address and valid password')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-email').send_keys('aafalu@yahoo.com')
    context.driver.find_element(By.ID, 'input-password').send_keys("Hero123")


@when(u'the user enters invalid email valid password')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-email').send_keys('aafa@yahoo.com')
    context.driver.find_element(By.ID, 'input-password').send_keys("Hero123")


@when(u'the user enters valid email invalid password')
def step_impl(context):
    context.driver.find_element(By.ID, 'input-email').send_keys('aafalu@yahoo.com')
    context.driver.find_element(By.ID, 'input-password').send_keys("He123")


@when(u'the user clicks on login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@type='submit']").click()


@then(u'the user should get error meesage')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR,
                                       "div[class='alert alert-danger alert-dismissible']").is_displayed()


@then(u'the user lands in home page')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, 'Edit your account information').is_displayed()


@when(u'the user enters invalid email address and invalid password')
def step_impl(context):
    print(u'STEP: When the user enters invalid email address and invalid password')
