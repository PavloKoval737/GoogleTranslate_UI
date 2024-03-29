from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List

class HomepageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links: str = '#mainNavigationFobs>Ii'
        self.text_button = '//button/span[text()="Текст"]'

    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible('xpath', self.text_button, 'Header Navigation Links')

    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()
        nav_links_text = [link.text for link in nav_links]
        return ",".join(nav_links_text)

