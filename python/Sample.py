import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import HtmlTestRunner

class FlipkartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_search_and_add_to_cart(self):
        driver = self.driver
        driver.get("https://www.flipkart.com")
        wait = WebDriverWait(driver, 15)

        # Close login popup
        try:
            close_login = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '✕')]")))
            close_login.click()
        except:
            print("Login popup did not appear.")

        # Search for product
        search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
        search_box.send_keys("iPhone 14")
        search_box.submit()

        # Wait for results to load and click the first product
        try:
            first_product = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(@href,'/apple-iphone')])[1]")))
            first_product.click()
        except:
            self.fail("Product not found in search results")

        # Switch to new tab
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)

        # Click Add to Cart
        try:
            add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add to cart')]")))
            add_to_cart.click() #asf
            print("✅ Product added to cart.")
        except:
            self.fail("❌ Add to cart button not found or page layout different.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output='D:\\VS code Project'
        )
    )
