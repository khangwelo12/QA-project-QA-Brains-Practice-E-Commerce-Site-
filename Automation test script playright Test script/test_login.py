import pytest

from pages.login_page import LoginPage


@pytest.mark.usefixtures("browser")
class TestLogin:
    def test_valid_login(self):
        self.page.goto("https://practice.qabrains.com/ecommerce-site")
        login = LoginPage(self.page)
        login.login("test@qabrains.com", "Password123")
        assert login.is_logged_in(), "Login failed"

    def test_invalid_login(self):
        self.page.goto("https://practice.qabrains.com/ecommerce-site")
        login = LoginPage(self.page)
        login.login("wrong@example.com", "wrongpass")
        assert "Neither email nor password matched." in login.get_error_message()
