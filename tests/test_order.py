import allure
from pages.home_page import HomePage
from pages.order_page import OrderPage
from utils.order_data_generator import generate_order_data
from utils.urls import BASE_URL


@allure.feature("Заказ самоката")
class TestOrder:

    @allure.title("Заказ самоката через кнопку в хедере")
    def test_positive_order_header_button(self, driver):
     
        home_page = HomePage(driver)
        home_page.open_base_url() 
        
        user_data = generate_order_data()
       
        home_page.click_order_header_button()
        
        order_page = OrderPage(driver)
        result = order_page.complete_order_flow(user_data)
        
        allure.attach(
            str(user_data),
            name="Данные заказа",
            attachment_type=allure.attachment_type.TEXT
        )
        
        assert result, "Ошибка создания заказа"


    @allure.title("Заказ самоката через кнопку в блоке Как это работает")
    def test_positive_order_roadmap_button(self, driver):
        
        home_page = HomePage(driver)
        home_page.open_base_url()   
        
        user_data = generate_order_data()
        
        home_page.click_order_roadmap_button()
        
        order_page = OrderPage(driver)
        result = order_page.complete_order_flow(user_data)
        
        allure.attach(
            str(user_data),
            name="Данные заказа",
            attachment_type=allure.attachment_type.TEXT
        )
        
        assert result, "Ошибка создания заказа"