import time
import data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from main import UrbanRoutesPage

class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        chrome_options = ChromeOptions()
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'from')))
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_select_comfort_rate(self):
        self.driver.get(data.urban_routes_url)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'from')))
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        # Seleccionar la tarifa Comfort
        routes_page.select_comfort_rate()

    def test_fill_phone_number(self):
        self.driver.get(data.urban_routes_url)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'from')))
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        routes_page.select_comfort_rate()
        time.sleep(2)
        # Llenar número de teléfono
        routes_page.fill_phone_number(data.phone_number)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(routes_page.phone_field_modal))
        phone_input = self.driver.find_element(*routes_page.phone_field_modal)
        phone_input.send_keys(data.phone_number)
        routes_page.click_phone_modal_button()
        time.sleep(2)
        routes_page.fill_sms_code()
        time.sleep(5)

    def test_add_card(self):
        self.test_fill_phone_number()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_add_card_button()
        time.sleep(2)
        routes_page.fill_card_number(data.card_number)
        routes_page.fill_card_code(data.card_code)
        time.sleep(2)
        routes_page.click_add_button_after_fill()
        routes_page.click_on_x_in_card_modal()

    def test_message_to_the_driver(self):
        self.test_add_card()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.send_the_message(data.message_for_driver)

    def test_order_tissues(self):
        self.test_message_to_the_driver()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.check_checkbox()

    def test_two_ice_cream(self):
        self.test_order_tissues()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.get_icecream()


    def test_ask_taxi(self):
        self.test_two_ice_cream()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.share_taxi()
        time.sleep(10)
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()