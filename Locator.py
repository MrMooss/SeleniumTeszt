from selenium.webdriver.common.by import By


class MainPageLocator(object):
    LIST_BUTTON = (By.LINK_TEXT, "List Reciepes")
    ADD_BUTTON = (By.LINK_TEXT, "Add Reciepe")


class ListPageLocator(object):
    SHOW_BUTTON = (By.CSS_SELECTOR, '.col:first-child .show-recipe-btn')
