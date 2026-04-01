import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from utils.urls import BASE_URL


@allure.feature("Переход по логотипам")
class TestLogoRedirect:

    @allure.title("Переход на главную страницу при клике на логотип Самоката")
    def test_scooter_logo_redirect(self, driver):
        driver.get(BASE_URL)
        
        home_page = HomePage(driver)
        home_page.click_scooter_logo()
        
        assert BASE_URL == driver.current_url, "Ошибка перехода на главную страницу"

    @allure.title("Переход на Дзен при клике на логотип Яндекса")
    def test_yandex_logo_redirect(self, driver):
        driver.get(BASE_URL)
        
        home_page = HomePage(driver)
        home_page.click_yandex_logo()
        
        original_window = driver.current_window_handle
        
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

        WebDriverWait(driver, 10).until(
            EC.url_contains("dzen.ru")
        )
        
        assert "dzen.ru" in driver.current_url, \
            "Ошибка перехода на Дзен"
        
        driver.close()
        driver.switch_to.window(original_window)