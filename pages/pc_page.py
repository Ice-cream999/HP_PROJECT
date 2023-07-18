from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Pc_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# Locators
    game_pc = "//a[@class='button-link button-link_game jsp']"

# Getters
    def get_game_pc(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.game_pc)))

# Actions
    def click_game_pc(self):
        self.get_game_pc().click()
        print('Click game pc')

# Methods
    def select_game_pc(self):
        self.get_current_url()
        self.assert_url('https://hp-rus.com/menu/nastolnye-pk/')
        self.click_game_pc()
