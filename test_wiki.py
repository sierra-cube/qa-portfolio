import pytest
from pages import WikipediaPage

@pytest.fixture
def wiki():
	page = WikipediaPage()
	page.open()
	yield page
	page.close()

def test_поиск_python(wiki):
	wiki.search("Python")
	assert "Python" in wiki.get_title()

def test_поиск_java(wiki):
	wiki.search("Java")
	assert "Java" in wiki.get_title()

def test_поиск_selenium(wiki):
	wiki.search("Selenium")
	assert "Selenium" in wiki.get_title()

def test_поиск_pytest(wiki):
	wiki.search("pytest")
	assert "pytest" in wiki.get_title()