from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    
    # Методы первого шага формы заказа
    def fill_name(self, name):
        self.send_keys_to_element(OrderPageLocators.NAME_FIELD, name)
    
    def fill_surname(self, surname):
        self.send_keys_to_element(OrderPageLocators.SURNAME_FIELD, surname)
    
    def fill_address(self, address):
        self.send_keys_to_element(OrderPageLocators.ADDRESS_FIELD, address)
    
    def select_metro_station(self, station_name):
        self.click_element(OrderPageLocators.METRO_STATION_INPUT)
        station_locator = OrderPageLocators.get_metro_station_option(station_name)
        self.click_element(station_locator)
    
    def fill_phone(self, phone):
        self.send_keys_to_element(OrderPageLocators.PHONE_FIELD, phone)
    
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
    def select_date(self):
        self.click_element(OrderPageLocators.DATE_FIELD)
        self.click_element(OrderPageLocators.TOMORROW_DATE)
    
    def select_rental_period(self, days):
        self.click_element(OrderPageLocators.RENTAL_PERIOD)
        rental_locator = OrderPageLocators.get_rental_period_option(days)
        self.click_element(rental_locator)
    
    def select_color(self, color):
        if color == "black":
            self.click_element(OrderPageLocators.COLOR_BLACK)
        elif color == "grey":
            self.click_element(OrderPageLocators.COLOR_GREY)
    
    def fill_comment(self, comment):
        self.send_keys_to_element(OrderPageLocators.COMMENT_FIELD, comment)
    
    def click_order_button(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)
    
    def click_confirm_button(self):
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)
    
    def fill_rental_info(self, rental_days, color, comment):
        self.select_date()
        self.select_rental_period(rental_days)
        self.select_color(color)
        self.fill_comment(comment)
        self.click_order_button()
        self.click_confirm_button()
    
    # Методы проверки оформления заказа
    def is_order_successful(self):
        return self.wait_for_element_visible(OrderPageLocators.SUCCESS_MODAL) is not None
    
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