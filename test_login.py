import pytest
from login_page import LoginPage


@pytest.fixture
def login():
    page = LoginPage()
    page.open()
    yield page
    page.close()


def test_успешный_вход(login):
    login.login("tomsmith", "SuperSecretPassword!")
    message = login.get_message()
    assert "You logged into a secure area!" in message


def test_неверный_пароль(login):
    login.login("tomsmith", "wrongpassword")
    message = login.get_message()
    assert "Your password is invalid!" in message


def test_неверный_логин(login):
    login.login("wronguser", "SuperSecretPassword!")
    message = login.get_message()
    assert "Your username is invalid!" in message

def test_пустой_логин(login):
	login.login("", "")
	message = login.get_message()
	assert "Your username is invalid!" in message

def test_пустой_пароль(login):
	login.login("tomsmith", "")
	message = login.get_message()
	assert "Your password is invalid!" in message