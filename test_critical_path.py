import time
import pytest
from .pages.auth_page import AuthPage
from .pages.header_page import HeaderPagePreconditions
from .pages.header_page import HeaderPageGetTeeMatik
from .pages.header_page import HeaderPageNewOrder

#@pytest.mark.skip
class TestAuthorizeNegative():
    def test_check_auth_form(self, browser):
        link = "https://rocket-girl.dev.superprotocol.com/login"
        page = AuthPage(browser, link)
        page.open()
        page.auth_form_presence()
        page.check_auth_form_title()
        page.check_auth_form_login_btn()

    def test_auth_with_no_token(self, browser):
        link = "https://rocket-girl.dev.superprotocol.com/login"
        page = AuthPage(browser, link)
        page.open()
        page.auth_with_no_token()

    def test_auth_with_incorrect_token_overdue(self, browser):
        link = "https://rocket-girl.dev.superprotocol.com/login"
        page = AuthPage(browser, link)
        page.open()
        page.auth_with_incorrect_token_overdue()

    def test_auth_with_incorrect_token_eng(self, browser):
        link = "https://rocket-girl.dev.superprotocol.com/login"
        page = AuthPage(browser, link)
        page.open()
        page.auth_with_incorrect_token_eng()

@pytest.mark.debug
class TestAuthorizePreconditions():
    def test_auth_with_correct_token(self, browser):
        link = "https://rocket-girl.dev.superprotocol.com/login"
        page = AuthPage(browser, link)
        page.open()
        page.auth_with_correct_token()

    def test_authorize_mm(self, browser):
        link = "chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/welcome"
        page = HeaderPagePreconditions(browser, link)
        page.open()
        page.auth_metamask()

    def test_connect_wallet_in_header(self, browser):
        link = "https://rocket-girl.dev.superprotocol.com/"
        page = HeaderPagePreconditions(browser, link)
        page.open()
        page.click_connect_wallet_in_header()
        page.mm_connection_alerts()
        page.open()

class TestWalletReplenishment():
    def test_get_matik_positive(self, browser):
        link = "https://rocket-girl.dev.superprotocol.com/"
        page = HeaderPageGetTeeMatik(browser, link)
        page.open()
        page.check_tee_and_matik_balance()
        page.click_get_matik_btn()
        page.check_confirm_mesage_when_click_get_matik_or_tee_btn()
        page.confirm_alert_when_get_matik_or_tee()
        page.check_positive_result_get_matik_or_tee()

    def test_get_matik_double_ask_alert(self, browser):
        link = "https://rocket-girl.dev.superprotocol.com/"
        page = HeaderPageGetTeeMatik(browser, link)
        page.click_get_matik_btn()
        page.check_negative_alert_when_double_ask_get_matik_or_tee()
        page.close_negative_alert_when_double_ask_get_matik_or_tee()

    def test_get_tee_positive(self, browser):
        link = "https://rocket-girl.dev.superprotocol.com/"
        page = HeaderPageGetTeeMatik(browser, link)
        page.open()
        page.check_tee_and_matik_balance()
        page.click_get_tee_btn()
        page.check_confirm_mesage_when_click_get_matik_or_tee_btn()
        page.confirm_alert_when_get_matik_or_tee()
        page.check_positive_result_get_matik_or_tee()

    def test_get_tee_double_ask_alert(self, browser):
        link = "https://rocket-girl.dev.superprotocol.com/"
        page = HeaderPageGetTeeMatik(browser, link)
        page.click_get_tee_btn()
        page.check_negative_alert_when_double_ask_get_matik_or_tee()
        page.close_negative_alert_when_double_ask_get_matik_or_tee()
