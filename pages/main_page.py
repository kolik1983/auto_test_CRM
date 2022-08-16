import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://minifreemarket.com/'

        super().__init__(web_driver, url)

    # Main LOGO.
    LOGO_BTN = WebElement(xpath='//a[@class="logo"]')
    # Help button
    HELP_BTN = WebElement(xpath='//a[@class="help"]')
    # Favorite button
    FAV_BTN = WebElement(xpath='//a[contains(text(), "Избранное")]')
    # Rus lang swich button
    RUS_LANG = WebElement(xpath='//a[contains(text(), "RUS")]')
    # Rus lang switch button
    ENG_LANG = WebElement(xpath='//a[contains(text(), "RUS")]')
    
    LOGO_RUS = WebElement(xpath='//div[contains(text(), "Язык")]')
    LOGO_ENG = WebElement(xpath='//div[contains(text(), "Language")]')
    RUB_BTN = WebElement(xpath='//a[contains(text(), "RUB")]')
    USD_BTN = WebElement(xpath='//a[contains(text(), "USD")]')
    USD_TXT = WebElement(xpath='//div[@class="price"][1]')
    EUR_BTN = WebElement(xpath='//a[contains(text(), "EUR")]')
    EUR_TXT = WebElement(xpath='//div[@class="price"][1]')
    BST_BTN = WebElement(xpath='//a[@class="basket"]')
    CAT_BTN = WebElement(xpath='//div[@class="item"]')
    CAT_MNU = WebElement(xpath='//div[@class="cat_menu"]')
    SHP_BTN = WebElement(xpath='//div[@class="item shops_btn"]')
    SEL_BTN = WebElement(xpath='//div[@class="item adadd"]')
    USR_BTN = WebElement(xpath='//a[@class="user"]')
    AUTH_BTN = WebElement(xpath='//a[@class="login"]')


