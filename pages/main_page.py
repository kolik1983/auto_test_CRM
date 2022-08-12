import pytest
from pages import MainPage


def test_check_main_search(web_browser):
    """ Make sure main search works fine. """

    page = MainPage(web_browser)

    page.search = 'iPhone 12'
    page.search_run_button.click()

    # Verify that user can see the list of products:
    assert page.products_titles.count() == 48

