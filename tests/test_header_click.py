# How to run:
#  1) Download geko driver for Chrome here:
#     https://chromedriver.chromium.org/downloads
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
# python -m pytest -v --driver Chrome --driver-path C:\Users\erigo\PycharmProjects\auto_test_CRM\tests\test_header_click.py
# python -m pytest -v --driver Chrome --driver-path c:/driver/chromedriver.exe C:\Users\erigo\PycharmProjects\auto_test_CRM\tests\test_header_click.py

import pytest
from pages.main_page import MainPage
from setting import Conf


def test_01_check_logo_refresh(web_browser):
    """Проверка возврата на главную странице при нажатие на логотип"""
    page = MainPage(web_browser)
    page.HELP_BTN.click()
    page.LOGO_BTN.click()
    assert page.get_current_url() == Conf.main_url


def test_02_check_category_menu(web_browser):
    """Появление меню категории при нажатии на одноименную кнопку"""
    page = MainPage(web_browser)
    page.CAT_BTN.click()
    assert page.CAT_MNU.is_visible()


def test_03_shop_page_visible(web_browser):
    """Проверка загрузки страницы продавцов после нажатия на кнопку продавцы"""
    page = MainPage(web_browser)
    page.SHP_BTN.click()
    assert page.get_current_url() == Conf.shops_url


def test_04_sell_page_visible(web_browser):
    """Проверка загрузки страницы подачи объявления о продаже после нажатия на кнопку"""
    page = MainPage(web_browser)
    page.SEL_BTN.click()
    assert page.get_current_url() == Conf.sel_url


def test_05_change_lang_eng(web_browser):
    """Проверка изменения языка на сайте при смене языка на англ"""
    page = MainPage(web_browser)
    page.ENG_LANG.click()
    assert "Language" == page.LOGO_ENG.get_text()


def test_06_change_lang_rus(web_browser):
    """Проверка изменения языка на сайте при смене языка на рус"""
    page = MainPage(web_browser)
    page.RUS_LANG.click()
    assert "Язык" == page.LOGO_RUS.get_text()

def test_07_change_currency_usd(web_browser):
    """Проверка изменения валюты при нажатии на USD """
    page = MainPage(web_browser)
    page.USD_BTN.click()
    page.USD_TXT.scroll_to_element()
    assert page.USD_TXT.get_text()

def test_08_change_currency_eur(web_browser):
    """Проверка изменения валюты при нажатии на EUR """
    page = MainPage(web_browser)
    page.EUR_BTN.click()
    page.EUR_TXT.scroll_to_element()
    assert page.EUR_TXT.get_text()

def test_09_basket_link(web_browser):
    """Проверка перехода на страницу корзины при выборе Корзины"""
    page = MainPage(web_browser)
    page.BST_BTN.click()
    assert page.get_current_url() == Conf.bask_url

def test_10_help_link(web_browser):
    """Проверка перехода на страницу помощи при выборе Помощь"""
    page = MainPage(web_browser)
    page.HELP_BTN.click()
    assert page.get_current_url() == Conf.hlp_url

def test_11_favorite_link(web_browser):
    """Проверка перехода на страницу избранного при выборе Избранное"""
    page = MainPage(web_browser)
    page.FAV_BTN.click()
    assert page.get_current_url() == Conf.fvr_url
    
def test_12_login_icon_without_auth(web_browser):
    """Проверка перехода на страницу регистрации без аутентификация"""
    page = MainPage(web_browser)
    page.USR_BTN.click()
    assert page.get_current_url() == Conf.auth_url
    
def test_13_login_reg_button(web_browser):
    """Переход на страницу регистрации при нажатии на Вход/Регистрация"""
    page = MainPage(web_browser)
    page.AUTH_BTN.click()
    assert page.get_current_url() == Conf.auth_url
    
def test_14_check_find_bar(web_browser):
    """Проверка поисковой строки"""
    page = MainPage(web_browser)
    page.FND_BAR.send_keys(Conf.find_bar_eng)
    
    
    
