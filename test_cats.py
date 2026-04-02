import requests

def test_статус_код():
    response = requests.get("https://catfact.ninja/fact")
    assert response.status_code == 200

def test_поле_fact():
    response = requests.get("https://catfact.ninja/fact")
    data = response.json()
    assert "fact" in data

def test_поле_length():
    response = requests.get("https://catfact.ninja/fact")
    data = response.json()
    assert "length" in data