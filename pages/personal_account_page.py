from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Personal_Account_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# Locators
    field_login = "//table[@class='bx-auth-table']//tr[1]//input"
    field_password = "//table[@class='bx-auth-table']//tr[2]//input"
    button_enter = "//td[@class='authorize-submit-cell']/input"
    button_hp = "//a[@class='header__logo']"

# Getters
    def get_field_login(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.field_login)))

    def get_field_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.field_password)))

    def get_button_enter(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_enter)))

    def get_button_hp(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_hp)))

# Actions
    def input_login(self, login):
        self.get_field_login().send_keys(login)
        print('Input login')

    def input_password(self, password):
        self.get_field_password().send_keys(password)
        print('Input password')

    def click_button_enter(self):
        self.get_button_enter().click()
        print('Click button enter account')

    def click_button_hp(self):
        self.get_button_hp().click()
        print('Back on main page')

# Methods
    def authorization(self):
        self.get_current_url()
        self.assert_url('https://hp-rus.com/auth/')
        self.input_login('ice cream')
        self.input_password('iloveicecream')
        self.click_button_enter()
        self.click_button_hp()
