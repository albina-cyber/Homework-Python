from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

cookie = {"name": "cookie_policy", "value": "1"}


def test_card_counter():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().
                                                     install()))
    browser.maximize_window

# Перейти на сайт: labirint.ru

    browser.get("https://www.labirint.ru/")
    browser.implicitly_wait(4)
    browser.add_cookie(cookie)

# Найти все книги по слову Python

    browser.find_element(By.CSS_SELECTOR, "#search-field").send_keys('python')

    sleep(5)

    browser.quit()


# Добавить все книги в корзину.
# Перейти в корзину.
# Проверить, что счетчик товаров соответствует количеству добавленных книг.
