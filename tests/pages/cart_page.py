from playwright.sync_api import Page, expect, Locator
from tests.pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_total = page.get_by_text("Total:")

    def get_cart_item_row(self, item_name: str) -> Locator:
        return self.page.locator("tr.cart-item", has_text=item_name)
    
    def get_unit_price(self, item_name: str) -> float:
        item_row = self.get_cart_item_row(item_name)
        price = item_row.locator("td").nth(1).text_content()
        return self.parse_price(price)
    
    def get_unit_quantity(self, item_name: str) -> int:
        item_row = self.get_cart_item_row(item_name)
        quantity = item_row.locator("td input[name='quantity']").input_value()
        return int(quantity)
    
    def get_item_subtotal(self, item_name: str) -> float:
        item_row = self.get_cart_item_row(item_name)
        subtotal = item_row.locator("td").nth(3).text_content()
        return self.parse_price(subtotal)
    
    def total_cost_is_visible(self, total: str) -> None:
        expect(self.cart_total).to_contain_text(total)
