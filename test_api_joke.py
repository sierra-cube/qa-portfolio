import requests

response = requests.get("https://api.chucknorris.io/jokes/random")

if response.status_code == 200:
	print("Тест пройден - сервер ответил 200")
else:
	print("Тест провален - статус:", response.status_code)

data = response.json()
if "value" in data:
	print("Тест пройден - поле value существует")
else:
	print("Тест провален - поле value отсутствует")
if "id" in data:
	print("Тест пройден - поле id cуществует")
else:
	print("Тест провален - поле id отсутствует")