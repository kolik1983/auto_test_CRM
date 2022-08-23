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
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

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
    time.sleep(5)
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
    assert page.USD_TXT.is_presented()

def test_08_change_currency_eur(web_browser):
    """Проверка изменения валюты при нажатии на EUR """
    page = MainPage(web_browser)
    page.EUR_BTN.click()
    page.EUR_TXT.scroll_to_element()
    assert page.EUR_TXT.is_presented()

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


def test_14_check_find_bar_positive_eng(web_browser):
    """Проверка поисковой строки на англ."""
    page = MainPage(web_browser)
    page.FND_BAR.send_keys(Conf.find_bar_eng)
    keyboard.press(Key.enter)
    assert page.get_current_url() == Conf.necron_url_eng


def test_15_check_find_bar_positive_rus(web_browser):
    """Проверка поисковой строки н русском"""
    page = MainPage(web_browser)
    page.FND_BAR.send_keys(Conf.find_bar_rus)
    keyboard.press(Key.enter)
    assert page.NECRON.is_presented()


def test_16_check_find_bar_special_symb(web_browser):
    """Проверка выдачи сообщения об отсутствие товара после ввода спец.символов"""
    page = MainPage(web_browser)
    page.wait_page_loaded()
    page.FND_BAR.send_keys(Conf.spec_sym)
    keyboard.press(Key.enter)
    assert page.NOT_FIND.is_visible()


def test_17_check_find_bar_253_symb(web_browser):
    """Проверка сообщения об ошибке после ввода больше 252 символов"""
    page = MainPage(web_browser)
    page.wait_page_loaded()
    page.FND_BAR.send_keys(Conf.more_252_pass)
    keyboard.press(Key.enter)
    assert page.NOT_FIND.is_visible()


def test_18_check_find_bar_252_symb(web_browser):
    """Проверка выдачи сообщения об отсутствие товара после ввода 252 символа"""
    page = MainPage(web_browser)
    page.wait_page_loaded()
    page.FND_BAR.send_keys(Conf.number_252_pass)
    keyboard.press(Key.enter)
    assert page.NOT_FIND.is_visible()


def test_19_check_find_bar_251_symb(web_browser):
    """Проверка выдачи сообщения об отсутствие товара после ввода 251 символа"""
    page = MainPage(web_browser)
    page.wait_page_loaded()
    page.FND_BAR.send_keys(Conf.number_251_pass)
    keyboard.press(Key.enter)
    assert page.NOT_FIND.is_visible()


def test_20_heck_find_bar_null_str(web_browser):
    """Проверка выдачи сообщения об отсутствие товара после вводе пустой строки"""
    page = MainPage(web_browser)
    page.wait_page_loaded()
    page.FND_BAR.send_keys(Conf.null_str)
    keyboard.press(Key.enter)
    assert page.get_current_url() == Conf.main_cat_url


def test_21_check_find_bar_digit(web_browser):
    """Проверка выдачи сообщения об отсутствие товара после вводе цифр"""
    page = MainPage(web_browser)
    page.wait_page_loaded()
    page.FND_BAR.send_keys(Conf.digit)
    keyboard.press(Key.enter)
    assert page.NOT_FIND.is_visible()


def test_22_check_category_block(web_browser):
    """Проверка загрузки соответствующей страница при выборе соответствующей категории"""
    page = MainPage(web_browser)
    page.CAT_BTN.click()
    page.CAT_MNU.click()
    page.WHM_BTN.click()
    assert page.get_current_url() == Conf.warh_url

def test_23_check_link_VK_footer(web_browser):
    """Проверка работы ссылки с иконки VK при нажатии на соответсвующую иконку"""
    page = MainPage(web_browser)
    page.wait_page_loaded()
    page.VK_FTR.scroll_to_element()
    page.VK_FTR.click()
    assert page.VK_FTR.is_clickable()

def test_24_check_link_FB_footer(web_browser):
    """Проверка работы ссылки с иконки FB при нажатии на соответсвующую иконку"""
    page = MainPage(web_browser)
    page.wait_page_loaded()
    page.FB_FTR.scroll_to_element()
    page.FB_FTR.click()
    assert page.FB_FTR.is_clickable()

def test_25_check_link_YT_footer(web_browser):
    """Проверка работы ссылки с иконки YOUTUBE при нажатии на соответсвующую иконку"""
    page = MainPage(web_browser)
    page.wait_page_loaded()
    page.YT_FTR.scroll_to_element()
    page.YT_FTR.click()
    assert page.YT_FTR.is_clickable()


