from pages.ProductPage import ProductPage
from pages.ButiquePage import ButiquePage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from selenium import webdriver
import time
import unittest
from utils.testCases import test_cases

class MasterTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls,browser="firefox"):
        if(browser == "chrome"):
            cls.driver = webdriver.Chrome(executable_path="../trendyol-ui-study/drivers/chromedriver")
        elif(browser == "safari"):
            cls.driver = webdriver.Safari()
        else :
            cls.driver = webdriver.Firefox(executable_path="../trendyol-ui-study/drivers/geckodriver")

        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_homepage_load(self):
        print("\n" + str(test_cases(0)))
        driver = self.driver
        page = HomePage(driver)
        page.openHomePage()
        assert "Trend" in driver.title
    
    def test_02_login_page_load(self):
        print("\n" + str(test_cases(1)))
        driver = self.driver
        page = HomePage(driver)
        page.clickLoginButton()
        assert "/giris" in driver.current_url
        self.assertTrue(page.isLoginPageVisible())


    def test_03_valid_user_login(self):
        print("\n" + str(test_cases(2)))
        driver = self.driver
        page = LoginPage(driver)
        page.user_login()
        time.sleep(5)

    def test_04_check_butique_images(self):
        print("\n" + str(test_cases(3)))
        driver = self.driver
        page = HomePage(driver)
        page.checkButiqueImages()

    def test_05_check_images_in_selected_store(self):
        print("\n" + str(test_cases(4)))
        driver = self.driver
        page =  ButiquePage(driver)
        time.sleep(5)
        page.selectStore()
        page.checkProductImagesInStore()
        

    def test_06_select_product(self):
        print("\n" + str(test_cases(5)))
        driver = self.driver
        page = ButiquePage(driver)
        page.selectProduct()
        self.assertTrue(page.isProductPageVisible())

    def test_07_add_to_basket(self):
        print("\n" + str(test_cases(6)))
        driver = self.driver
        page = ProductPage(driver)
        page.addToBasket()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed")

#if __name__ == '__main__':
#    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../../reports'))