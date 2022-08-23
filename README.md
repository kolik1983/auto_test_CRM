# Автотесты для сайта СРМ https://minifreemarket.com/
Тесты проверяют кликабельность и видмость всех элементов шапки на главной странице и работу поисковой строк. Так же часть элементов в подвале. Второй файл с тестами проверяет работу элементов и полей ввода на странице авторизации.
Для запуска используйте:
- при наличие вэб-драйвера в корневом каталоге  
python -m pytest -v --driver Chrome --driver-path C:\Users\erigo\PycharmProjects\auto_test_CRM\tests\test_header_click.py(tests_auth.py)
- при хранении драйвера в отдельной папке - 
python -m pytest -v --driver Chrome --driver-path c:/driver/chromedriver.exe C:\Users\erigo\PycharmProjects\auto_test_CRM\tests\test_header_click.py(tests_auth.py)
