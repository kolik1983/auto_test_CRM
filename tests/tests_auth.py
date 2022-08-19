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
  
def test_05_login_with_nonvalid_name(web_browser):
  """Проверка входа с невалидным именем"""
  page.AuthPage(web_browser)
  page.AUTH_B.send_keys(Conf.incorrect_login )
  page.PASS_B.send_keys(Conf.correct_pass)
  page.LOG_BTN.click()
  assert page.ERR_MSG.is_visible
  
def test_06_login_with_nonvalid_password(web_browser):
  """Проверка входа с невалидным паролем"""
  page.AuthPage(web_browser)
  page.AUTH_B.send_keys(Conf.correct_login)
  page.PASS_B.send_keys(Conf.digit)
  page.LOG_BTN.click()
  assert page.ERR_MSG.is_visible
  
def test_07_login_with_space_after_valid_name(web_browser):
  """Проверка входа валидным логином и пробелом в конце"""
  page.AuthPage(web_browser)
  page.AUTH_B.send_keys(Conf.key_space_login)
  page.PASS_B.send_keys(Conf.correct_pass)
  page.LOG_BTN.click()
  assert page.ERR_MSG.is_visible
  
def test_08_login_with_space_after_valid_password(web_browser):
  """Проверка входа валидным паролем и пробелом в конце"""
  page.AuthPage(web_browser)
  page.AUTH_B.send_keys(Conf.correct_login)
  page.PASS_B.send_keys(Conf.key_space_passw)
  page.LOG_BTN.click()
  assert page.ERR_MSG.is_visible
  
def test_09_special_symbol(web_browser):
  """Проверка входа при вводе спец. символов в полк пароля"""
  page.AuthPage(web_browser)
  page.AUTH_B.send_keys(Conf.correct_login)
  page.PASS_B.send_keys(Conf.spec_sym)
  page.LOG_BTN.click()
  assert page.ERR_MSG.is_visible
  
def test_10_254_symbol_password(web_browser):
  """Проверка входа при вооде 254 символа """
  page.AuthPage(web_browser)
  page.AUTH_B.send_keys(Conf.correct_login)
  page.PASS_B.send_keys(Conf.spec_sym)
  page.LOG_BTN.click()
  assert page.ERR_MSG.is_visible
  


