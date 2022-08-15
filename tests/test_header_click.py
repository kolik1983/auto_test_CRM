# How to run:
#  1) Download geko driver for Chrome here:
#     https://chromedriver.chromium.org/downloads
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
#     python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*




import pytest
from pages.main_page import MainPage
from setting import *

def test_check_logo_refresh(web_browser):
    page = MainPage(web_browser)
    page.help.click()
    page.logo.click()
    
    assert url == 'https://minifreemarket.com/'
    assert page.get_current_url() == 'https://minifreemarket.com/'
    

  
  
