import requests

response = requests.get("https://catfact.ninja/fact")

if response.status_code == 200:
	print("Тест пройден - сервер ответил 200")
else:
	print("Тест провален - статус:", response.status_code)

data = response.json()
if "fact" in data:
	print("Тест пройден - поле fact существует")
else:
	print("Тест провален - поле fact отсутствует")