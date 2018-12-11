from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import pyautogui


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def go(self, url):
        self.driver.get(url)
        return self

    def element(self, locator):
        return self.driver.find_element(*locator)

    def elements(self, locator):
        return self.driver.find_elements(*locator)

    def fill(self, locator, value=None):
        element = self.element(locator)
        element.clear()
        element.send_keys(value)

    def fill_last_element(self, locator, value=None):
        element = self.elements(locator)[-1]
        element.clear()
        element.send_keys(value)

    def click(self, locator):
        self.element(locator).click()

    def click_last_element(self, locator):
        self.elements(locator)[-1].click()

    def focus_element(self, locator):
        script = 'arguments[0].scrollIntoView(false)'
        element = self.element(locator)
        self.driver.execute_script(script, element)
        return self

    def get_element_text(self, locator):
        return self.element(locator).text

    def wait_clickable_and_click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.click(locator)

    def wait_visibility_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def wait_invisibility_element(self, locator):
        WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located(locator))

    def fill_date(self, locator, value=None):
        script = 'arguments[0].removeAttribute("readonly")'
        element = self.elements(locator)[-1]
        self.driver.execute_script(script, element)
        element.clear()
        element.send_keys(value)

    def close_desctop_window(self):
        pyautogui.press('esc')

    def upload_file(self, locator, file_path):
        script = \
            'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";'
        element = self.elements(locator)[-1]
        self.driver.execute_script(script, element)
        element.send_keys(file_path)

    def select_value(self, locator, value):
        return Select(self.element(locator)).select_by_value(value)

    def select_last_value(self, locator, value):
        return Select(self.elements(locator)[-1]).select_by_value(value)

    def select_text(self, locator, text):
        return Select(self.element(locator)).select_by_visible_text(text)

    def time_out(self, sec):
        import time
        time.sleep(sec)
