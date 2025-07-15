
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))
driver.maximize_window


cookie = {"name": "cookie_policy", "value": "1"}


def test_card_counter():
    browser = webdriver.Chrome()


browser.get("https://www.labirint.ru")
browser.implicitly_wait(4)
browser.maximize_window()
browser.add_cookie(cookie)


sleep(5)
