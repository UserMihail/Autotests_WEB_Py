from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

class TestSearchLocators:
    LOCATOR_LOGIN_FILED = (By.XPATH, '//*[@id="login"]/div[1]/label/input')
    LOCATOR_PASS_FILED = (By.XPATH, '//*[@id="login"]/div[2]/label/input')
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, "button")
    LOCATOR_ERROR_FILED = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/h2')
    LOCATOR_TEXT_FILED = (By.XPATH, '//*[@id="app"]/main/nav/a/span')

class OperationsHelper(BasePage):

    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FILED[1]}")
        login_failed = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FILED)
        login_failed.clear()
        login_failed.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FILED[1]}")
        pass_failed = self.find_element(TestSearchLocators.LOCATOR_PASS_FILED)
        pass_failed.clear()
        pass_failed.send_keys(word)

    def clik_login_button(self):
        logging.info("Clik login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).clik()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FILED, time=3)
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FILED[1]}")
        return text

    def get_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_TEXT_FILED, time=3)
        text = text_field.text
        logging.info(f"We find text {text} in field {TestSearchLocators.LOCATOR_TEXT_FILED[1]}")
        return text

