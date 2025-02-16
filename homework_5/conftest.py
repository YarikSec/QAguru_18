import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(autouse=True, scope="function")
def browser_conf():
    # browser.config.base_url = 'https://demoqa.com'
    # browser.config.type_by_js = True  # в type текст не накликивается по одной букве, а залетает махом

    driver_options = webdriver.FirefoxOptions()
    driver_options.add_argument("--headless")
    driver_options.page_load_strategy = 'eager' # тем где сайт грузится медленно. Это "стратегия eager", которая говорит "не ждать отстающих" (долго грузящихся).
    browser.config.driver_options = driver_options

    browser.config.timeout = 2.0
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    yield

    print("Браузер закрывается, отойдите от компьютера!)")
    browser.quit()