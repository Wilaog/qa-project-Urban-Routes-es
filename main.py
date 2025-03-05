
import time
import data
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from methods import Methods


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    ask_taxi = (By.XPATH, "//button[contains(text(), 'Pedir un taxi')]")
    comfort_option = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")
    phone_field = (By.XPATH, "//div[@class='form']//div[@class='np-button']")
    phone_field_modal = (By.XPATH, "//div[@class='section active']//input[@id='phone']")
    button_phone_modal = (By.XPATH, "//div[@class='buttons']/button[@class='button full']")

    # Boton principal de agregar tarjeta
    card_field = (By.XPATH, "//div[@class='pp-text'][text()='Método de pago']")
    add_card_btn = (By.XPATH, "//div[@class='pp-title'][text()='Agregar tarjeta']")
    # modal de agregar tarjeta
    card_form = (By.XPATH, "//div[@class='section active unusual']//form")
    card_number_input = (By.XPATH, "//div[@class='card-number-input']/input[@type='text']")
    card_code_input = (By.XPATH, "//div[@class='card-code-input']/input[@type='text']")
    add_card_button = (
    By.XPATH, "//div[@class='section active unusual']//button[@class='button full' and text()='Agregar']")
    x_button_card_modal = (By.XPATH, "(//button[@class='close-button section-close'])[3]")
    send_message = (By.XPATH, "//div[@class='form']//input[@id='comment'][@name='comment']")
    checkbox = (By.XPATH, "//div[@class='r-sw']/div[@class='switch']")
    icecream_counter = (By.XPATH, "//div[@class='r-counter']//div[@class='counter-plus']")
    code_sms = (By.ID, "code")
    code_sms_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
    button_taxi = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/button')
    def __init__(self, driver):
        self.driver = driver
        self.methods = Methods()

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def select_comfort_rate(self):
        # Espera a que el elemento sea clicleable
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ask_taxi))
        self.driver.find_element(*self.ask_taxi).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.comfort_option))
        self.driver.find_element(*self.comfort_option).click()

    def fill_phone_number(self, phone_number):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.phone_field))
        phone_button = self.driver.find_element(*self.phone_field)
        phone_button.click()

    def click_phone_modal_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_phone_modal))
        phone_button_modal = self.driver.find_element(*self.button_phone_modal)
        phone_button_modal.click()

    def fill_sms_code(self):
        time.sleep(1)
        code = self.methods.retrieve_phone_code(self.driver)  # Pasando el driver aquí
        self.driver.find_element(*self.code_sms).send_keys(code)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.code_sms_button))
        button_code = self.driver.find_element(*self.code_sms_button)
        button_code.click()

    def click_add_card_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.card_field))
        click_btn = self.driver.find_element(*self.card_field)
        click_btn.click()
        # Esperar a que el elemento de superposición desaparezca
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'overlay')))
        # Hacer clic en el botón "Agregar" después de que desaparezca la superposición
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_card_btn))
        add_card_button = self.driver.find_element(*self.add_card_btn)
        add_card_button.click()

    def fill_card_number(self, card_number):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.card_number_input))
        card_number_input = self.driver.find_element(*self.card_number_input)
        card_number_input.send_keys(card_number)

    def fill_card_code(self, card_code):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.card_code_input))
        card_code_input = self.driver.find_element(*self.card_code_input)
        card_code_input.send_keys(card_code)


    def click_add_button_after_fill(self):
        # Llenar número de tarjeta y código de tarjeta
        self.fill_card_number(data.card_number)
        self.fill_card_code(data.card_code)

        # Simular un cambio de enfoque para activar el botón "Agregar"
        card_code_input = self.driver.find_element(*self.card_code_input)
        card_code_input.send_keys(Keys.TAB)  # Simular presionar la tecla TAB

        # Esperar a que el botón "Agregar" esté activo
        add_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_card_button)
        )

        # Hacer clic en el botón "Agregar"
        add_button.click()

    def click_on_x_in_card_modal(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.x_button_card_modal))
        x_button = self.driver.find_element(*self.x_button_card_modal)
        x_button.click()

    def send_the_message(self, message):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.send_message))
        msg = self.driver.find_element(*self.send_message)
        self.driver.execute_script("arguments[0].click();", msg)
        msg.send_keys(message)
        time.sleep(5)

    def check_checkbox(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.checkbox))
        c_box = self.driver.find_element(*self.checkbox)
        c_box.click()

    def get_icecream(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.icecream_counter))
        icecream = self.driver.find_element(*self.icecream_counter)
        icecream.click()
        time.sleep(2)
        icecream.click()
        time.sleep(5)
    def share_taxi(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.button_taxi))
        tax_button = self.driver.find_element(*self.button_taxi)
        tax_button.click()

