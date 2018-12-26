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

    def fill_tender_description(self, data):
        fill = self.fill
        fill(self.title, data.title)
        fill(self.description, data.description)

    def fill_tender_period(self, data):
        dw = self.date_widget
        dw.fill_enquiry_period_end(data)
        dw.fill_tender_period_start(data)
        dw.fill_tender_period_end(data)

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







