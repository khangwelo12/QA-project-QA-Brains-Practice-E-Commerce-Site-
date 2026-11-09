import pytest

from pages.ecommerce_page import EcommercePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("browser")
class TestAddToCart:
    def test_add_single_item(self):
        self.page.goto("https://practice.qabrains.com/ecommerce-site")
        login = LoginPage(self.page)
        login.login("test@qabrains.com", "Password123")

        ecommerce = EcommercePage(self.page)
        ecommerce.add_first_product_to_cart()
        assert ecommerce.get_cart_count() == "1"
