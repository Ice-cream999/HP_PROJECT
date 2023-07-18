
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Filter_Game_Pc_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# Locators
    filter_hp_omen = "//input[@id='arrFilter_91_2359487926']"
    button_show = "//input[@class='btn btn-themes']"
    buy_omen_gt13_1154_tower = "//div[@class='product__list']/div[3]/div[4]/a"
    close_window = "//button[contains(@class,'fancybox-close-small')]//*[name()='svg']"
    cart = "//a[contains(@class,'jsBasketCount')]//*[name()='svg']"


# Getters
    def get_filter_hp_omen(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.filter_hp_omen)))

    def get_button_show(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_show)))

    def get_buy_omen_gt13_1154_tower(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.buy_omen_gt13_1154_tower)))

    def get_close_window(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.close_window)))

    def get_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

# Actions
    def click_filter_hp_omen(self):
        self.get_filter_hp_omen().click()
        print('Click filter PC hp omen')

    def click_button_show(self):
        self.get_button_show().click()
        print('Click button show (PC)')

    def click_buy_omen_gt13_1154_tower(self):
        self.get_buy_omen_gt13_1154_tower().click()
        print('Click buy omen gt13-1154 tower (PC)')

    def close_alert(self):
        self.get_close_window().click()
        print('Close window')

    def click_cart(self):
        self.get_cart().click()
        print('Click cart')

# Methods
    def select_hp_omen_pc(self):
        self.get_current_url()
        self.assert_url('https://hp-rus.com/catalog/kompyutery/filter/aspect-is-dlya-igr/apply/')
        self.click_filter_hp_omen()
        self.click_button_show()
        self.click_buy_omen_gt13_1154_tower()
        self.close_alert()
        self.click_cart()

