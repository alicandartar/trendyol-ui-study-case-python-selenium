from selenium.webdriver import ActionChains
import time
from utils.locators import *
#from utils.userCredentials import UserCredentials



class ProductPage():

    def __init__(self,driver):
        self.driver = driver
        self.addToBasketButton = Locators.addToBasketButton


    def addToBasket(self):
        driver = self.driver
        time.sleep(3)
        driver.find_element(*self.addToBasketButton).click()