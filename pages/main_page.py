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
    ENG_LANG = WebElement(xpath='//a[contains(text(), "ENG")]')
    # Switch rus lang
    LOGO_RUS = WebElement(xpath='//div[contains(text(), "Язык")]')
    # Switch eng lang
    LOGO_ENG = WebElement(xpath='//div[contains(text(), "Language")]')
    # Currency in rub
    RUB_BTN = WebElement(xpath='//a[contains(text(), "RUB")]')
     # Currency in usd
    USD_BTN = WebElement(xpath='//a[contains(text(), "USD")]')
     # Price in specified currency
    USD_TXT = ManyWebElements(xpath='//div[@class="price"][contains(text(), "$")]')
     # Currency in eur
    EUR_BTN = WebElement(xpath='//a[contains(text(), "EUR")]')
    # Price in specified currency
    EUR_TXT = ManyWebElements(xpath='//div[@class="price"][contains(text(), "€")]')
    # Busket button
    BST_BTN = WebElement(xpath='//a[@class="basket"]')
    # Item button
    CAT_BTN = WebElement(xpath='//div[@class="item"]')
    # Cat_mnu
    CAT_MNU = WebElement(xpath='//li/a[contains(text(), "Варгеймы")]')
    # Warhammer 40k button in category menu
    WHM_BTN = WebElement(xpath='//a[@class="btn"][contains(text(), "Warhammer 40.000")]')
    # Category button
    CTG_MNU = WebElement(xpath='//div[@class="cat_menu"]')
    # Shop button
    SHP_BTN = WebElement(xpath='//div[@class="item shops_btn"]')
    # Busket button
    SEL_BTN = WebElement(xpath='//div[@class="item adadd"]')
    # Button user icon
    USR_BTN = WebElement(xpath='//a[@class="user"]')
    # Login/auth button
    AUTH_BTN = WebElement(xpath='//a[@class="login"]')
    # find bar
    FND_BAR = WebElement(xpath='//input[@name="fg_text"]')
    # category menu
    FND_ = WebElement(xpath='//a[@class="open_search_cats"]')
    # category in warhammer 40000
    FND_MNU = WebElement(xpath='//div[@data-value="/catalog/games-with-miniatures/warhammer-40000"]')
    # string negative find
    FND_NEG = WebElement(xpath='//p[contains(text(), "По Вашему запросу ничего не найдено")]')
    # error message
    NOT_FIND = WebElement(xpath='//p[contains(text(), "По Вашему запросу")]')
    # string for find bar test
    NECRON = ManyWebElements(xpath='//a[@class="cat_title"]')
    # footer_link_VK
    VK_FTR = WebElement(xpath='//a[@class="vk"]')
    # footer_link_FB
    FB_FTR = WebElement(xpath='//a[@class="fb"]')
    # footer_link_YT
    YT_FTR = WebElement(xpath='//a[@class="yt"]')


