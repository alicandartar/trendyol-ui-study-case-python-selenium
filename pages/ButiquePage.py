from selenium.webdriver import ActionChains
import logging
from utils.locators import *
#from utils.users import Users
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

logging.basicConfig(filename='../trendyol-ui-study/logs/logfile.log', format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y:%M:%S %p', level=logging.DEBUG)

class ButiquePage():


    def __init__(self,driver):
        self.driver = driver
        self.choosedStore = Locators.choosedStore
        self.choosedProduct = Locators.chooseProduct
        self.addToBasketButton = Locators.addToBasketButton



    def selectStore(self):
        driver = self.driver
        driver.find_element(*self.choosedStore).click()

    def isProductPageVisible(self):
        driver = self.driver
        try:
            driver.find_element(*self.addToBasketButton)
            logging.info("Product page is visible.")
            return True
        except:
            logging.warning("Product Page Error")
            return False


    def checkProductImagesInStore(self):
        driver = self.driver
        #time.sleep(1)
        timeout = 10
        element_present = EC.presence_of_element_located((By.CLASS_NAME, 'p-card-wrppr'))#wait till exist func
        WebDriverWait(driver, timeout).until(element_present)
        productCount = len(driver.find_elements_by_class_name("p-card-wrppr")) #boutique-product bazı butiklerde ürünler bu class ile geliyor bazılarında farklı.
        print("Bu sayfada" + str(productCount) + "ürün bulunmaktadır.")

        for x in range(1,productCount):
                #elementPath = "div.boutique-product:nth-child(" + str(x) + ") > a:nth-child(1) > div:nth-child(1) > img:nth-child(1)"
                elementPath = "#search-app > div > div > div.srch-prdcts-cntnr > div:nth-child(2) > div > div:nth-child("+str(x)+") > div.p-card-chldrn-cntnr > a > div.image-container > div > img"
                #search-app > div > div > div.srch-prdcts-cntnr > div:nth-child(2) > div > div:nth-child(2) > div.p-card-chldrn-cntnr > a > div.image-container > div > img
                
                mainElem = driver.find_element_by_css_selector(elementPath)
                mainElemSrc = driver.find_element_by_css_selector(elementPath).get_attribute("src")
                mainElemAlt = driver.find_element_by_css_selector(elementPath).get_attribute("alt")
                driver.execute_script("arguments[0].scrollIntoView();", mainElem)
                print(elementPath)
                print(mainElemSrc)
                
                ###Get Element attributes
                productPath = "#search-app > div > div > div.srch-prdcts-cntnr > div:nth-child(2) > div > div:nth-child("+ str(x) +")"
                productTitle = mainElemAlt
                productID = driver.find_element_by_css_selector(productPath).get_attribute("data-id")

                if(mainElemSrc == "/Content/images/defaultThumb.jpg"):
                    logging.error("Fotoğraf yüklenemedi. ProductID : " + productID + " ProductTitle : " + productTitle)
                else:
                    logging.info("Fotoğraf başarıyla görüntülendi. Product ID : " + productID + "ProductTitle : " + productTitle)

    def selectProduct(self):
        driver = self.driver
        product = driver.find_element(*self.choosedProduct)
        driver.execute_script("arguments[0].scrollIntoView();", product)
        product.click()



