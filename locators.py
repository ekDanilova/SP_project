from selenium.webdriver.common.by import By

class HeaderPageLocators():
    GET_MATIK_BTN = (By.CSS_SELECTOR, ".Button_grey-fill__dauaG:nth-child(1)")
    GET_MATIK_OR_TEE_OK_BTN = (By.XPATH, "/html/body/div[7]/div/div/div/div[2]/button")
    GET_TEE_BTN = (By.CSS_SELECTOR, ".Button_grey-fill__dauaG:nth-child(2)")
    REPLENISHMENT_ALERT_WINDOW = (By.CSS_SELECTOR, ".ModalOkCancel_body__xpmET")
    REPLENISHMENT_ALERT_TEXT = (By.CSS_SELECTOR, ".ModalResult_txt__25sZ6")
    BALANCE_INFO = (By.CSS_SELECTOR, ".Account_balance__2nBPh")
    DISCORD_LINK = (By.CSS_SELECTOR, ".DiscordLink_icon__39qgS")
    ACCOUNT_DROPDOWN_MENU_BTN = (By.CSS_SELECTOR, ".Dropdown_wrap__2TUwY")
    CONNECT_WALLET_HEADER_BTN = (By.XPATH, "/html/body/div[2]/div/div/div/div/div[1]/div[2]/div/button")
    AREA = (By.CSS_SELECTOR, ".modal-dialog")

    NEW_ORDER_BTN = (By.CSS_SELECTOR, ".Button_primary__MF6GH")
    NEW_ORDER_FORM = (By.CSS_SELECTOR, ".ModalOkCancel_body__xpmET")
    NEW_ORDER_ADD_SOLUTION_BTN = (By.XPATH, "//div[@id='solution']/button")
    NEW_ORDER_ADD_SOLUTION_LIST = (By.CSS_SELECTOR, ".ModalOkCancel_body__xpmET")
    NEW_ORDER_ADD_SOLUTION_CHOOSE_FACE = (By.XPATH, "/html/body/div[7]/div/div/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div")
    NEW_ORDER_FACE_ADDED = (By.XPATH, "//div[@id='solution']/div[2]/div/div[1]/div[1]/div/div/div")
    NEW_ORDER_ADD_STORAGE_BTN = (By.XPATH, "//div[@id='storage']/button")


class AuthPageLocators():
    AUTH_FORM = (By.CSS_SELECTOR, ".ModalOkCancel_body__xpmET")
    AUTH_FORM_TITLE = (By.CSS_SELECTOR, ".ModalOkCancel_header__1GK_S")
    TOKEN_FIELD_PLACEHOLDER = (By.CSS_SELECTOR, "[data-testid='input']")
    AUTH_FORM_LOGIN_BTN = (By.CSS_SELECTOR, ".Button_root__3mH23")
    AUTH_TOKEN_ERROR_MSG = (By.CSS_SELECTOR, ".ErrorBox_error__pGpNM")
    AUTH_FORM_INPUT_FIELD = (By.CSS_SELECTOR, ".InputUi_input__3Z6JI")

class MetaMaskWindowLocators():
    UNLOCK_WINDOW = (By.CSS_SELECTOR, "[data-testid='unlock-page']")
    MM_START_AUTH_BTN = (By.CSS_SELECTOR, "button.button")
    MM_WATCHING_REJECT_BTN = (By.CSS_SELECTOR, "[data-testid='page-container-footer-cancel']")
    MM_IMPORT_WALLET_BTN = (By.CSS_SELECTOR, "[data-testid='import-wallet-button']")
    MM_SEKRET_KEY_1 = (By.CSS_SELECTOR,"[data-testid='import-srp__srp-word-0']")
    MM_SEKRET_KEY_2 = (By.CSS_SELECTOR,"[data-testid='import-srp__srp-word-1']")
    MM_SEKRET_KEY_3 = (By.CSS_SELECTOR,"[data-testid='import-srp__srp-word-2']")
    MM_SEKRET_KEY_4 = (By.CSS_SELECTOR,"[data-testid='import-srp__srp-word-3']")
    MM_SEKRET_KEY_5 = (By.CSS_SELECTOR,"[data-testid='import-srp__srp-word-4']")
    MM_SEKRET_KEY_6 = (By.CSS_SELECTOR,"[data-testid='import-srp__srp-word-5']")
    MM_SEKRET_KEY_7 = (By.CSS_SELECTOR,"[data-testid='import-srp__srp-word-6']")
    MM_SEKRET_KEY_8 = (By.CSS_SELECTOR,"[data-testid='import-srp__srp-word-7']")
    MM_SEKRET_KEY_9 = (By.CSS_SELECTOR,"[data-testid='import-srp__srp-word-8']")
    MM_SEKRET_KEY_10 = (By.CSS_SELECTOR,"[data-testid='import-srp__srp-word-9']")
    MM_SEKRET_KEY_11 = (By.CSS_SELECTOR,"[data-testid='import-srp__srp-word-10']")
    MM_SEKRET_KEY_12 = (By.CSS_SELECTOR,"[data-testid='import-srp__srp-word-11']")
    MM_NEW_PASS = (By.CSS_SELECTOR, "#password")
    MM_CONFIRM_PASS = (By.CSS_SELECTOR, "#confirm-password")
    MM_ACCEPT_TERMS = (By.CSS_SELECTOR, "#create-new-vault__terms-checkbox")
    MM_CONFIRM_IMORT_WALLET_BTN = (By.CSS_SELECTOR, ".create-new-vault__submit-button")
    MM_IMPORT_WALLET_DONE_BTN = (By.CSS_SELECTOR, "[data-testid='EOF-complete-button']")
    MM_ALERT_BTN = (By.CSS_SELECTOR, ".btn-primary")
    MM_NETWORK_LIST_CALL = (By.CSS_SELECTOR, ".chip__right-icon")
    MM_ADD_NETWORK_BTN = (By.CSS_SELECTOR, ".btn-secondary")

    MM_NETWORK_NAME = (By.XPATH, "//div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/label/input")
    MM_NETWORK_URL = (By.XPATH, "//div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/label/input")
    MM_NETWORK_ID = (By.XPATH, "//div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/label/input")
    MM_NETWORK_CURRENCY = (By.XPATH, "//div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[4]/label/input")
    MM_NETWORK_SAVE_BTN = (By.CSS_SELECTOR, ".btn-primary")
    MM_UNFOCUS_CLICK_ON_TITLE = (By.CSS_SELECTOR, ".networks-tab__subheader--break")
    MM_CONNECTING_WALLET_FORWARD = (By.CSS_SELECTOR, ".btn-primary")
    MM_CONNECTING_WALLET_CONFIRM = (By.CSS_SELECTOR, "[data-testid='page-container-footer-next']")