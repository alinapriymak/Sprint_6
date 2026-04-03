from pages.base_page import BasePage
from locators.main_page_locators import HomePageLocators
from utils.urls import BASE_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):

    # Открытие главной страницы
    def open_base_url(self):
        self.driver.get(BASE_URL)

    # Получение текущего URL
    def get_current_url(self):
        return self.driver.current_url
    
     # Проверка, содержит ли URL указанный текст
    def is_url_contains(self, text):
        return text in self.driver.current_url
    
    # Ожидание загрузки блока FAQ
    def wait_for_faq_section(self):
        self.wait_for_element_visible(HomePageLocators.FAQ_QUESTIONS[1])
    
    # Клик на кнопку Заказать в хедере
    def click_order_header_button(self):
        self.click_element(HomePageLocators.ORDER_TOP_BUTTON)

    # Клик на кнопку Заказать в блоке Как это работает
    def click_order_roadmap_button(self):
        self.scroll_to_element(HomePageLocators.ORDER_BOTTOM_BUTTON)
        self.click_element(HomePageLocators.ORDER_BOTTOM_BUTTON)

    # Клик на логотип Самоката
    def click_scooter_logo(self):
        self.click_element(HomePageLocators.SCOOTER_LOGO)

    # Клик на вопрос в FAQ
    def click_faq_question(self, question_number):
        locator = HomePageLocators.FAQ_QUESTIONS[question_number]
        self.scroll_to_element(locator)
        self.click_element_js(locator)

    # Получение текста ответа 
    def check_faq_answer_text(self, question_number):
        locator = HomePageLocators.FAQ_ANSWERS[question_number]
        self.wait_for_element_visible(locator)
        return self.get_text(locator)
    
    # Клик на логотип и переключение на новую вкладку 
    def click_yandex_logo_and_switch_to_new_window(self):
        original_window = self.driver.current_window_handle
        self.click_element(HomePageLocators.YANDEX_LOGO)

        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
    
        self.driver.switch_to.window(self.driver.window_handles[-1])
        
        WebDriverWait(self.driver, 10).until(EC.url_contains("dzen.ru"))
    

    # Проверка, что текущая страница главная
    def check_main_page_url(self):
        return self.driver.current_url == BASE_URL
    
    def close_current_window_and_switch_back(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])



 