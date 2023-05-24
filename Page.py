from Locator import *
from Element import BasePageElement


class NameTextElement(BasePageElement):
    locator = "name"


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def is_title_matches(self):
        return "Workshop" in self.driver.title

    def click_list_button(self):
        element = self.driver.find_element(*MainPageLocator.LIST_BUTTON)
        element.click()

    def click_add_button(self):
        element = self.driver.find_element(*MainPageLocator.ADD_BUTTON)
        element.click()


class ListPage(BasePage):

    def is_showbutton_exists(self):
        element = self.driver.find_element(*ListPageLocator.SHOW_BUTTON)
        return element.is_displayed()


class AddPage(BasePage):

    name_text_element = NameTextElement()

