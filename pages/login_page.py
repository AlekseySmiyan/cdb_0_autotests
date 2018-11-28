from selenium.webdriver.common.by import By

from .base_page import BasePage

login_field = (By.ID, "email")
password_field = (By.ID, "password")
signin_btn = (By.ID, "dz-signin-btn")


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def autn(self, login, password):
        fill, click = self.fill, self.click
        fill(login_field, login)
        fill(password_field, password)
        click(signin_btn)

