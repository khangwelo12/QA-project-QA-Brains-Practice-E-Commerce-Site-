import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def browser(request):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        request.cls.page = page
        yield page
        context.close()
        browser.close()
