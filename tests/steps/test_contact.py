from pytest_bdd import when, then, scenarios, parsers
from tests.pages.contact_page import ContactPage

scenarios("features/contact.feature")

@when(parsers.parse("I submit the form"))
def step_submit_contact_form(contact_page: ContactPage) -> None:
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
def step_field_error_message_not_visible(contact_page: ContactPage, error_message: str) -> None:
    contact_page.field_error_message_not_visible(error_message)

@then("I should see the success message")
def step_success_alert_is_visible(contact_page: ContactPage) -> None:
    contact_page.success_alert_is_visible()

@then("I should see the the back button")
def step_back_button_is_visible(contact_page: ContactPage) -> None:
    contact_page.back_button_is_visible()
