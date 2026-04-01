from selenium.webdriver.common.by import By


class OrderPageLocators:
    """Локаторы страницы заказа"""
    
    # Локаторы первого шага формы заказа
    NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    # Локаторы второго шага формы заказа 
    DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    TOMORROW_DATE = (By.XPATH, "//div[contains(@class, 'react-datepicker__day--today')]/following-sibling::div[1]")
    RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-placeholder")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']")
    
    # Модалка подтверждения заказа
    CONFIRM_BUTTON = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Да']")
    SUCCESS_MODAL = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and text()='Заказ оформлен']")
    
    
    # Возвращает локатор конкретной станции
    @staticmethod
    def get_metro_station_option(station_name):
        return (By.XPATH, f"//div[text()='{station_name}']")
    
    # Возвращает локатор для срока аренды
    @staticmethod
    def get_rental_period_option(days):
        return (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{days}']")