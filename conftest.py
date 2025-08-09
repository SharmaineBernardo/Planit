import pytest
from playwright.sync_api import sync_playwright, Page
from tests.pages.contact_page import ContactPage
from tests.pages.home_page import HomePage
from tests.pages.shop_page import ShopPage
from tests.pages.cart_page import CartPage

@pytest.fixture(scope="session")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
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

@pytest.fixture()
def shop_page(page: Page) -> ShopPage:
    return ShopPage(page)

@pytest.fixture()
def cart_page(page: Page) -> CartPage:
    return CartPage(page)
