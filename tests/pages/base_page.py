from playwright.sync_api import Page

class BasePage:
    def __init__(self, page:Page):
        self.page = page          

    def go_to_page(self, nav_item: str) -> None:
        self.page.get_by_role("link", name=nav_item).click()
    
    def go_to_url(self, url) -> None:
        self.page.goto(url)
    
    def parse_price(self, price_str: str) -> float:
        return float(price_str.replace("$", "").strip())