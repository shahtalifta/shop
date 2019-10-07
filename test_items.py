from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


class TestShop:
    def test_running_auto_tests_for_different_interface_languages(self, browser):
        browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        button_basket = WebDriverWait(browser, 3).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#add_to_basket_form > button[type=\'submit\']")))
        assert button_basket

        time.sleep(30)
