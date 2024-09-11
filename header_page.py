import time
from selenium.webdriver import ActionChains
from .base_page import BasePage
from .locators import HeaderPageLocators
from .locators import AuthPageLocators
from .locators import MetaMaskWindowLocators
from selenium.webdriver.common.by import By


class HeaderPagePreconditions(BasePage):
    def auth_metamask(self):
        self.browser.find_element(*MetaMaskWindowLocators.MM_START_AUTH_BTN).click()
        print("Start auth btn clicked successfully")
        self.browser.find_element(*MetaMaskWindowLocators.MM_WATCHING_REJECT_BTN).click()
        print("MM watching successfully rejected")
        self.browser.find_element(*MetaMaskWindowLocators.MM_IMPORT_WALLET_BTN).click()
        print("MM import btn clicked")

        self.browser.find_element(*MetaMaskWindowLocators.MM_SEKRET_KEY_1).send_keys("*")
        self.browser.find_element(*MetaMaskWindowLocators.MM_SEKRET_KEY_2).send_keys("*")
        self.browser.find_element(*MetaMaskWindowLocators.MM_SEKRET_KEY_3).send_keys("*")
        self.browser.find_element(*MetaMaskWindowLocators.MM_SEKRET_KEY_4).send_keys("*")
        self.browser.find_element(*MetaMaskWindowLocators.MM_SEKRET_KEY_5).send_keys("*")
        self.browser.find_element(*MetaMaskWindowLocators.MM_SEKRET_KEY_6).send_keys("*")
        self.browser.find_element(*MetaMaskWindowLocators.MM_SEKRET_KEY_7).send_keys("*")
        self.browser.find_element(*MetaMaskWindowLocators.MM_SEKRET_KEY_8).send_keys("*")
        self.browser.find_element(*MetaMaskWindowLocators.MM_SEKRET_KEY_9).send_keys("*")
        self.browser.find_element(*MetaMaskWindowLocators.MM_SEKRET_KEY_10).send_keys("*")
        self.browser.find_element(*MetaMaskWindowLocators.MM_SEKRET_KEY_11).send_keys("*")
        self.browser.find_element(*MetaMaskWindowLocators.MM_SEKRET_KEY_12).send_keys("*")
        print("MM secret keys filled in successfully")

        self.browser.find_element(*MetaMaskWindowLocators.MM_NEW_PASS).send_keys("*")
        self.browser.find_element(*MetaMaskWindowLocators.MM_CONFIRM_PASS).send_keys("*")
        print("MM passes filled in successfully")

        self.browser.find_element(*MetaMaskWindowLocators.MM_ACCEPT_TERMS).click()
        self.browser.find_element(*MetaMaskWindowLocators.MM_CONFIRM_IMORT_WALLET_BTN).click()
        self.browser.find_element(*MetaMaskWindowLocators.MM_IMPORT_WALLET_DONE_BTN).click()
        print("MM secret keys, passes, terms accepted")

        self.browser.find_element(*MetaMaskWindowLocators.MM_NETWORK_LIST_CALL).click()
        self.browser.find_element(*MetaMaskWindowLocators.MM_ADD_NETWORK_BTN).click()
        time.sleep(3)
        self.browser.find_element(*MetaMaskWindowLocators.MM_UNFOCUS_CLICK_ON_TITLE).click()

        self.browser.find_element(*MetaMaskWindowLocators.MM_NETWORK_NAME).send_keys("*")
        self.browser.find_element(*MetaMaskWindowLocators.MM_NETWORK_URL).send_keys("*")
        self.browser.find_element(*MetaMaskWindowLocators.MM_NETWORK_ID).send_keys("*")
        self.browser.find_element(*MetaMaskWindowLocators.MM_NETWORK_CURRENCY).send_keys("*")
        self.browser.find_element(*MetaMaskWindowLocators.MM_NETWORK_SAVE_BTN).click()
        print("MM Mumbai network added successfully")

    def click_connect_wallet_in_header(self):
        self.browser.find_element(*HeaderPageLocators.CONNECT_WALLET_HEADER_BTN).click()
        print("Connect wallet btn found and clicked successfully")

    def mm_connection_alerts(self):
        link = "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#connect/l3JMPcs87RjTqYe2mfCIi"
        self.browser.get(link)
        self.browser.find_element(*MetaMaskWindowLocators.MM_CONNECTING_WALLET_FORWARD).click()
        self.browser.find_element(*MetaMaskWindowLocators.MM_CONNECTING_WALLET_CONFIRM).click()
        time.sleep(3)
        link = "https://rocket-girl.dev.superprotocol.com/"
        self.browser.get(link)
        time.sleep(3)
        self.browser.find_element(*HeaderPageLocators.CONNECT_WALLET_HEADER_BTN).click()
        print("Clicked connect wallet btn to refresh data")

    def check_results_auth(self):
        assert self.is_element_present(*HeaderPageLocators.GET_MATIK_BTN), "Get MATIK btn is not presented"
        print("Get MATIK btn is presented")
        assert self.is_element_present(*HeaderPageLocators.GET_TEE_BTN), "Get TEE btn is not presented"
        print("Get TEE btn is presented")
        assert self.is_element_present(*HeaderPageLocators.BALANCE_INFO), "Balance info is not presented"
        print("Balance info is not presented")
        assert self.is_element_present(*HeaderPageLocators.DISCORD_LINK), "Discord link is not presented"
        print("Discord link is presented OK")
        assert self.is_element_present(*HeaderPageLocators.ACCOUNT_DROPDOWN_MENU_BTN), "Dropdown menu btn is not presented"
        print("Dropdown menu btn is presented")
        assert self.is_not_element_present(*HeaderPageLocators.CONNECT_WALLET_HEADER_BTN), "Connect wallet btn is presented, but should not"
        print("Connect wallet btn is not presented")

