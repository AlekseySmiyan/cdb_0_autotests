from selenium.webdriver.common.by import By

from .base_page import BasePage


class DateWidget(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @staticmethod
    def create_locator(text, element):
        field = "//*[text()='{}']/following-sibling::div//input".format(text)
        return {
            'date': (By.XPATH, "{}[contains(@name, 'input-date')]".format(field)),
            'hour': (By.XPATH, "{}[@ng-change='updateHours()']".format(field)),
            'minutes': (By.XPATH, "{}[@ng-change='updateMinutes()']".format(field))
        }.get(element)

    def fill_date_time(self, text, date):
        locator = self.create_locator
        self.fill_date(locator(text, 'date'), date['date'])
        self.fill_last_element(locator(text, 'hour'), date['hour'])
        self.fill_last_element(locator(text, 'minutes'), date['minutes'])

    def fill_enquiry_period_end(self, data):
        date = data.period('enquiryPeriod', 'endDate')
        self.fill_date_time('Обращение за разъяснениями', date)

    def fill_tender_period_start(self, data):
        date = data.period('tenderPeriod', 'startDate')
        self.fill_date_time('Начало регистрации предложений', date)

    def fill_tender_period_end(self, data):
        date = data.period('tenderPeriod', 'endDate')
        self.fill_date_time('Конечный срок подачи тендерных предложений', date)

    def fill_tender_periods(self, data):
        self.fill_enquiry_period_end(data)
        self.fill_tender_period_start(data)
        self.fill_tender_period_end(data)

    def fill_delivery_start(self, index, data):
        date = data.period_delivery(index, 'startDate')
        self.fill_date_time('Дата с какой ожидается поставка', date)

    def fill_delivery_end(self, index, data):
        date = data.period_delivery(index, 'endDate')
        self.fill_date_time('Требуемый крайний срок поставки', date)

    def fill_delivery_periods(self, index, data):
        self.fill_delivery_start(index, data)
        self.fill_delivery_end(index, data)
