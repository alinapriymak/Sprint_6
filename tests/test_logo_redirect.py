import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from utils.urls import BASE_URL


@allure.feature("Переход по логотипам")
class TestLogoRedirect:

    @allure.title("Переход на главную страницу при клике на логотип Самоката")
    def test_scooter_logo_redirect(self, driver):

        home_page = HomePage(driver)
        home_page.open_base_url() 
        home_page.click_scooter_logo()
        
        assert home_page.check_main_page_url(), "Ошибка перехода на главную страницу"

    @allure.title("Переход на Дзен при клике на логотип Яндекса")
    def test_yandex_logo_redirect(self, driver):
        
        home_page = HomePage(driver)
        home_page.open_base_url() 
        home_page.click_yandex_logo_and_switch_to_new_window()
        
        assert "dzen.ru" in home_page.get_current_url(), \
            "Ошибка перехода на Дзен"
        
        home_page.close_current_window_and_switch_back()
        