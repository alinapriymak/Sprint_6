from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure


class OrderPage(BasePage):
    
    # Методы первого шага формы заказа

    @allure.step("Заполнить поле Имя")
    def fill_name(self, name):
        self.send_keys_to_element(OrderPageLocators.NAME_FIELD, name)
    
    @allure.step("Заполнить поле Фамилия")
    def fill_surname(self, surname):
        self.send_keys_to_element(OrderPageLocators.SURNAME_FIELD, surname)
    
    @allure.step("Заполнить поле Адрес")
    def fill_address(self, address):
        self.send_keys_to_element(OrderPageLocators.ADDRESS_FIELD, address)
    
    @allure.step("Выбрать станцию метро в выпадающем списке")
    def select_metro_station(self, station_name):
        self.click_element(OrderPageLocators.METRO_STATION_INPUT)
        station_locator = OrderPageLocators.get_metro_station_option(station_name)
        self.click_element(station_locator)
    
    @allure.step("Заполнить поле Телефон")
    def fill_phone(self, phone):
        self.send_keys_to_element(OrderPageLocators.PHONE_FIELD, phone)
    
    @allure.step("Нажать кнопку Далее")
    def click_next_button(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)
    
    def fill_personal_info(self, name, surname, address, metro_station, phone):
        self.fill_name(name)
        self.fill_surname(surname)
        self.fill_address(address)
        self.select_metro_station(metro_station)
        self.fill_phone(phone)
        self.click_next_button()
    
    # Методы второго шага формы заказа

    @allure.step("Выбрать дату в выпадающем календаре")
    def select_date(self):
        self.click_element(OrderPageLocators.DATE_FIELD)
        self.click_element(OrderPageLocators.TOMORROW_DATE)
    
    @allure.step("Выбрать срок аренды в выпадающем списке")
    def select_rental_period(self, days):
        self.click_element(OrderPageLocators.RENTAL_PERIOD)
        rental_locator = OrderPageLocators.get_rental_period_option(days)
        self.click_element(rental_locator)
    
    @allure.step("Выбрать цвет")
    def select_color(self, color):
        if color == "black":
            self.click_element(OrderPageLocators.COLOR_BLACK)
        elif color == "grey":
            self.click_element(OrderPageLocators.COLOR_GREY)
    
    @allure.step("Заполнить поле Комментарий")
    def fill_comment(self, comment):
        self.send_keys_to_element(OrderPageLocators.COMMENT_FIELD, comment)
    
    @allure.step("Нажать кнопку Заказать")
    def click_order_button(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)
    
    @allure.step("Нажать кнопку подтверждения заказа")
    def click_confirm_button(self):
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)
    
    @allure.step("Заполнить персональные данные для заказа")
    def fill_rental_info(self, rental_days, color, comment):
        self.select_date()
        self.select_rental_period(rental_days)
        self.select_color(color)
        self.fill_comment(comment)
        self.click_order_button()
        self.click_confirm_button()
    
    # Методы проверки оформления заказа

    @allure.step("Проверить, что заказ успешно оформлен")
    def is_order_successful(self):
        return self.wait_for_element_visible(OrderPageLocators.SUCCESS_MODAL) is not None
    
    @allure.step("Выполнить полный флоу заказа")
    def complete_order_flow(self, user_data):
        self.fill_personal_info(
            user_data["name"],
            user_data["surname"],
            user_data["address"],
            user_data["metro_station"],
            user_data["phone"]
        )
        self.fill_rental_info(
            user_data["rental_days"],
            user_data["color"],
            user_data["comment"]
        )
        return self.is_order_successful()