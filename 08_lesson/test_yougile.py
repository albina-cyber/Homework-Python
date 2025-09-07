import requests


base_url = "http://yougile.com/api-v2"
key = "dWGBENCKUsK71RTx5GIsbmdGWW1FjgrCcie8yDCmLT8gG0-m090DketVABpCfphh"
headers = {"Authorization": f"Bearer {key}"}


# Позитивная проверка на создание проекта
def test_create_project_positive():
    url = base_url + "/projects"
    data = {"title": "Проект 1-Домашнее задание"}
    response = requests.post(url, json=data, headers=headers)
    assert response.status_code == 200


# Негативная проверка на создание
def test_create_project_negative():
    url = "http://yougile.com/api-v2/projects"
    data = {"description": "This is a test project"}
    response = requests.post(url, json=data)
    assert response.status_code == 401


# Позитивная проверка на изменение проекта
def test_update_project_positive():
    url = base_url + "/projects"
    data = {"title": "Проект 1-Домашнее задание"}
    response = requests.post(url, json=data, headers=headers)
    assert response.status_code == 200
    url = base_url + "/projects" + response.json()["id"]
    data = {"title": "Проект 2-Test"}
    response = requests.put(url, json=data, headers=headers)
    assert response.status_code == 200


# Негативная проверка на изменение проекта
def test_update_project_negative():
    url = "http://yougile.com/api-v2/projects/999"
    data = {"name": "Updated Project", "description": "This is an updated project"}
    response = requests.put(url, json=data)
    assert response.status_code == 401


# Позитивная проверка на получение проекта
def test_get_project_positive():
    url = base_url + "/projects"
    data = {"title": "Проект 1-Домашнее задание"}
    response = requests.post(url, json=data, headers=headers)
    assert response.status_code == 200
    response2 = requests.get(url + response.json()["id"], headers=headers)
    assert response2.status_code == 200


# Негативная проверка на получение проекта
def test_get_project_negative():
    url = "http://yougile.com/api-v2/projects/999"
    response = requests.get(url)
    assert response.status_code == 401
