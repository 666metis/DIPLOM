import requests
import allure
import pytest


baseURL = 'https://api.kinopoisk.dev/v1.4/'
headers = {
'x-api-key': '1F1KRJW-MJY4T12-PKSWGBQ-H83959E',
'Content-Type': 'application/json'
}


@allure.suite("Заполнение и отправка формы")
@allure.title("Тест отправки формы")
@allure.description(
    "Этот тест проряет заполняемость формы данными и проверяет заполненность каждого поля после отправки"
)
@allure.feature("Форма отправки")
def test_series_id_information():
    with allure.step("Отправить запрос на поиск сериала и получить ответ"):
        response = requests.get(f'{baseURL}movie/727157', headers = headers)
    assert response.status_code == 200

def test_film_id_information():
    with allure.step("Отправить запрос на поиск фильма и получить ответ"):
        response = requests.get(f'{baseURL}movie/263531', headers=headers)
    assert response.status_code == 200

def test_director_id():
    with allure.step("Отправить запрос на поиск режиссера и получить ответ"):
        response = requests.get(f'{baseURL}movie/40182', headers=headers)
    assert response.status_code == 200

def test_non_series():
    with allure.step("Отправить невалидный запрос на поиск сериала и получить ответ"):
        response = requests.get(f'{baseURL}movie/000001', headers=headers)
    assert response.status_code == 400

def test_invalid_name():
    with allure.step("Отправить запрос с невалидным названием и получить ответ"):
        response = requests.get(f'{baseURL}movie/Мст.ти!тели', headers=headers)
    assert response.status_code == 400