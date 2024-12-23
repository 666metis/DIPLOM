import requests


baseURL = 'https://api.kinopoisk.dev/v1.4/'
headers = {
'x-api-key': '1F1KRJW-MJY4T12-PKSWGBQ-H83959E',
'Content-Type': 'application/json'
}

def test_series_id_information():
    response = requests.get(f'{baseURL}movie/727157', headers = headers)
    assert response.status_code == 200

def test_film_id_information():
    response = requests.get(f'{baseURL}movie/263531', headers=headers)
    assert response.status_code == 200

def test_director_id():
    response = requests.get(f'{baseURL}movie/40182', headers=headers)
    assert response.status_code == 200

def test_non_series():
    response = requests.get(f'{baseURL}movie/000001', headers=headers)
    assert response.status_code == 400

def test_invalid_name():
    response = requests.get(f'{baseURL}movie/Мст.ти!тели', headers=headers)
    assert response.status_code == 400