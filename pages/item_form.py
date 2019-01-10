from selenium.webdriver.common.by import By

from .base_page import BasePage
from .date_widget import DateWidget


class ItemForm(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.date_widget = DateWidget(driver)

    # buttons
    add_item = (By.XPATH, '//*[@ng-click="vm.addItem()"]')
    measure_list = (By.ID, 'measure-list')
    add_cpv = (By.XPATH, '//input[contains(@id, "classifier-cpv")]')
    confirm_cpv = (By.ID, 'select-classifier-btn')
    add_delivery_address = (By.XPATH, '//*[@ng-model="vm.deliveryAddressTitle"]')
    save = (By.XPATH, '//*[@ng-click="save()"]')
    save_address = (By.XPATH, '//*[@ng-click="vm.save()"]')
    # field
    classifier_search = (By.ID, 'classifier-search-field')
    # check box
    choose_cpv = (By.XPATH, "//input[@ng-change='chooseClassificator(item)']")

    def go_item_form(self):
        self.click_last_element(self.add_item)

    def item_field(self, name):
        return (By.XPATH, '(//input[@ng-model="vm.item.{}"])'.format(name))

    def unit_name(self, name):
        return (By.XPATH, '//a[text()="{}"]'.format(name))

    def classifier_code(self, code):
        return (By.XPATH, '//*[text()="{}"]'.format(code))

    def delivery_address(self, field):
        return (By.NAME, '{}'.format(field))

    def fill_item(self, index, data):
        fill = self.fill_last_element
        click = self.click_last_element
        field = self.item_field
        fill(field('description'), data.item_description(index))
        fill(field('quantity'), data.item_quantity(index))
        click(self.measure_list)
        click(self.unit_name(data.unit_name(index)))

    def select_cpv(self, index, data):
        click = self.click
        self.click_last_element(self.add_cpv)
        self.fill(self.classifier_search, data.cpv_id(index))
        self.wait_visibility_element(self.classifier_code(data.cpv_id(index)))
        click(self.choose_cpv)
        click(self.confirm_cpv)

    def fill_delivery_address(self, index, data):
        fill = self.fill
        field = self.delivery_address
        self.click_last_element(self.add_delivery_address)
        self.time_out(2)

        def value(name):
            return data.delivery_address(index, name)
        fill(field('street_address'), value('streetAddress'))
        fill(field('country_name'), value('countryName'))
        fill(field('company-city'), value('locality'))
        fill(field('delivery-region'), value('region'))
        fill(field('postal-code'), value('postalCode'))
        self.focus_element(self.save_address)
        self.click(self.save_address)

