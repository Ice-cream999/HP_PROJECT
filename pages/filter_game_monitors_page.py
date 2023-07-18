import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Filter_Game_Monitors_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# Locators
    filter_hp_omen = "//input[@id='arrFilter_91_2075639259']"
    button_show = "//input[@class='btn btn-themes']"
    buy_hp_omen_25 = "//div[@class='product__list']/div[3]/div[4]/a"
    close_window = "//button[contains(@class,'fancybox-close-small')]//*[name()='svg']"
    button_hp = "//a[@class='header__logo']"

# Getters
    def get_filter_hp_omen(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.filter_hp_omen)))

    def get_button_show(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_show)))

    def get_buy_hp_omen_25(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.buy_hp_omen_25)))

    def get_close_window(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.close_window)))

    def get_button_hp(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_hp)))

# Actions
    def click_filter_hp_omen(self):
        self.get_filter_hp_omen().click()
        print('Click filter hp omen')

    def click_button_show(self):
        self.get_button_show().click()
        print('Click button show')

    def click_buy_hp_omen_25(self):
        self.get_buy_hp_omen_25().click()
        print('Click buy hp omen 25')

    def close_alert(self):
        self.get_close_window().click()
        print('Close window')

    def click_button_hp(self):
        self.get_button_hp().click()

# Methods
    def select_hp_omen_monitor(self):
        self.get_current_url()
        self.assert_url('https://hp-rus.com/catalog/monitory/filter/aspect-is-dlya-igr/apply/')
        self.click_filter_hp_omen()
        self.click_button_show()
        self.click_buy_hp_omen_25()
        self.close_alert()
        self.click_button_hp()
