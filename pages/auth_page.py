import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://minifreemarket.com/cabinet'

        super().__init__(web_driver, url)

    # login string
    CAB_REG = WebElement(xpath='//a[contains(text(), "учетную запись")]')
    # auth bar
    AUTH_B = WebElement(xpath='//input[@name="login_"]')
    # password bar
    PASS_B = WebElement(xpath='//input[@name="password_"]')
    # login button
    LOG_BTN = WebElement(xpath='//a[@class="btn submit"]')
    # user info icon
    INF_USR = WebElement(xpath='//div[@class="seller clearfix"]')
    # user nick
    NIC_USR = WebElement(xpath='//a[@class="login"]')
    # registration button
    REG_HR = WebElement(xpath='//form/a[contains(text(), "Регистрация")]')
    # recovery passw button
    FGT_HR = WebElement(xpath='//a[@class="fr"]')
    # VK button reg
    VK_BTN = WebElement(xpath='//a[@class="soc_btn vk"]')
    # facebook button reg
    FB_BTN = WebElement(xpath='//a[@class="soc_btn fb"]')
    # yandex button reg
    YA_BTN = WebElement(xpath='//a[@class="soc_btn ya"]')
    # error login
    ERR_MSG = WebElement(xpath='//p[@class="error"]')
    # Button user icon
    USR_BTN = WebElement(xpath='//div[@class="user toggle_next"]')
    # box shows user info
    PERS_BOX = WebElement(xpath='//div[@class="user_drop_down"]')
