import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import HtmlTestRunner

class FlipkartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_search_and_add_to_cart(self):
        driver = self.driver
        driver.get("https://www.flipkart.com")
        time.sleep(2)

        # Close login popup
        try:
            close_login = driver.find_element(By.XPATH, "//button[contains(text(), '✕')]")
            close_login.click()
        except:
            print("Login popup did not appear.")

        time.sleep(2)

        # Search for product
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("iPhone 14")
        search_box.submit()
        time.sleep(3)

        # Click on first product
        first_product = driver.find_element(By.XPATH, "//div[@class='_4rR01T']")
        first_product.click()
        time.sleep(3)

        # Switch to new tab
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)

        # Add to cart
        try:
            add_to_cart = driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]")
            add_to_cart.click()
            time.sleep(2)
        except:
            self.fail("Add to cart button not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
