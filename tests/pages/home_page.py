from playwright.sync_api import Page
from tests.pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
    
    def click_nav_link(self, nav_item: str) -> None:
        self.page.get_by_role("link", name=nav_item).click()