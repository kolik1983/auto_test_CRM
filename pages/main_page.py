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
    # Eng lang switch button
    ENG_LANG = WebElement(xpath='//a[contains(text(), "RUS")]')
    # Switch rus lang
    LOGO_RUS = WebElement(xpath='//div[contains(text(), "Язык")]')
    # Switch eng lang
    LOGO_ENG = WebElement(xpath='//div[contains(text(), "Language")]')
    # Currency in rub
    RUB_BTN = WebElement(xpath='//a[contains(text(), "RUB")]')
     # Currency in usd
    USD_BTN = WebElement(xpath='//a[contains(text(), "USD")]')
     # Price in specified currency
    USD_TXT = WebElement(xpath='//div[@class="price"][1]')
     # Currency in eur
    EUR_BTN = WebElement(xpath='//a[contains(text(), "EUR")]')
    # Price in specified currency
    EUR_TXT = WebElement(xpath='//div[@class="price"][1]')
    # Busket button
    BST_BTN = WebElement(xpath='//a[@class="basket"]')
    # Item button
    CAT_BTN = WebElement(xpath='//div[@class="item"]')
    # Category button
    CAT_MNU = WebElement(xpath='//div[@class="cat_menu"]')
    # Shop button
    SHP_BTN = WebElement(xpath='//div[@class="item shops_btn"]')
    # Busket button
    SEL_BTN = WebElement(xpath='//div[@class="item adadd"]')
    USR_BTN = WebElement(xpath='//a[@class="user"]')
    AUTH_BTN = WebElement(xpath='//a[@class="login"]')


