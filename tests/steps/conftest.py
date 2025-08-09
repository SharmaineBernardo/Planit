from pytest_bdd import given, parsers, step

from tests.pages.home_page import HomePage
from configs.config import BASE_URL

@given("I am on the home page")
def step_go_to_home_page(home_page: HomePage) -> None:
    home_page.go_to_url(BASE_URL)

@step(parsers.parse("I navigate to the '{nav_item}' page"))
def step_click_nav_link(home_page: HomePage, nav_item: str) -> None:
    home_page.go_to_page(nav_item)