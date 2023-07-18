from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

from pages.main_page import Main_Page
from pages.monitors_page import Monitors_Page
from pages.filter_game_monitors_page import Filter_Game_Monitors_Page
from pages.personal_account_page import Personal_Account_Page
from pages.pc_page import Pc_Page
from pages.filter_game_pc_page import Filter_Game_Pc_Page
from pages.cart_page import Cart_Page


def test_buy_products(set_up):
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities['pageLoadStrategy'] = 'eager'
    options = Options()
    s = Service(executable_path=r"C:\chromedriver\chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=options, desired_capabilities=capabilities)

    mp = Main_Page(driver)
    mp.join_personal_account()

    pap = Personal_Account_Page(driver)
    pap.authorization()
    pap.back_on_main_page()

    mp.select_monitors()

    mmp = Monitors_Page(driver)
    mmp.select_game_monitors()

    fgmp = Filter_Game_Monitors_Page(driver)
    fgmp.select_hp_omen_monitor()
    fgmp.back_on_main_page()

    mp.select_pc()

    pp = Pc_Page(driver)
    pp.select_game_pc()

    fgpp = Filter_Game_Pc_Page(driver)
    fgpp.select_hp_omen_pc()
    fgpp.select_cart()

    cp = Cart_Page(driver)
    cp.check_basket()
    cp.confirm_the_order()

    time.sleep(5)




