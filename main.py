import unittest
from selenium import webdriver
import Page


class RecipebrowserAzureShowButton(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://recipebrowser.azurewebsites.net")

    def test_title(self):
        mainPage = Page.MainPage(self.driver)
        assert mainPage.is_title_matches()


    def test_name_add(self):
        mainPage = Page.MainPage(self.driver)
        mainPage.click_add_button()
        addPage = Page.AddPage(self.driver)
        addPage.name_text_element = "test"
        assert addPage.name_text_element == "test"


    def test_listrecipes_showbutton_exists(self):
        mainPage = Page.MainPage(self.driver)
        mainPage.click_list_button()
        listPage = Page.ListPage(self.driver)
        assert listPage.is_showbutton_exists()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