class HeaderPageGetTeeMatik(BasePage):
    def check_tee_and_matik_balance(self):
        time.sleep(20)
        self.before_balance = self.browser.find_element(*HeaderPageLocators.BALANCE_INFO).text
        print(self.before_balance)

    def click_get_matik_btn(self):
        self.browser.find_element(*HeaderPageLocators.GET_MATIK_BTN).click()
        print("Get Matik btn clicked")

    def click_get_tee_btn(self):
        self.browser.find_element(*HeaderPageLocators.GET_TEE_BTN).click()
        print("Get tee btn clicked")

    def check_confirm_mesage_when_click_get_matik_or_tee_btn(self):
        time.sleep(20)
        assert self.is_element_present(*HeaderPageLocators.REPLENISHMENT_ALERT_WINDOW), "Get Matik/Tee confirm message didn't appear"
        print("Get Matik/Tee confirm message appeared")

    def confirm_alert_when_get_matik_or_tee(self):
        self.browser.find_element(*HeaderPageLocators.GET_MATIK_OR_TEE_OK_BTN).click()
        print("Confirm alert clicked to close")

    def check_positive_result_get_matik_or_tee(self):
        time.sleep(30)
        after_balance = self.browser.find_element(*HeaderPageLocators.BALANCE_INFO).text
        print(after_balance)
        assert self.before_balance != after_balance, "Matik/Tee balance didn't change"
        print("Matik/Tee balance changed (before " + self.before_balance + " after " + after_balance)

    def check_negative_alert_when_double_ask_get_matik_or_tee(self):
        time.sleep(5)
        assert self.is_element_present(*HeaderPageLocators.REPLENISHMENT_ALERT_WINDOW), "Get Matik/Tee error message didn't appear"
        print("Get Matik/Tee error message appeared")

    def close_negative_alert_when_double_ask_get_matik_or_tee(self):
        ActionChains(self.browser).move_by_offset(328, 51).click().perform()
        time.sleep(3)
        assert self.is_not_element_present(*HeaderPageLocators.REPLENISHMENT_ALERT_WINDOW), "Get Matik/Tee error message didn't disappear"
        print("Get Matik/Tee error message disappeared")

class HeaderPageNewOrder(BasePage):
    def click_new_order_btn(self):
        self.browser.find_element(*HeaderPageLocators.NEW_ORDER_BTN).click()
        print("New order btn clicked")
        assert self.is_element_present(*HeaderPageLocators.NEW_ORDER_FORM), "New order form is not displayed"
        print("New order form is displayed")

    def new_order_click_add_solution_btn(self):
        self.browser.find_element(*HeaderPageLocators.NEW_ORDER_ADD_SOLUTION_BTN).click()
        print("Add solution btn is clicked")
        assert self.is_element_present(*HeaderPageLocators.NEW_ORDER_ADD_SOLUTION_LIST), "List of solutions to add is not displayed"
        print("List of solutions to add is displayed")

    def new_order_add_solution_choose_face(self):
        time.sleep(15)
        self.browser.find_element(*HeaderPageLocators.NEW_ORDER_ADD_SOLUTION_CHOOSE_FACE).click()
        print("Solution Face is chosen")
        time.sleep(5)
        assert self.is_element_present(*HeaderPageLocators.NEW_ORDER_FORM), "Not returned to new order form"
        print("Returned to new order form")
        assert self.is_element_present(*HeaderPageLocators.NEW_ORDER_FACE_ADDED), "Added solution field is not displayed"
        print("Added solution field is displayed")
        NEW_ORDER_ADDED_SOLUTION_NAME = self.browser.find_element(By.XPATH, "//div[@id='solution']/div[2]/div/div[1]/div[1]/div/div/div").text
        print(NEW_ORDER_ADDED_SOLUTION_NAME)
        assert NEW_ORDER_ADDED_SOLUTION_NAME == "Face Recognition", "Added solution name is not correct"
        print("Added solution name is correct")

    def new_order_click_add_storage_btn(self):
        self.browser.find_element(*HeaderPageLocators.NEW_ORDER_ADD_STORAGE_BTN).click()