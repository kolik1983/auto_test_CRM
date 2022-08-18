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
from pages.auth_page import AuthPage
from setting import Conf

def test_01_login_valid_pass_name(web_browser):
  """Проверка входа в систему с валидными данными"""
  page = AuthPage(web_browser)
  page.AUTH_B.send_keys(Conf.correct_login)
  page.PASS_B.send_keys(Conf.correct_pass)
  page.LOG_BTN.click()
  assert page.INF_USR.is_visible and 'Kolik' in page.NIC_USR.text()
  
def test_02_login_with_null_name(web_browser):
  """Попытка войти личный кабинет с пустым полем Ник"""
  page = AuthPage(web_browser)
  page.AUTH_B.send_keys(Conf.null_str)
  page.PASS_B.send_keys(Conf.correct_pass)
  page.LOG_BTN.click()
  assert page.ERR_MSG.is_visible
 
def test_03_login_with_null_pass(web_browser):
  """Попытка войти личный кабинет с пустым полем пароля"""
  page = AuthPage(web_browser)
  page.AUTH_B.send_keys(Conf.correct_login)
  page.PASS_B.send_keys(Conf.null_str)
  page.LOG_BTN.click()
  assert page.ERR_MSG.is_visible
  
def test_04_login_with_null_both(web_browser):
  """Попытка войти личный кабинет с пустым полем пароля и ника"""
  page = AuthPage(web_browser)
  page.AUTH_B.send_keys(Conf.null_str)
  page.PASS_B.send_keys(Conf.null_str)
  page.LOG_BTN.click()
  assert page.ERR_MSG.is_visible
  
  


