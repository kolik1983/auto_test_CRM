# How to run:
#  1) Download geko driver for Chrome here:
#     https://chromedriver.chromium.org/downloads
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
# python -m pytest -v --driver Chrome --driver-path C:\Users\erigo\PycharmProjects\auto_test_CRM\tests\tests_auth.py
# python -m pytest -v --driver Chrome --driver-path c:/driver/chromedriver.exe C:\Users\erigo\PycharmProjects\auto_test_CRM\tests\tests_auth.py

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
  assert page.INF_USR.is_visible and page.NIC_USR.is_visible()

def test_02_login_with_null_name(web_browser):
  """Попытка войти личный кабинет с пустым полем Ник"""
  page = AuthPage(web_browser)
  page.AUTH_B.send_keys(Conf.null_str)
  page.PASS_B.send_keys(Conf.correct_pass)
  page.LOG_BTN.click()
  assert page.ERR_MSG.is_visible()

def test_03_login_with_null_pass(web_browser):
  """Попытка войти личный кабинет с пустым полем пароля"""
  page = AuthPage(web_browser)
  page.AUTH_B.send_keys(Conf.correct_login)
  page.PASS_B.send_keys(Conf.null_str)
  page.LOG_BTN.click()
  assert page.ERR_MSG.is_visible()

def test_04_login_with_null_both(web_browser):
  """Попытка войти личный кабинет с пустым полем пароля и ника"""
  page = AuthPage(web_browser)
  page.AUTH_B.send_keys(Conf.null_str)
  page.PASS_B.send_keys(Conf.null_str)
  page.LOG_BTN.click()
  assert page.ERR_MSG.is_visible()


def test_05_login_with_nonvalid_name(web_browser):
  """Проверка входа с невалидным именем"""
  page = AuthPage(web_browser)
  page.wait_page_loaded()
  page.AUTH_B.send_keys(Conf.incorrect_login)
  page.PASS_B.send_keys(Conf.correct_pass)
  page.LOG_BTN.click()
  assert page.ERR_MSG.is_visible()


def test_06_login_with_not_valid_password(web_browser):
  """Проверка входа с невалидным паролем"""
  page = AuthPage(web_browser)
  page.wait_page_loaded()
  page.AUTH_B.send_keys(Conf.correct_login)
  page.PASS_B.send_keys(Conf.digit)
  page.LOG_BTN.click()
  assert page.ERR_MSG.is_visible()

@pytest.mark.xfail
def test_07_login_with_space_after_valid_name(web_browser):
  """Проверка входа валидным логином и пробелом в конце.  Этот тест нашел баг, фактически сайт принимает такое имя, а должен выдавать ошибку"""
  page = AuthPage(web_browser)
  page.AUTH_B.send_keys(Conf.key_space_login)
  page.PASS_B.send_keys(Conf.correct_pass)
  page.LOG_BTN.click()
  assert page.ERR_MSG.is_visible()


def test_08_login_with_space_after_valid_password(web_browser):
  """Проверка входа валидным паролем и пробелом в конце"""
  page = AuthPage(web_browser)
  page.wait_page_loaded()
  page.AUTH_B.send_keys(Conf.correct_login)
  page.PASS_B.send_keys(Conf.key_space_passw)
  page.LOG_BTN.click()
  assert page.ERR_MSG.is_visible()


def test_09_special_symbol(web_browser):
  """Проверка входа при вводе спец. символов в поле пароля"""
  page = AuthPage(web_browser)
  page.wait_page_loaded()
  page.AUTH_B.send_keys(Conf.correct_login)
  page.PASS_B.send_keys(Conf.spec_sym)
  page.LOG_BTN.click()
  assert page.ERR_MSG.is_visible()


def test_10_251_symbols_password(web_browser):
  """Проверка входа при вводе 251 символа в поле пароля"""
  page = AuthPage(web_browser)
  page.AUTH_B.send_keys(Conf.correct_login)
  page.PASS_B.send_keys(Conf.number_251_pass)
  page.LOG_BTN.click()
  assert page.ERR_MSG.is_visible()


def test_11_252_symbols_password(web_browser):
  """Проверка входа при вводе 252 символов в поле пароля"""
  page = AuthPage(web_browser)
  page.wait_page_loaded()
  page.AUTH_B.send_keys(Conf.correct_login)
  page.PASS_B.send_keys(Conf.number_252_pass)
  page.LOG_BTN.click()
  assert page.ERR_MSG.is_visible()


