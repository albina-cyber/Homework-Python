import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    return driver


def test_fill_and_submit_form(driver):
    driver.maximize_window()
    driver.get
    ("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.CSS_SELECTOR, "input[name=first-name]").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "input[name=last-name]").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, "input[name=address]").send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, "input[name=e-mail]").send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, "input[name=phone]").send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, "input[name=zip-code]").send_keys("")
    driver.find_element(By.CSS_SELECTOR, "input[name=city]").send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, "input[name=country]").send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, "input[name=job-position]").send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, "input[name=company]").send_keys("SkyPro")

    submit_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3")
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)

    submit_button.click()

    new_ids = ["first-name", "last-name", "address", "city", "country", "e-mail", "phone", "job-position", "company"]

    zip_code_presence = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "zip-code")))
    if zip_code_presence:
        zip_code_field = driver.find_element(By.CSS_SELECTOR, "div#zip-code")
        assert "alert-danger" in zip_code_field.get_attribute("class")
        for new_id in new_ids:
            element = driver.find_element(By.ID, new_id)
            assert "alert-success" in element.get_attribute("class")
