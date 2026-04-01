from pages.base_page import BasePage
from locators.main_page_locators import HomePageLocators


class HomePage(BasePage):
    
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

    # Клик на логотип Яндекса
    def click_yandex_logo(self):
        self.click_element(HomePageLocators.YANDEX_LOGO)

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