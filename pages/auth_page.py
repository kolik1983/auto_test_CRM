import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://minifreemarket.com/cabinet'

        super().__init__(web_driver, url)

    # Main LOGO.
    LOGO_BTN = WebElement(xpath='//a[@class="logo"]')
