from selenium.webdriver.common.by import By

from .base_page import BasePage


class TenderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # buttons
    publish_tender_button = (By.XPATH, '//*[@ng-click="publish()"]')
    attach_docs_tender_button = (By.ID, 'attach-docs-btn')
    no_docs_tender_button = (By.ID, 'no-docs-btn')

    # fields
    title = (By.ID, 'tender-title')
    description = (By.ID, 'tender-description')

    def fill_tender_description(self, data):
        fill = self.fill
        fill(self.title, data.title)
        fill(self.description, data.description)

    def publish_tender(self, docs=False):
        click = self.click
        click(self.publish_tender_button)
        if docs:
            click(self.attach_docs_tender_button)
        else:
            click(self.no_docs_tender_button)


class LotModal(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # buttons
    add_lot = (By.XPATH, '//*[@ng-click="addLot()"]')
    add_item = (By.XPATH, '//*[@ng-click="vm.addItem()"]')
    measure_list = (By.ID, 'measure-list')
    add_cpv = (By.XPATH, '//input[contains(@id, "classifier-cpv")]')
    confirm_cpv = (By.ID, 'select-classifier-btn')
    add_delivery_address = (By.XPATH, '//*[@ng-model="vm.deliveryAddressTitle"]')
    save_delyvery_address = (By.XPATH, '//*[@ng-click="vm.save()"]')
    save_lot_button = (By.XPATH, '//*[@ng-click="save()"]')
    # field
    lot_fields = lambda *args, name=None: (By.XPATH, '//input[@ng-model="lot.{}"]'.format(name))
    item_fields = lambda *args, name=None: (By.XPATH, '(//input[@ng-model="vm.item.{}"])'.format(name))
    unit_name = lambda *args, name=None: (By.XPATH, '//a[text()="{}"]'.format(name))
    classifier_search = (By.ID, 'classifier-search-field')
    classifier_code = lambda *args, code=None: (By.XPATH, '//*[text()="{}"]'.format(code))
    delivery_address = lambda *args, name: (By.NAME, '{}'.format(name))
    # check box
    choose_cpv = (By.XPATH, "//input[@ng-change='chooseClassificator(item)']")

    def go_lot_modal(self):
        self.focus_element(self.add_lot)
        self.click(self.add_lot)

    def go_item_modal(self):
        self.click_last_element(self.add_item)

    def fill_lot(self, index, data):
        fill = self.fill
        field = self.lot_fields
        self.go_lot_modal()
        fill(field(name='title'), data.lot_title(index))
        fill(field(name='description'), data.lot_description(index))
        fill(field(name='value.amount'), data.lot_value_amount(index))
        fill(field(name='minimalStep.amount'), data.lot_minimalstep_amount(index))

    def fill_item(self, index, data):
        fill = self.fill_last_element
        field = self.item_fields
        click = self.click_last_element
        self.go_item_modal()
        fill(field(name='description'), data.item_description(index))
        fill(field(name='quantity'), data.item_quantity(index))
        click(self.measure_list)
        click(self.unit_name(name=data.unit_name(index)))

    def select_cpv(self, index, data):
        click = self.click
        self.click_last_element(self.add_cpv)
        self.fill(self.classifier_search, data.cpv_id(index))
        self.wait_visibility_element(self.classifier_code(code=data.cpv_id(index)))
        click(self.choose_cpv)
        click(self.confirm_cpv)

    def fill_delivery_address(self, index, data):
        fill = self.fill
        field = self.delivery_address
        self.click_last_element(self.add_delivery_address)
        fill_adress = lambda field_name=None, value_name=None: \
            fill(field(name=field_name), data.delivery_address(index, value_name))
        self.time_out(2)
        fill_adress(field_name='street_address', value_name='streetAddress')
        fill_adress(field_name='country_name', value_name='countryName')
        fill_adress(field_name='company-city', value_name='locality')
        fill_adress(field_name='delivery-region', value_name='region')
        fill_adress(field_name='postal-code', value_name='postalCode')
        self.click(self.save_delyvery_address)

    def save_lot(self):
        self.click(self.save_lot_button)


class DocumentModal(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    add_document = (By.XPATH, '//*[@ng-click="uploadDocument()"]')
    select = lambda *args, name=None: (
        By.XPATH, '//select[@ng-model="document.{}"]'.format(name))
    upload_button = (By.XPATH, '//*[@ng-model="file"]')
    input_file = (By.XPATH, "//input[@type='file']")
    upload_document = (By.XPATH, '//*[@ng-click="upload()"]')

    def attach_documents_tender(self, doc_of_value, doc_type, data, file_path):
        click, wait_and_click = self.click, self.wait_clickable_and_click
        select = self.select
        select_value, select_text = self.select_value, self.select_text
        click(self.add_document)
        select_value(select(name='documentOf'), doc_of_value)
        if doc_of_value == 'lot':
            select_text(select(name='relatedItem'), data.lot_title(0))
        elif doc_of_value == 'item':
            select_text(select(name='relatedItem'), data.item_description(0))
        select_value(select(name='documentType'), doc_type)
        self.time_out(1)
        click(self.upload_button)
        self.close_desctop_window()
        self.upload_file(self.input_file, file_path)
        click(self.upload_document)
        self.wait_invisibility_element(self.upload_document)


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




