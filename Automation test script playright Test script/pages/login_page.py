from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_URL = "https://practice.qabrains.com/ecommerce/login"
    EMAIL_SELECTOR = 'input[name="email"]'
    PASSWORD_SELECTOR = 'input[name="password"]'
    LOGIN_BTN = 'button[type="submit"]'
    ERROR_MSG = "text=Neither email nor password matched."

    def login(self, email: str, password: str) -> None:
        if self.page.locator(self.EMAIL_SELECTOR).count() == 0:
            self.page.goto(self.LOGIN_URL)

        self.fill(self.EMAIL_SELECTOR, email)
        self.fill(self.PASSWORD_SELECTOR, password)
        self.click(self.LOGIN_BTN)

    def is_logged_in(self) -> bool:
        try:
            self.page.wait_for_url("**/ecommerce", timeout=5000)
        except PlaywrightTimeoutError:
            return False
        return True

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MSG)
