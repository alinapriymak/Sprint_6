import pytest
import time
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from utils.urls import BASE_URL


@pytest.fixture(scope="function")
def driver():
    """Фикстура для запуска Firefox с гарантированным закрытием"""
    options = Options()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    
    options.set_preference("browser.sessionstore.resume_from_crash", False)
    options.set_preference("browser.startup.page", 0)
    
    service = Service("/usr/local/bin/geckodriver")
    driver = webdriver.Firefox(service=service, options=options)
    

    # Закрытие браузера при упавшем тесте
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
        
        time.sleep(1)
        os.system("killall geckodriver 2>/dev/null")
        os.system("killall firefox 2>/dev/null")
        print("=== Firefox должен быть закрыт ===")