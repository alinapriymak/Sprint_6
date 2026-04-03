import pytest
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from utils.urls import BASE_URL

# Путь к geckodriver через переменную окружения
# На Mac можно установить: export GECKODRIVER_PATH=/usr/local/bin/geckodriver
# На Windows: set GECKODRIVER_PATH=C:\path\to\geckodriver.exe
GECKODRIVER_PATH = os.getenv('GECKODRIVER_PATH', '/usr/local/bin/geckodriver')


@pytest.fixture(scope="function")
def driver():
    """Фикстура для запуска Firefox с гарантированным закрытием"""
    options = Options()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    
    options.set_preference("browser.sessionstore.resume_from_crash", False)
    options.set_preference("browser.startup.page", 0)
    
    # Кроссплатформенный способ получения geckodriver
    service = Service(GECKODRIVER_PATH)
    driver = webdriver.Firefox(service=service, options=options)
    
    try:
        driver.get(BASE_URL)
        yield driver
    finally:
        print("\n=== Закрываем Firefox ===")
        try:
            driver.quit()
            print("✓ driver.quit() выполнен успешно")
        except Exception as e:
            print(f"Ошибка при quit(): {e}")
    
        if os.name != 'nt':
            os.system("killall geckodriver 2>/dev/null")
            os.system("killall firefox 2>/dev/null")
        print("=== Firefox должен быть закрыт ===")