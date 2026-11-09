from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def click(self, selector: str) -> None:
        self.page.locator(selector).click()

    def fill(self, selector: str, text: str) -> None:
        self.page.locator(selector).fill(text)

    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).inner_text()

    def is_visible(self, selector: str) -> bool:
        return self.page.locator(selector).is_visible()
