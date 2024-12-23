import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def chrome_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(300)
    yield driver
    driver.quit()

def test_search_name(chrome_browser):
    chrome_browser.get("https://www.kinopoisk.ru/")
    chrome_browser.find_element(By.NAME, "kp_query").send_keys("Мстители")
    chrome_browser.find_element(By.ID, "suggest-item-film-263531").click()
    assert chrome_browser.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text =="Мстители (2012)"

def test_search_name_invalid(chrome_browser):
    chrome_browser.get("https://www.kinopoisk.ru/")
    chrome_browser.find_element(By.NAME, "kp_query").send_keys("Мст!тел№")
    assert chrome_browser.find_element(By.XPATH,"//*[contains(@class, 'emptySuggest')]").text == "По вашему запросу ничего не найдено"

def test_search_english_name(chrome_browser):
    chrome_browser.get("https://www.kinopoisk.ru/")
    chrome_browser.find_element(By.NAME, "kp_query").send_keys("Avengers")
    chrome_browser.find_element(By.ID, "suggest-item-film-843650").click()
    assert chrome_browser.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text =="Мстители: Финал (2019)"

def test_by_valid_symbol(chrome_browser):
    chrome_browser.get("https://www.kinopoisk.ru/")
    chrome_browser.find_element(By.NAME,"kp_query").send_keys("1+1")
    chrome_browser.find_element(By.ID,"suggest-item-film-535341").click()
    assert chrome_browser.find_element(By.CSS_SELECTOR,"span[data-tid='75209b22']").text =="1+1 (2011)"

def test_search_by_actor(chrome_browser):
    chrome_browser.get("https://www.kinopoisk.ru/")
    chrome_browser.find_element(By.NAME,"kp_query").send_keys("Вин Дизель")
    chrome_browser.find_element(By.ID,"suggest-item-person-11437").click()
    assert chrome_browser.find_element(By.CSS_SELECTOR,"h1[data-tid='f22e0093']").text =="Вин Дизель"