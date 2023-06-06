from behave import *
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


@given(u'the user navigates to the Home Page')
def step_impl(context):
  title= context.driver.title
  print(title)



@when(u'the user enters valid product into the search box field')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("HP")


@when(u'the user enters invalid product into the search box field')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("Honda")

@when(u'the user does not enter any product into the search box field')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("")

@when(u'the user clicks on Search button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@id='search']//button[@type='button']").click()


@then(u'proper message should display in Search Result')
def step_impl(context):
    expected_text = 'There is no product that matches the search criteria.'
    actual_text = context.driver.find_element(By.XPATH, '//h2/following-sibling::p').text
    assert expected_text.__eq__(actual_text)


@then(u'valid product shoud get displayed in search results')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT, 'HP LP3065').is_displayed()
