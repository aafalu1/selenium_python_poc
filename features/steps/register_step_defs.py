from behave import *


@given(u'the user navigates register page')
def step_impl(context):
    print(u'STEP: Given the user navigates register page')


@when(u'the user enters all mandatory fields')
def step_impl(context):
    print(u'STEP: When the user enters all mandatory fields')


@when(u'the user clicks on continue button')
def step_impl(context):
    print(u'STEP: Then the account should get created')


@when(u'the user enters all fields')
def step_impl(context):
    print(u'STEP: When the user enters all field')


@then(u'the account should get created')
def step_impl(context):
    print(u'STEP: Then the account should get created')
