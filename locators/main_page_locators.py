from selenium.webdriver.common.by import By


class HomePageLocators:
    """Локаторы главной страницы"""
    
    # Кнопки
    ORDER_TOP_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g")
    ORDER_BOTTOM_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g' and text()='Заказать']")
    
    # Логотипы
    SCOOTER_LOGO = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    YANDEX_LOGO = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    
    # FAQ вопросы и ответы
    FAQ_QUESTIONS = {
        1: (By.ID, "accordion__heading-0"),
        2: (By.ID, "accordion__heading-1"),
        3: (By.ID, "accordion__heading-2"),
        4: (By.ID, "accordion__heading-3"),
        5: (By.ID, "accordion__heading-4"),
        6: (By.ID, "accordion__heading-5"),
        7: (By.ID, "accordion__heading-6"),
        8: (By.ID, "accordion__heading-7"),
    }
    
    FAQ_ANSWERS = {
        1: (By.ID, "accordion__panel-0"),
        2: (By.ID, "accordion__panel-1"),
        3: (By.ID, "accordion__panel-2"),
        4: (By.ID, "accordion__panel-3"),
        5: (By.ID, "accordion__panel-4"),
        6: (By.ID, "accordion__panel-5"),
        7: (By.ID, "accordion__panel-6"),
        8: (By.ID, "accordion__panel-7"),
    }