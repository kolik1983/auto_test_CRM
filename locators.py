from selenium.webdriver.common.by import By


# Locators from headers main page/
class Main_Page_Locators:
    LOGO_BTN = (By.xpath('//a[@class="logo"]'))
    HELP_BTN = (By.xpath('//a[@class="help"]'))
    FAV_BTN = (By.xpath('//a[contains(text(), "Избранное")]'))
    RUS_LANG = (By.xpath('//a[contains(text(), "RUS")]'))
    ENG_LANG = (By.xpath('//a[contains(text(), "RUS")]'))
    LOGO_RUS = (By.xpath('//div[contains(text(), "Язык")]'))
    LOGO_ENG = (By.xpath('//div[contains(text(), "Language")]'))
    RUB_BTN = (By.xpath('//a[contains(text(), "RUB")]'))
    USD_BTN = (By.xpath('//a[contains(text(), "USD")]'))
    EUR_BTN = (By.xpath('//a[contains(text(), "EUR")]'))
    BST_BTN = (By.xpath('//a[@class="basket"]'))
    CAT_BTN = (By.xpath('//div[@class="item"]'))
    SHP_BTN = (By.xpath('//div[@class="item shops_btn"]'))
    SEL_BTN = (By.xpath('//div[@class="item adadd"]'))
    USR_BTN = (By.xpath('//a[@class="user"]'))
    AUTH_BTN = (By.xpath('//a[@class="login"]'))


# Locators from auth_page.
class Auth_Page_Locators:
    CAB_REG = (By.xpath('//a[contains(text(), "учетную запись")]'))
    AUTH_B = (By.xpath('//input[@name="login_"]'))
    PASS_B = (By.xpath('//input[@name="password_"]'))
    LOG_BTN = (By.xpath('//a[@class="btn submit"]'))
    REG_HR = (By.xpath('//form/a[contains(text(), "Регистрация")]'))
    FGT_HR = (By.xpath('//a[@class="fr"]'))
    VK_BTN = (By.xpath('//a[@class="soc_btn vk"]'))
    FB_BTN = (By.xpath('//a[@class="soc_btn fb"]'))
    YA_BTN = (By.xpath('//a[@class="soc_btn ya"]'))


# Locators from find_bar main page.
class Find_Bar_Locators:
    FND_BAR = (By.xpath('//input[@name="fg_text"]'))
    FND_ = (By.xpath('//a[@class="open_search_cats"]'))
    FND_MNU = (By.xpath('//div[@data-value="/catalog/games-with-miniatures/warhammer-40000"]'))














