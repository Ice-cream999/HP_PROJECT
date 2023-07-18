
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Cart_Page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# Locators
    button_order = "//a[@class='button-link ']"
    basket_item_1_name = "//div[@class='basket']/div[2]/div[1]/a/div[2]"
    basket_item_1_number = "//div[@class='basket']/div[2]/div[5]/div/span"
    basket_item_2_name = "//div[@class='basket']/div[3]/div[1]/a/div[2]"
    basket_item_2_number = "//div[@class='basket']/div[3]/div[5]/div/span"

# Getters
    def get_button_order(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_order)))

    def get_basket_item_1_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.basket_item_1_name)))

    def get_basket_item_2_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.basket_item_2_name)))

    def get_basket_item_1_number(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.basket_item_1_number)))

    def get_basket_item_2_number(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.basket_item_2_number)))


# Actions
    def click_button_order(self):
        self.get_button_order().click()

    def check_item_1(self, expected_name, expected_number):
        assert self.get_basket_item_1_name().text == expected_name
        assert self.get_basket_item_1_number().text == expected_number
        print(expected_name + ' ' + expected_number + ' ' + 'CORRECT')

    def check_item_2(self, expected_name, expected_number):
        assert self.get_basket_item_2_name().text == expected_name
        assert self.get_basket_item_2_number().text == expected_number
        print(expected_name + ' ' + expected_number + ' ' + 'CORRECT')


# Methods
    def check_basket(self):
        self.get_current_url()
        self.assert_url('https://hp-rus.com/cart/')
        self.check_item_1('HP OMEN 25', '1')
        self.check_item_2('Omen GT13-1154 Tower', '1')

    def confirm_the_order(self):
        self.click_button_order()

