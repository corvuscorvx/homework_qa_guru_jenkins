import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

DESKTOP_SIZES = [(1280, 720), (1920, 1080), (2560, 1440)]
MOBILE_SIZES = [(402, 874), (360, 780), (394, 875)]
ALL_SIZES = DESKTOP_SIZES + MOBILE_SIZES
DESKTOP_MIN_WIDTH = 1012

DESKTOP_PARAMS = [
    pytest.param((1280, 720), id="Wisecoco"),
    pytest.param((1920, 1080), id="Acer"),
    pytest.param((2560, 1440), id="LG"),
    pytest.param((402, 874), marks=pytest.mark.skip(reason="Мобильное разрешение не подходит для desktop"),
                 id="iPhone 16 Pro"),
    pytest.param((360, 780), marks=pytest.mark.skip(reason="Мобильное разрешение не подходит для desktop"),
                 id="Samsung Galaxy S25"),
    pytest.param((394, 875), marks=pytest.mark.skip(reason="Мобильное разрешение не подходит для desktop"),
                 id="Xiaomi")
]
MOBILE_PARAMS = [
    pytest.param((1280, 720), marks=pytest.mark.skip(reason="Десктопное разрешение не подходит для mobile"),
                 id="Wisecoco"),
    pytest.param((1920, 1080), marks=pytest.mark.skip(reason="Десктопное разрешение не подходит для mobile"),
                 id="Acer"),
    pytest.param((2560, 1440), marks=pytest.mark.skip(reason="Десктопное разрешение не подходит для mobile"),
                 id="LG"),
    pytest.param((402, 874), id="iPhone 16 Pro"),
    pytest.param((360, 780), id="Samsung Galaxy S25"),
    pytest.param((394, 875), id="Xiaomi")
]


def create_driver(width: int, height: int):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(width, height)
    driver.implicitly_wait(5)
    return driver


@pytest.fixture(scope="function")
def desktop_driver(request):
    width, height = request.param

    if width < DESKTOP_MIN_WIDTH:
        pytest.skip(f"Разрешение {width} на {height} не подходит для Desktop")
    driver = create_driver(width, height)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def mobile_driver(request):
    width, height = request.param

    if width >= DESKTOP_MIN_WIDTH:
        pytest.skip(f"Разрешение {width} на {height} не подходит для Mobile")
    driver = create_driver(width, height)
    yield driver
    driver.quit()
