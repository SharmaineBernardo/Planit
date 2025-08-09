from playwright.sync_api import Page
from tests.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def go_to_page(self, nav_item: str) -> None:
        self.page.get_by_role("link", name=nav_item, exact=True).click()
