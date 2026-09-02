import allure
import pytest
from conftest import DESKTOP_SIZES, MOBILE_SIZES
from page_github import GitHubPage

@allure.epic("Веб-форма")
@allure.feature("Авторизация")
@allure.story("Авторизация на пк")
@allure.title("Позитивный сценарий")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("desktop_driver", DESKTOP_SIZES, indirect=True, ids=["Wisecoco", "Acer", "LG"])
def test_desktop_sign_in(desktop_driver):
    page = GitHubPage(desktop_driver)

    page.open()
    page.click_desktop_sign_in()

    assert "login" in page.get_current_url()

@allure.epic("Веб-форма")
@allure.feature("Авторизация")
@allure.story("Авторизация на телефонах")
@allure.title("Позитивный сценарий")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("mobile_driver", MOBILE_SIZES, indirect=True,
                         ids=["iPhone 16 Pro", "Samsung Galaxy S25", "Xiaomi"])
def test_mobile_sign_in(mobile_driver):
    page = GitHubPage(mobile_driver)

    page.open()
    page.click_mobile_sign_in()

    assert "login" in page.get_current_url()
