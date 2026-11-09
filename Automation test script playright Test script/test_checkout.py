import pytest

from pages.checkout_page import CheckoutPage
from pages.ecommerce_page import EcommercePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("browser")
class TestCheckout:
    def test_checkout_with_valid_data(self):
        self.page.goto("https://practice.qabrains.com/ecommerce-site")
        login = LoginPage(self.page)
        login.login("test@qabrains.com", "Password123")
        assert login.is_logged_in(), "Login failed"

        EcommercePage(self.page).add_first_product_to_cart()
        checkout = CheckoutPage(self.page)
        checkout.open_checkout()
        checkout.fill_shipping("John", "Doe", "10001")
        checkout.place_order()
        assert checkout.is_order_successful()
