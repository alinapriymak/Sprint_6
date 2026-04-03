from pages.base_page import BasePage
from locators.main_page_locators import HomePageLocators
from utils.urls import BASE_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class HomePage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_base_url(self):
        self.driver.get(BASE_URL)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Ожидание загрузки блока FAQ")
    def wait_for_faq_section(self):
        self.wait_for_element_visible(HomePageLocators.FAQ_QUESTIONS[1])
    
    @allure.step("Кликнуть на кнопку Заказать в хедере")
    def click_order_header_button(self):
        self.click_element(HomePageLocators.ORDER_TOP_BUTTON)

    @allure.step("Кликнуть на кнопку Заказать в блоке 'Как это работает'")
    def click_order_roadmap_button(self):
        self.scroll_to_element(HomePageLocators.ORDER_BOTTOM_BUTTON)
        self.click_element(HomePageLocators.ORDER_BOTTOM_BUTTON)

    @allure.step("Кликнуть на логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(HomePageLocators.SCOOTER_LOGO)

    @allure.step("Кликнуть на вопрос FAQ №{question_number}")
    def click_faq_question(self, question_number):
        locator = HomePageLocators.FAQ_QUESTIONS[question_number]
        self.scroll_to_element(locator)
        self.click_element_js(locator)

    @allure.step("Получить текст ответа на вопрос FAQ №{question_number}")
    def check_faq_answer_text(self, question_number):
        locator = HomePageLocators.FAQ_ANSWERS[question_number]
        self.wait_for_element_visible(locator)
        return self.get_text(locator)
    
    @allure.step("Кликнуть на логотип Яндекса и переключиться на новую вкладку")
    def click_yandex_logo_and_switch_to_new_window(self):
        original_window = self.driver.current_window_handle
        self.click_element(HomePageLocators.YANDEX_LOGO)

        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
    
        self.driver.switch_to.window(self.driver.window_handles[-1])
        
        WebDriverWait(self.driver, 10).until(EC.url_contains("dzen.ru"))
    

    @allure.step("Проверить, что текущая страница — главная")
    def check_main_page_url(self):
        return self.driver.current_url == BASE_URL
    
    @allure.step("Закрыть текущую вкладку и вернуться на первую")
    def close_current_window_and_switch_back(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])



 