from selenium.webdriver.common.by import By

from .base_page import BasePage


class DateWidget(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # fields
    period = "//*[text()='{}']/following-sibling::div//input"

    @staticmethod
    def create_locator(path, element):
        return {
            'date': (By.XPATH, "{}[contains(@name, 'input-date')]".format(path)),
            'hour': (By.XPATH, "{}[@ng-change='updateHours()']".format(path)),
            'minutes': (By.XPATH, "{}[@ng-change='updateMinutes()']".format(path))
        }.get(element)

    def fill_period(self, path, date):
        locator = self.create_locator
        self.fill_date(locator(path, 'date'), date('date'))
        self.fill_last_element(locator(path, 'hour'), date('hour'))
        self.fill_last_element(locator(path, 'minutes'), date('minutes'))

    def fill_enquiry_period_end(self, data):
        path = self.period.format('Обращение за разъяснениями')
        date = lambda f: data.period('enquiryPeriod', 'endDate')[f]
        self.fill_period(path, date)

    def fill_tender_period_start(self, data):
        path = self.period.format('Начало регистрации предложений')
        date = lambda f: data.period('tenderPeriod', 'startDate')[f]
        self.fill_period(path, date)

    def fill_tender_period_end(self, data):
        path = self.period.format('Конечный срок подачи тендерных предложений')
        date = lambda f: data.period('tenderPeriod', 'endDate')[f]
        self.fill_period(path, date)

    def fill_delivery_start(self, index, data):
        path = self.period.format('Дата с какой ожидается поставка')
        date = lambda f: data.period_delivery(index, 'startDate')[f]
        self.fill_period(path, date)

    def fill_delivery_end(self, index, data):
        path = self.period.format('Требуемый крайний срок поставки')
        date = lambda f: data.period_delivery(index, 'endDate')[f]
        self.fill_period(path, date)
