from page_object.home_page import HomePage
from page_object import home_page
from selenium_wrapper.base import Base


class TestLogin(Base):

    def test_1_view_page(self):
        driver = self.driver
        driver.get(home_page.base_url)
        element = HomePage(driver).view_page()
        self.assertTrue(element, "not image")

    def test_2_login_failed(self):
        driver = self.driver
        user = "standar_user"
        password = "secret_saucedf"
        HomePage(driver).send_text_user(user)
        HomePage(driver).send_password(password)
        HomePage(driver).click_element()
        error = HomePage(driver).view_error()
        self.assertTrue(error, 'no such element')

    def test_3_login(self):
        driver = self.driver
        HomePage(driver).clear_user_field()
        HomePage(driver).clear_password_field()
        user = "standard_user"
        password = "secret_sauce"
        HomePage(driver).send_text_user(user)
        HomePage(driver).send_password(password)
        HomePage(driver).click_element()
        suced = HomePage(driver).view_suced()
        self.assertTrue(suced, 'no such element')

