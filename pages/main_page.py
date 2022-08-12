import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements
from locators import Main_Page_Locators


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://minifreemarket.com/'

        super().__init__(web_driver, url)

    # Main LOGO.
    logo = WebElement(LOGO_BTN)
    
    help = WebElement(HELP_BTN)
    

    # Search button
    #search_run_button = WebElement(xpath='//button[@type="submit"]')
