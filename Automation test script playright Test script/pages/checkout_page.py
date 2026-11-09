from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    def open_checkout(self) -> None:
        self.page.locator("header [role='button']").click()
        self.page.wait_for_url("**/ecommerce/cart")
        self.page.get_by_role("button", name="Checkout").click()
        self.page.wait_for_url("**/ecommerce/checkout-info")

    def fill_shipping(
        self, first_name: str, last_name: str, zip_code: str
    ) -> None:
        self.page.get_by_placeholder("Ex. John").fill(first_name)
        self.page.get_by_placeholder("Ex. Doe").fill(last_name)
        self.page.locator("input").nth(3).fill(zip_code)

    def place_order(self) -> None:
        self.page.get_by_role("button", name="Continue").click()
        self.page.wait_for_url("**/ecommerce/checkout-overview")
        self.page.get_by_role("button", name="Finish").click()
        self.page.wait_for_url("**/ecommerce/checkout-complete")

    def is_order_successful(self) -> bool:
        return self.page.get_by_role(
            "heading", name="Thank you for your order!", exact=True
        ).is_visible()
