import pytest
from playwright.sync_api import sync_playwright, Page
from tests.pages.contact_page import ContactPage
from tests.pages.home_page import HomePage

@pytest.fixture(scope="session")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

@pytest.fixture()
def home_page(page: Page) -> HomePage:
    return HomePage(page)

@pytest.fixture()
def contact_page(page: Page) -> ContactPage:
    return ContactPage(page)
