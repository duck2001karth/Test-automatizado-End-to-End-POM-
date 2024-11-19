from selenium.webdriver.common.by import By
import unittest
from selenium import webdriver  # Asegúrate de tener instalado Selenium
from pyunitreport import HTMLTestRunner  # Asegúrate de tener instalado pyunitreport

base_url = "https://www.saucedemo.com/"

class HomePage:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.xpath_image_login = "/html/body/div[2]/div[1]"
        self.input_user = "user-name"
        self.input_password = "password"
        self.button = "login-button"
        self.xpath_error = '/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3'
        self.xpath_page_init = '//*[@id="add-to-cart-sauce-labs-bike-light"]'

    def get_page_login(self):
        return self.driver.find_element(By.ID, self.button)

    def get_input_user(self):
        return self.driver.find_element(By.ID, self.input_user)

    def get_input_password(self):
        return self.driver.find_element(By.ID, self.input_password)

    def send_text_user(self, user):
        self.get_input_user().send_keys(user)

    def send_password(self, password):
        self.get_input_password().send_keys(password)

    def click_element(self):
        self.get_page_login().click()

    def get_error(self):
        return self.driver.find_element(By.XPATH, self.xpath_error)

    def get_success_element(self):
        return self.driver.find_element(By.XPATH, self.xpath_page_init)


class TestHomePage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(base_url)
        self.home_page = HomePage(self.driver)

    def test_login_button_present(self):
        """Verifica que el botón de login esté presente en la página."""
        login_button = self.home_page.get_page_login()
        self.assertIsNotNone(login_button)

    def test_invalid_login(self):
        """Verifica que un login inválido muestra un mensaje de error."""
        self.home_page.send_text_user("invalid_user")
        self.home_page.send_password("invalid_password")
        self.home_page.click_element()
        error_element = self.home_page.get_error()
        self.assertTrue(error_element.is_displayed())

    def test_valid_login(self):
        """Verifica que un login válido permita acceder a la página principal."""
        self.home_page.send_text_user("standard_user")
        self.home_page.send_password("secret_sauce")
        self.home_page.click_element()
        success_element = self.home_page.get_success_element()
        self.assertTrue(success_element.is_displayed())

    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reports', report_name='Pruebas de Testing'))
