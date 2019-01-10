from selenium.webdriver.common.by import By

from .base_page import BasePage
from .date_widget import DateWidget


class TenderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.date_widget = DateWidget(driver)

    # buttons
    add_lot = (By.XPATH, '//*[@ng-click="addLot()"]')
    publish = (By.XPATH, '//*[@ng-click="publish()"]')
    attach_docs = (By.ID, 'attach-docs-btn')
    no_docs = (By.ID, 'no-docs-btn')

    # fields
    title = (By.ID, 'tender-title')
    description = (By.ID, 'tender-description')

    @property
    def tender_id(self):
        return self.get_element_text((By.XPATH, "//*[@class='title']//a"))

    @property
    def tender_title(self):
        return self.get_element_text((By.ID, 'view-tender-title'))

    @property
    def tender_description(self):
        return self.get_element_text((By.ID, 'view-tender-description'))

    @property
    def tender_value_amount(self):
        return self.get_element_text((By.ID, 'view-tender-value'))

    @property
    def list_lots(self):
        return self.elements((By.XPATH, '//*[@class="short-lots__list"]/li'))

    def lot_title(self, index):
        return self.get_element_text((By.ID, 'view-lot-title-{}'.format(index)))

    def lot_description(self,  index):
        return self.get_element_text((By.ID, 'view-lot-description-{}'.format(index)))

    def lot_value_amount(self, index):
        return self.get_element_text((By.XPATH, '(//*[@id="view-lot-value"])[{}]'.format(index + 1)))

    def lot_minimalstep_amount(self, index):
        return self.get_element_text((
            By.XPATH,
            '//*[@id="lot-item-{}"]//*[@class="tender-budget__minimal-step block-info"]//div[2]'.format(index)))

    def list_lot_items(self, index):
        return self.elements((By.XPATH, '//*[@id="lot-item-{}"]//*[@id="view-item-description"]'.format(index)))

    def item_description(self, index):
        return self.get_element_text((By.XPATH, '(//*[@id="view-item-description"])[{}]'.format(index + 1)))

    def item_quantity(self, index):
        return self.get_element_text((By.XPATH, '(//*[@id="quantity"])[{}]'.format(index + 1)))

    def item_unit_name(self, index):
        return self.get_element_text((By.XPATH, '(//*[@id="quantity"]/following-sibling::span)[{}]'.format(index + 1)))

    def item_cpv(self, index):
        return self.get_element_text((
            By.XPATH, '(//*[contains(text(), "ДК 021:2015")]/following-sibling::div)[{}]'.format(index + 1)))

    def full_delivery_address(self, index):
        return self.get_element_text((
            By.XPATH, '(//*[contains(text(), "Место поставки")]/following-sibling::div)[{}]'.format(index + 1)))

    def delivery_date(self, index, period):
        return self.get_element_text((
            By.XPATH, '(//*[contains(@ng-bind, "vm.item.deliveryDate.{}Date")])[{}]'.format(period, index + 1)))

    def fill_tender_description(self, data):
        fill = self.fill
        fill(self.title, data.title())
        fill(self.description, data.description())

    def go_lot_form(self):
        add_lot = self.add_lot
        self.focus_element(add_lot)
        self.click(add_lot)

    def publish_tender(self, docs=False):
        click = self.click
        click(self.publish)
        if docs:
            click(self.attach_docs)
        else:
            click(self.no_docs)







