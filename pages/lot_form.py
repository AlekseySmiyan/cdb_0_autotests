from selenium.webdriver.common.by import By

from .base_page import BasePage


class LotForm(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    save = (By.XPATH, '//*[@ng-click="save()"]')

    def lot_field(self, name):
        return (By.XPATH, '//input[@ng-model="lot.{}"]'.format(name))

    def fill_lot(self, index, data):
        fill = self.fill
        field = self.lot_field
        fill(field('title'), data.lot_title(index))
        fill(field('description'), data.lot_description(index))
        fill(field('value.amount'), data.lot_value_amount(index))
        fill(field('minimalStep.amount'), data.lot_minimalstep_amount(index))

    def save_lot(self):
        self.click(self.save)

