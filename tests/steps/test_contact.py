from pytest_bdd import given, when, then, scenarios, parsers
from tests.pages.contact_page import ContactPage
from tests.pages.home_page import HomePage
from configs.config import BASE_URL

scenarios("features/contact.feature")

@given("I am on the home page")
def step_go_to_home_page(home_page: HomePage) -> None:
    home_page.go_to(BASE_URL)

@when(parsers.parse("I navigate to the '{nav_item}' page"))
def step_click_nav_link(home_page: HomePage, nav_item: str) -> None:
    home_page.click_nav_link(nav_item)

@when(parsers.parse("I submit the form"))
def step_click_nav_link(contact_page: ContactPage) -> None:
    contact_page.submit_contact_form()

@when("I enter the following information in the fields:")
def step_populate_contact_form(contact_page: ContactPage, datatable: dict[str, str]) -> None:
    for field, value in datatable:
        contact_page.enter_field_value(field, value)

@then("I should see an error in the header message")
def step_validate_header_error_message(contact_page: ContactPage) -> None:
    contact_page.validate_header_error_message()

@then(parsers.parse("I should see that the error message '{error_message}' is displayed"))
def step_validate_field_error_message(contact_page: ContactPage, error_message: str) -> None:
    contact_page.validate_field_error_message(error_message)

@then("I should no longer see an error in the header message")
def step_header_error_message_not_visible(contact_page: ContactPage) -> None:
    contact_page.header_error_message_not_visible()

@then(parsers.parse("I should no longer see the error message '{error_message}'"))
def step_validate_field_error_message(contact_page: ContactPage, error_message: str) -> None:
    contact_page.field_error_message_not_visible(error_message)

@then("I should see the success message")
def step_success_alert_is_visible(contact_page: ContactPage) -> None:
    contact_page.success_alert_is_visible()

@then("I should see the the back button")
def step_back_button_is_visible(contact_page: ContactPage) -> None:
    contact_page.back_button_is_visible()