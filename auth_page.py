import time
from .base_page import BasePage
from .locators import AuthPageLocators
from .locators import HeaderPageLocators

class AuthPage(BasePage):
    def auth_form_presence(self):
        time.sleep(5)
        assert self.is_element_present(*AuthPageLocators.AUTH_FORM), "Auth form is not presented"
        print("OK - Auth form is presented")

    def check_auth_form_title(self):
        time.sleep(5)
        AUTH_FORM_TITLE_CHECK = self.browser.find_element(*AuthPageLocators.AUTH_FORM_TITLE).text
        print(AUTH_FORM_TITLE_CHECK)
        assert AUTH_FORM_TITLE_CHECK == "Access token", "Wrong auth form title"
        print("OK - Auth form title is correct")

    def check_auth_form_login_btn(self):
        assert self.is_element_present(*AuthPageLocators.AUTH_FORM_LOGIN_BTN), "Login btn is not presented"
        print("OK - Login btn is presented")

    def auth_with_no_token(self):
        self.browser.find_element(*AuthPageLocators.AUTH_FORM_LOGIN_BTN).click()
        time.sleep(10)
        assert self.is_element_present(*AuthPageLocators.AUTH_TOKEN_ERROR_MSG), "Auth_with_token_empty_field - Error msg is not presented"
        print("OK - Auth_with_token_empty_field - Error msg is presented")
        assert self.browser.find_element(*AuthPageLocators.AUTH_TOKEN_ERROR_MSG).text == "Incorrect token", "Error in msg"
        print("OK - auth_with_token_empty_field - Error msg is correct")

    def auth_with_incorrect_token_overdue(self):
        self.browser.find_element(*AuthPageLocators.AUTH_FORM_INPUT_FIELD).send_keys("***")
        time.sleep(10)
        self.browser.find_element(*AuthPageLocators.AUTH_FORM_LOGIN_BTN).click()
        assert self.is_element_present(*AuthPageLocators.AUTH_TOKEN_ERROR_MSG), "Auth_with_incorrect_token_rus - Error msg is not presented"
        print("OK - auth_with_incorrect_token_rus - Error msg is presented")
        assert self.browser.find_element(*AuthPageLocators.AUTH_TOKEN_ERROR_MSG).text == "Incorrect token", "Auth_with_incorrect_token_rus - Error in msg"
        print("OK - auth_with_incorrect_token_rus - Error msg is correct")

    def auth_with_incorrect_token_eng(self):
        self.browser.find_element(*AuthPageLocators.AUTH_FORM_INPUT_FIELD).send_keys("***")
        time.sleep(10)
        self.browser.find_element(*AuthPageLocators.AUTH_FORM_LOGIN_BTN).click()
        assert self.is_element_present(*AuthPageLocators.AUTH_TOKEN_ERROR_MSG), "Auth_with_incorrect_token_eng - Error msg is not presented"
        print("OK - auth_with_incorrect_token_eng - Error msg is presented")
        assert self.browser.find_element(*AuthPageLocators.AUTH_TOKEN_ERROR_MSG).text == "Incorrect token", "Auth_with_incorrect_token_eng - Error in msg"
        print("OK - auth_with_incorrect_token_eng - Error msg is correct")

    def auth_with_correct_token(self):
        self.browser.find_element(*AuthPageLocators.AUTH_FORM_INPUT_FIELD).send_keys("***")
        time.sleep(5)
        self.browser.find_element(*AuthPageLocators.AUTH_FORM_LOGIN_BTN).click()
        assert self.is_not_element_present(*AuthPageLocators.AUTH_TOKEN_ERROR_MSG), "Auth_with_correct_token - Error msg is presented, but should not"
        print("OK - auth_with_correct_token - Error msg is not presented")

    def check_correct_auth_result(self):
        assert self.browser.current_url == "https://rocket-girl.dev.superprotocol.com/", "Opens incorrect page"
        print("OK - correct_auth_result_new_user - opens correct page")
        assert self.is_not_element_present(*HeaderPageLocators.GET_MATIK_BTN), "Get MATIK btn is presented, but should not"
        print("OK - correct_auth_result_new_user - Get MATIK btn is not presented")
        assert self.is_not_element_present(*HeaderPageLocators.GET_TEE_BTN), "Get TEE btn is presented, but should not"
        print("OK - correct_auth_result_new_user - Get TEE btn is not presented")
        assert self.is_not_element_present(*HeaderPageLocators.BALANCE_INFO), "Balance info is presented, but should not"
        print("OK - correct_auth_result_new_user - Balance info is not presented")
        assert self.is_not_element_present(*HeaderPageLocators.DISCORD_LINK), "Discord link is presented, but should not"
        print("OK - correct_auth_result_new_user - Discord link is not presented")
        assert self.is_not_element_present(*HeaderPageLocators.ACCOUNT_DROPDOWN_MENU_BTN), "Dropdown menu btn is presented, but should not"
        print("OK - correct_auth_result_new_user - Dropdown menu btn is not presented")
        assert self.is_element_present(*HeaderPageLocators.CONNECT_WALLET_HEADER_BTN), "Connect wallet btn is not presented"
        print("OK - correct_auth_result_new_user - Connect wallet btn is presented")

