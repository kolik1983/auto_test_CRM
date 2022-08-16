import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://minifreemarket.com/cabinet'

        super().__init__(web_driver, url)

    #
    CAB_REG = WebElement(xpath='//a[contains(text(), "учетную запись")]')
    AUTH_B = WebElement(xpath='//input[@name="login_"]')
    PASS_B = WebElement(xpath='//input[@name="password_"]')
    LOG_BTN = WebElement(xpath='//a[@class="btn submit"]')
    REG_HR = WebElement(xpath='//form/a[contains(text(), "Регистрация")]')
    FGT_HR = WebElement(xpath='//a[@class="fr"]')
    VK_BTN = WebElement(xpath='//a[@class="soc_btn vk"]')
    FB_BTN = WebElement(xpath='//a[@class="soc_btn fb"]')
    YA_BTN = WebElement(xpath='//a[@class="soc_btn ya"]')
