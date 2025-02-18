from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


ORDERS_BTN = (By.ID, 'nav-orders')
SEARCH_FILED = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterMoreOnAmazon a')
POPUP_SIGNIN_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-signin-button")


@given('Open Amazon main page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main_page()


@when('Search for {search_word}')
def search_amazon(context, search_word):
    # context.driver.find_element(*SEARCH_FILED).send_keys(search_word)
    # context.driver.find_element(*SEARCH_BTN).click()
    context.app.header.search_for_product(search_word)
    # sleep(5)


@when('Click Orders')
def click_orders(context):
    # context.driver.find_element(*ORDERS_BTN).click()
    # element = context.driver.find_element(*ORDERS_BTN)
    # print('Before refresh: ', element)
    # context.driver.refresh()
    # element = context.driver.find_element(*ORDERS_BTN)
    # print('After refresh: ', element)
    # element.click()
    context.app.header.click_orders()


@when('Verify Orders btn present')
def click_orders(context):
    context.driver.find_element(*ORDERS_BTN)


@when('Click on button from SignIn popup')
def click_sign_in_popup_btn(context):
    context.driver.wait.until(EC.element_to_be_clickable(POPUP_SIGNIN_BTN), message='Signin btn not clickable').click()


@when('Wait for {sec_amount} sec')
def wait_sec(context, sec_amount):
    sleep(int(sec_amount))


@when('Hover over language options')
def hover_lang(context):
    context.app.header.hover_lang()


@when('Select department {alias}')
def select_dep(context, alias):
    context.app.header.select_dep(alias)


@then('Verify Sign In is clickable')
def verify_signin_popup_btn_clickable(context):
    context.driver.wait.until(EC.element_to_be_clickable(POPUP_SIGNIN_BTN),
        message='Signin btn not clickable')


@then('Verify Sign In disappears')
def verify_signin_popup_disappears(context):
    context.driver.wait.until_not(EC.visibility_of_element_located(POPUP_SIGNIN_BTN),
        message='Signin btn did not disappear')



@then('Verify there are {expected_amount} links')
def verify_link_count(context, expected_amount):
    expected_amount = int(expected_amount)
    print('After conversion: => ', type(expected_amount))

    links_count = len(context.driver.find_elements(*FOOTER_LINKS)) # 36
    print(type(links_count))

    # 36 == 36
    assert links_count == expected_amount, f'Expected {expected_amount} links, but got {links_count}'


@then('Verify Spanish option present')
def verify_spanish_lang_present(context):
    context.app.header.verify_spanish_lang_present()


