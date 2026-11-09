import pytest

from pages.ecommerce_page import EcommercePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("browser")
class TestFavorites:
    def test_add_to_favorites(self):
        self.page.goto("https://practice.qabrains.com/ecommerce-site")
        login = LoginPage(self.page)
        login.login("test@qabrains.com", "Password123")
        assert login.is_logged_in(), "Login failed"

        ecommerce = EcommercePage(self.page)
        ecommerce.add_first_product_to_favorites()
        assert ecommerce.get_favorites_count() == 1
