from selenium.webdriver.common.by import By

from .base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # button
    create_menu = (By.ID, "create-menu")
    tender_create = (By.XPATH, "//a[@ng-click='vm.createTender($event)']")
    plan_create = (By.XPATH, "//a[@ui-sref='planning.create']")

    # field
    user_name = (By.XPATH, "//*[@class='user-menu-btn__info']/*[@class='ng-binding']")

    def get_user_name(self):
        return self.get_element_text(self.user_name)

    def select_create(self, create):
        click, wait_and_click = self.click, self.wait_clickable_and_click
        click(self.create_menu)
        wait_and_click(
            self.tender_create if create == 'tender' else self.plan_create)


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





