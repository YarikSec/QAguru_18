import pytest
from selene import browser, be, have

@pytest.fixture(autouse=True)
def browser_conf():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    yield
    print("Закрываем браузер!")
    browser.quit()


def test_success_search(browser_conf):
    browser.open('https://ya.ru')
    browser.element('[name="text"]').should(be.blank).type('yashaka/selene').press_enter()
    # browser.element('h1').should(have.text('Подтвердите, что запросы отправляли вы, а не робот'))
    browser.element('[id="search-result"]').should(have.text('User-oriented Web UI browser tests in Python'))

def test_empty_search(browser_conf):
    browser.open('https://ya.ru')
    browser.element('[name="text"]').should(be.blank).type('dsgjenfsdvwe$#').press_enter()
    browser.element('html').should(have.text('Ничего не нашли'))