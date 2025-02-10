import pytest
from selene import browser


@pytest.fixture(autouse=True, scope="session")
def browser_conf():
    browser.config.window_height = 1366
    browser.config.window_width = 1024
    browser.open('https://ya.ru')
    yield
    print("Закрываем браузер!")
    browser.quit()