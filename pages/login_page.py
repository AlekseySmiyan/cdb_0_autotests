from selenium.webdriver.common.by import By

from .base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    login_field = (By.ID, "email")
    password_field = (By.ID, "password")
    signin_btn = (By.ID, "dz-signin-btn")

    def autn(self, login, password):
        fill, click = self.fill, self.click
        fill(self.login_field, login)
        fill(self.password_field, password)
        self.time_out(1)
        click(self.signin_btn)