def test_12_253_symbols_password(web_browser):
  """Проверка входа при вводе больше 252 символов в поле пароля"""
  page = AuthPage(web_browser)
  page.wait_page_loaded()
  page.AUTH_B.send_keys(Conf.correct_login)
  page.PASS_B.send_keys(Conf.more_252_pass)
  page.LOG_BTN.click()
  assert page.ERR_MSG.is_visible()


def test_13_rus_symbols_password(web_browser):
  """Проверка входа при вводе русских букв в поле пароля"""
  page = AuthPage(web_browser)
  page.wait_page_loaded()
  page.AUTH_B.send_keys(Conf.correct_login)
  page.PASS_B.send_keys(Conf.rus_login)
  page.LOG_BTN.click()
  assert page.ERR_MSG.is_visible()


def test_14_rus_symbols_name(web_browser):
  """Проверка входа при вводе русских букв в поле имени"""
  page = AuthPage(web_browser)
  page.wait_page_loaded()
  page.AUTH_B.send_keys(Conf.rus_login)
  page.PASS_B.send_keys(Conf.correct_pass)
  page.LOG_BTN.click()
  assert page.ERR_MSG.is_visible()


def test_15_251_symbols_name(web_browser):
  """Проверка входа при вводе 251 символа в поле имени"""
  page = AuthPage(web_browser)
  page.wait_page_loaded()
  page.AUTH_B.send_keys(Conf.number_251_pass)
  page.PASS_B.send_keys(Conf.correct_pass)
  page.LOG_BTN.click()
  assert page.ERR_MSG.is_visible()


def test_16_252_symbols_name(web_browser):
  """Проверка входа при вводе 252 символов в поле имени"""
  page = AuthPage(web_browser)
  page.wait_page_loaded()
  page.AUTH_B.send_keys(Conf.number_252_pass)
  page.PASS_B.send_keys(Conf.correct_pass)
  page.LOG_BTN.click()
  assert page.ERR_MSG.is_visible()


def test_17_253_symbols_name(web_browser):
  """Проверка входа при вводе больше 252 символов в поле имени"""
  page = AuthPage(web_browser)
  page.wait_page_loaded()
  page.AUTH_B.send_keys(Conf.more_252_pass)
  page.PASS_B.send_keys(Conf.correct_pass)
  page.LOG_BTN.click()
  assert page.ERR_MSG.is_visible()


def test_18_special_symbol(web_browser):
  """Проверка входа при вводе спец. символов в поле имени"""
  page = AuthPage(web_browser)
  page.wait_page_loaded()
  page.AUTH_B.send_keys(Conf.spec_sym)
  page.PASS_B.send_keys(Conf.correct_pass)
  page.LOG_BTN.click()
  assert page.ERR_MSG.is_visible()


def test_19_VK_button(web_browser):
  """Проверка перехода на страницу авторизации через VK"""
  page = AuthPage(web_browser)
  page.VK_BTN.click()
  assert page.get_current_url() == Conf.vk_url


def test_20_FB_button(web_browser):
  """Проверка перехода на страницу авторизации через FB"""
  page = AuthPage(web_browser)
  page.FB_BTN.click()
  assert page.get_current_url() == Conf.fb_url


def test_21_YA_button(web_browser):
  """Проверка перехода на страницу авторизации через YA"""
  page = AuthPage(web_browser)
  page.YA_BTN.click()
  assert page.get_current_url() == Conf.ya_url


def test_22_registration_link(web_browser):
  """Проверка перехода по ссылке регистрация на соответсвующую страницу"""
  page = AuthPage(web_browser)
  page.REG_HR.click()
  assert page.get_current_url() == Conf.reg_url


def test_23_forgoth_pass_link(web_browser):
  """Проверка перехода по ссылке забыли пароль? на страницу регистрации"""
  page = AuthPage(web_browser)
  page.FGT_HR.click()
  assert page.get_current_url() == Conf.fgt_url


def test_24_user_registration_link(web_browser):
  """Проверка перехода по ссылке учетная запись на страницу регистрации"""
  page = AuthPage(web_browser)
  page.CAB_REG.click()
  assert page.get_current_url() == Conf.reg_url

def test_25_login_icon_with_authorization(web_browser):
  """Проверка выпадающего меню профиля при нажатии на кнопку профиля при аутентификации"""
  page = AuthPage(web_browser)
  page.wait_page_loaded()
  page.AUTH_B.send_keys(Conf.correct_login)
  page.PASS_B.send_keys(Conf.correct_pass)
  page.LOG_BTN.click()
  page.USR_BTN.click()
  assert page.PERS_BOX.is_presented()



  
  


