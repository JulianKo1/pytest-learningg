import allure
from playwright.sync_api import Page

from component.base_component import BaseComponent
from element.input import Input

class RegistrationFormComponent(BaseComponent):
    """
    Компонент формы регистрации. Содержит поля: Email, Username, Password.
    Предоставляет методы для заполнения и проверки отображения формы.
    """
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, "registration-form-email-input", "Email")
        self.username_input = Input(page, "registration-form-username-input", "Username")
        self.password_input = Input(page, "registration-form-password-input", "Password")

    @allure.step("Fill registration form")
    def fill(self, email: str, username: str, password: str):
        """
        Заполняет форму регистрации заданными значениями.

        :param email: Email пользователя
        :param username: Имя пользователя
        :param password: Пароль
        """
        self.email_input.fill(email)
        self.email_input.check_have_value(email)

        self.username_input.fill(username)
        self.email_input.check_have_value(username)

        self.password_input.fill(password)
        self.email_input.check_have_value(password)

    @allure.step("Check that registration form is visible")
    def check_visible(self, email: str, username: str, password: str)
        """
        Проверяет, что форма регистрации отображается корректно и содержит указанные значения.

        :param email: Ожидаемое значение email
        :param username: Ожидаемое значение username
        :param password: Ожидаемое значение пароля
        """
        self.email_input.check_visible()
        self.email_input.check_have_value(email)

        self.username_input.check_visible()
        self.username_input.check_have_value(username)

        self.password_input.check_visible()
        self.password_input.check_have_value(password)