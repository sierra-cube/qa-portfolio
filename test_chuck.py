import requests

def test_статус_код():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    assert response.status_code == 200

def test_поле_value():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    data = response.json()
    assert "value" in data

def test_поле_id():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    data = response.json()
    assert "id" in data