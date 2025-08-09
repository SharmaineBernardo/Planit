from playwright.sync_api import Page
from tests.pages.base_page import BasePage


class ShopPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def add_to_cart(self, item_name: str) -> None:
        item = self.page.get_by_role("listitem").filter(has_text=item_name)
        item.get_by_role("link", name="Buy").click()
