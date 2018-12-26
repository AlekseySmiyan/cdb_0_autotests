from selenium.webdriver.common.by import By

from .base_page import BasePage


class DocumentForm(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    add_document = (By.XPATH, '//*[@ng-click="uploadDocument()"]')
    upload_button = (By.XPATH, '//*[@ng-model="file"]')
    input_file = (By.XPATH, "//input[@type='file']")
    upload_document = (By.XPATH, '//*[@ng-click="upload()"]')

    def select(self, name):
        return (By.XPATH, '//select[@ng-model="document.{}"]'.format(name))

    def attach_documents_tender(self, doc_of_value, doc_type, data, file_path):
        click, wait_and_click = self.click, self.wait_clickable_and_click
        select = self.select
        select_value, select_text = self.select_value, self.select_text
        click(self.add_document)
        select_value(select('documentOf'), doc_of_value)
        if doc_of_value == 'lot':
            select_text(select('relatedItem'), data.lot_title(0))
        elif doc_of_value == 'item':
            select_text(select('relatedItem'), data.item_description(0))
        select_value(select('documentType'), doc_type)
        self.time_out(1)
        click(self.upload_button)
        self.close_desctop_window()
        self.upload_file(self.input_file, file_path)
        click(self.upload_document)
        self.wait_invisibility_element(self.upload_document)