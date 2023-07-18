from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_Page(Base):

    url = 'https://hp-rus.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# Locators
    monitors = "//ul[@class='top-menu jsTopMenu']/li[5]"
    pc = "//ul[@class='top-menu jsTopMenu']/li[3]"
    personal_account = "//a[@class='header__panel-item ']"

# Getters
    def get_monitors(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.monitors)))

    def get_personal_account(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.personal_account)))

    def get_pc(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.pc)))

# Actions
    def click_monitors(self):
        self.get_monitors().click()
        print('Click monitors')

    def click_personal_account(self):
        self.get_personal_account().click()

    def click_pc(self):
        self.get_pc().click()

# Methods
    def join_personal_account(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_personal_account()
    def select_monitors(self):
        self.get_current_url()
        self.click_monitors()

    def select_pc(self):
        self.get_current_url()
        self.click_pc()





