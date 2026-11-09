import pytest

from pages.ecommerce_page import EcommercePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("browser")
class TestSearchSort:
    def _open_ecommerce(self):
        self.page.goto("https://practice.qabrains.com/ecommerce-site")
        login = LoginPage(self.page)
        login.login("test@qabrains.com", "Password123")
        assert login.is_logged_in(), "Login failed"
        return EcommercePage(self.page)

    def test_search_valid(self):
        ecommerce = self._open_ecommerce()
        ecommerce.search("Laptop")
        assert ecommerce.is_product_visible("Laptop")

    def test_sort_price_low_to_high(self):
        ecommerce = self._open_ecommerce()
        ecommerce.sort_by("price-low-high")
        assert ecommerce.is_sorted_correctly("price", "asc")
