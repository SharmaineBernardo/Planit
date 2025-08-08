from playwright.sync_api import Page, expect
from tests.pages.base_page import BasePage

class ContactPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.submit_button = page.get_by_role("link", name="Submit")
        self.back_button = page.get_by_role("link", name="Back", exact=False)
        self.loading_modal = page.get_by_text("Sending Feedback")
        self.alert_error = page.locator('.alert-error')
        self.alert_success = page.locator('.alert-success')

    def submit_contact_form(self) -> None:
        self.submit_button.click()
    
    def enter_field_value(self, field: str, value: str) -> None:
        input_field = self.page.get_by_role("textbox", name=field)
        input_field.fill(value)
    
    def success_alert_is_visible(self) -> None:
        self.loading_modal.wait_for(state="hidden")
        expect(self.alert_success).to_be_visible()

    def back_button_is_visible(self) -> None:
        expect(self.back_button).to_be_visible()
        
    def validate_header_error_message(self) -> None:
        expect(self.alert_error).to_be_visible()
    
    def validate_field_error_message(self, error_message: str) -> None:
        expect(self.page.get_by_text(error_message, exact=True)).to_be_visible()
    
    def header_error_message_not_visible(self) -> None:
        expect(self.alert_error).not_to_be_visible()
    
    def field_error_message_not_visible(self, error_message: str) -> None:
        expect(self.page.get_by_text(error_message, exact=True)).not_to_be_visible()