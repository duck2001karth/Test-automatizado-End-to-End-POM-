import unittest
from selenium import webdriver

class Base(unittest.TestCase):
    driver = webdriver.Firefox()

    @classmethod
    def setUpClass(cls) -> None:
        driver = cls.driver
        driver.maximize_window()
        driver.implicitly_wait(10)
        return super().setUpClass()
    
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        return super().tearDownClass()
    