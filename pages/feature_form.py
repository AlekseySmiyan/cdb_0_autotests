from selenium.webdriver.common.by import By

from .base_page import BasePage


class FeatureForm(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # buttons
    feature_form = (By.ID, 'qualityIndicator')
    add_feature_button = (By.XPATH, '//*[@ng-click="addNewField()"]')
    add_option_button = (By.XPATH, '//*[contains(@id, "add-option")]')
    save_feature_button = (By.XPATH, '//*[@ng-click="save()"]')

    def option(self, name):
        return (By.XPATH, '//*[@ng-model="option.{}"]'.format(name))

    def feature_field(self, name):
        return (By.XPATH, '//*[@ng-model="item.{}"]'.format(name))

    def feature_of_select(self, index):
        return (By.NAME, 'featureOf{}'.format(index))

    def related_item_select(self, index):
        return (By.NAME, 'relatedItem{}'.format(index))

    def go_feature_form(self):
        self.click(self.feature_form)

    def add_feature(self, index, data):
        click, fill = self.click_last_element, self.fill_last_element
        fill(self.feature_field('title'), data.feature(index, 'title'))
        fill(self.feature_field('description'), data.feature(index, 'description'))
        self.select_value(self.feature_of_select(index), data.feature(index, 'featureOf'))
        self.select_text(self.related_item_select(index), data.item_description(index))
        for i in range(0, len(data.options(index))):
            self.add_option(data, index, i)
        click(self.save_feature_button)

    def add_option(self, data, index_features, index_option):
        click, fill = self.click, self.fill_last_element
        if index_option > 0:
            click(self.add_option_button)
        fill(self.option('title'), data.option(index_features, index_option, 'title'))
        fill(self.option('value'), str(data.option(index_features, index_option, 'value') * 100))
        fill(self.option('description'), data.option(index_features, index_option, 'description'))