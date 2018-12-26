from selenium.webdriver.common.by import By

from .base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # button
    create_menu = (By.ID, "create-menu")
    tender_create = (By.XPATH, "//a[@ng-click='vm.createTender($event)']")
    plan_create = (By.XPATH, "//a[@ui-sref='planning.create']")
    search = (By.XPATH, '//*[@class="buttons-wrapper"]/div[@ng-click="search()"]')
    home = (By.XPATH, '//div/*[@ui-sref="goHome"]')

    # field
    user_name = (By.XPATH, "//*[@class='user-menu-btn__info']/*[@class='ng-binding']")
    search_field = (By.XPATH, '//*[@class="search-field"]/input')

    def go_home(self):
        return self.click(self.home)

    def get_user_name(self):
        return self.get_element_text(self.user_name)

    def select_create(self, create):
        click, wait_and_click = self.click, self.wait_clickable_and_click
        click(self.create_menu)
        wait_and_click(
            self.tender_create if create == 'tender' else self.plan_create)

    def link_tender(self, tender_id):
        return (By.XPATH, '//*[text()="ID: {id}"]'.format(id=tender_id))

    def search_tender(self, tender_id):
        self.go_home()
        self.fill(self.search_field, tender_id)
        self.click(self.search)
        list_tenders = self.elements(self.link_tender(tender_id))
        return list_tenders

    def go_tender(self, tender_id):
        if len(self.elements(self.link_tender(tender_id))) != 1:
            self.search_tender(tender_id)
        self.click(self.link_tender(tender_id))


class SelectProcedureModal(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    procedure_menu = (By.XPATH, "//*[@ng-model='vm.tenderProcedure']")
    single_lot = (By.XPATH, "//md-radio-button[@value='singlelot']")
    multi_lot = (By.XPATH, "//md-radio-button[@value='multilot']")
    create_button = (By.XPATH, "//button[@ng-click='vm.createTender(vm.tenderProcedure, vm.tenderLots)']")

    @classmethod
    def get_select_procedure(cls, name):
        locator = "//md-option[@value='{}']".format(name)
        return (By.XPATH, locator)

    def select_procedure(self, name, lots=True):
        click, wait_and_click = self.click, self.wait_clickable_and_click
        wait_and_click(self.procedure_menu)
        click(self.get_select_procedure(name))
        if name == 'belowThreshold':
            click(self.multi_lot if lots else self.single_lot)
        click(self.create_button)





