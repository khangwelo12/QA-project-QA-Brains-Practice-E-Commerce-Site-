import re

from playwright.sync_api import Page


class EcommercePage:
    SORT_OPTIONS = {
        "price-low-high": ("Low to High (Price)", "low"),
        "price-high-low": ("High to Low (Price)", "high"),
        "name-a-z": ("A to Z (Ascending)", "asc"),
        "name-z-a": ("Z to A (Descending)", "desc"),
    }

    def __init__(self, page: Page):
        self.page = page

    def search(self, query: str) -> None:
        search_box = self.page.get_by_role("searchbox")
        if search_box.count() == 0:
            raise LookupError("The ecommerce page does not provide a search box.")
        search_box.fill(query)

    def is_product_visible(self, product_name: str) -> bool:
        return self.page.locator(".products > div").filter(
            has_text=product_name
        ).count() > 0

    def sort_by(self, sort_option: str) -> None:
        try:
            option_name, query_value = self.SORT_OPTIONS[sort_option]
        except KeyError:
            raise ValueError(f"Unsupported sort option: {sort_option}") from None

        self.page.get_by_role("combobox").click()
        self.page.get_by_role("option", name=option_name, exact=True).click()
        self.page.wait_for_url(f"**/ecommerce?order_by={query_value}")

    def is_sorted_correctly(self, field: str, order: str) -> bool:
        if field != "price" or order not in {"asc", "desc"}:
            raise ValueError(f"Unsupported sort field/order: {field}/{order}")

        prices = []
        for card in self.page.locator(".products > div").all():
            price_text = card.locator("span").filter(has_text="$").first.inner_text()
            match = re.search(r"\$\s*([\d,]+(?:\.\d{1,2})?)", price_text)
            if match is None:
                raise ValueError(f"Unable to read product price: {price_text!r}")
            prices.append(float(match.group(1).replace(",", "")))

        expected = sorted(prices, reverse=order == "desc")
        return prices == expected

    def add_first_product_to_cart(self) -> None:
        self.page.get_by_role("button", name="Add to cart").first.click()

    def add_first_product_to_favorites(self) -> None:
        self.page.locator(".products > div [role='button'] button").first.click()

    def get_favorites_count(self) -> int:
        return self.page.locator(
            ".products > div [role='button'] button[style*='rgb(255, 0, 0)']"
        ).count()

    def get_cart_count(self) -> str:
        return (
            self.page.get_by_role("banner")
            .get_by_role("button")
            .first.inner_text()
            .strip()
        )
