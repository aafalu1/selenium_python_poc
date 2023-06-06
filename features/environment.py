from selenium import webdriver

from features.utilities.LoadConfig import LoadConfig


def get_webdriver(browser):
    supported_browsers = {
        'chrome': webdriver.Chrome,
        'firefox': webdriver.Firefox,
        'edge': webdriver.Edge,
        'safari': webdriver.safari
    }
    if browser in supported_browsers:
        return supported_browsers[browser]()
    else:
        raise ValueError(f'Unsupported browser: {browser}. Supported browsers are: {list(supported_browsers.keys())}')


def before_scenario(context, driver):
    config = LoadConfig()
    browser = config.string_property_config('app', 'browser')
    print(f'Browser name: {browser}')
    context.driver = get_webdriver(browser)
    context.driver.maximize_window()


def after_scenario(context, driver):
    context.driver.quit()
