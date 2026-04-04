 QA Portfolio — Автоматизация тестирования

## 👤 Обо мне
QA-инженер с навыками ручного и автоматизированного тестирования.
Специализация: Python, Selenium, API-тестирование.

## 🛠️ Технологии
- Python 3.14
- Selenium WebDriver
- pytest + pytest-html + pytest-xdist
- GitHub Actions (CI/CD)
- Page Object Model

## 📁 Структура проекта
my_tests/
test_cats.py      # API тесты — catfact.ninja
test_chuck.py     # API тесты — chucknorris.io
test_login.py     # UI тесты — авторизация
test_wiki.py      # UI тесты — поиск Wikipedia
pages.py          # Page Object — Wikipedia
login_page.py     # Page Object — Login
## 🚀 Как запустить
`bash
# Установить зависимости
pip install selenium pytest pytest-html pytest-xdist requests

# Запустить все тесты
python -m pytest -v

# Запустить с отчётом
python -m pytest -v --html=report.html

# Запустить параллельно
python -m pytest -v -n auto
📊 Результаты
Всего тестов: 15
API тестов: 6
UI тестов: 9
CI/CD: GitHub Actions ✅