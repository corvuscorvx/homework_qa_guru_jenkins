import pytest
import allure
from conftest import ALL_SIZES
from page_github import GitHubPage

SIZE_IDS = ["Wisecoco", "Acer", "LG", "iPhone 16 Pro", "Samsung Galaxy S25", "Xiaomi"]

@allure.epic("Веб-форма")
@allure.feature("Авторизация на пк")
@allure.story("Пропуск тестов для мобильных устройств")
@allure.title("Позитивный сценарий")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("desktop_driver", ALL_SIZES, indirect=True, ids=SIZE_IDS)
def test_desktop_sign_in_with_skip(desktop_driver):
    page = GitHubPage(desktop_driver)

    page.open()
    page.click_desktop_sign_in()

    assert "login" in page.get_current_url()

@allure.epic("Веб-форма")
@allure.feature("Авторизация на мобильны")
@allure.story("Пропуск тестов для пк")
@allure.title("Позитивный сценарий")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("mobile_driver", ALL_SIZES, indirect=True, ids=SIZE_IDS)
def test_mobile_sign_in_with_skip(mobile_driver):
    page = GitHubPage(mobile_driver)

    page.open()
    page.click_mobile_sign_in()

    assert "login" in page.get_current_url()
