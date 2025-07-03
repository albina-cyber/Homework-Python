
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))
driver.maximize_window

# зайти на сайт лабиринт
driver.get("https://www.labirint.ru")

# найти книги по слову Python
search_locator = "#search-field"
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys("Python", Keys.RETURN)

# собрать все карточки товара
books = driver.find_elements(By.CSS_SELECTOR, "div.product-card")

print(len(books))


# вывести в консоль инфо+автор+цена

for book in books:
    try:
        author = book.find_element(By.CSS_SELECTOR,
                                   "div.product-card__author").text

    except NoSuchElementException:
        author = "Автор не указан"
    print(author)


sleep(15)
