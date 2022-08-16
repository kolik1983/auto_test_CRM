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
    
def test_02_    
    
