import pytest
from playwright.sync_api import sync_playwright

from elements.button import Button

def test_button_example():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://bpmsoft.ru")

        # Пример кнопки с data-testid="login-btn"
        login_btn = Button(
            page=page,
            locator="a.bpm-button.bpm-button--default.bpm-button--primary",
            name="ADD Todo Input"
        )

        login_btn.check_visible()
        login_btn.check_enabled()
        login_btn.click()

        browser.close()
