# How to run:
#  1) Download geko driver for Chrome here:
#     https://chromedriver.chromium.org/downloads
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
#     python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*




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
    """Появление меню категории при нажании на оноименную кнопку"""
    page = MainPage(web_browser)
    page.CAT_BTN.click()
    assert page.CAT_MNU.is_visible()
    
def test_03_shop_page_visible(web_browser):
    """Проверка загрузки страницы продавцов после нажатия на кнопку продавцы"""
    page = MainPage(web_browser)
    page.SHP_BTN.click()
    assert page.get_current_url() == Conf.shops_url
    
def test_04_sell_page_visible(web_browser):
    """Проверка загрузки страницы подачи объявления о продаже после нажания на кнопку"""
    page = MainPage(web_browser)
    page.SEL_BTN.click()
    assert page.get_current_url() == Conf.sel_url
    
def test_05_change_lang_eng(web_browser):
    """Проверка изменения языка на сайте при смене языка на англ"""
    page = MainPage(web_browser)
    page.ENG_LANG.click()
    assert "Language" in page.LOGO_ENG.text() 
    
def test_06_change_lang_rus(web_browser):
    """Проверка изменения языка на сайте при смене языка на рус"""
    page = MainPage(web_browser)
    page.RUS_LANG.click()
    assert "Язык" in page.LOGO_RUS.text()
    
def test_07_
    
    
    
    
    
    
    
    
    
