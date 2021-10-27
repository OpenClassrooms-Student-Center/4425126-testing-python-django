from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse


class TestHome(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("tests/functional_tests/chromedriver")

    def tearDown(self):
        self.browser.close()

    def signup(self):
        self.browser.get(self.live_server_url + reverse("signup"))

        fname = self.browser.find_element_by_id("fname")
        fname.send_keys("Ranga")
        lname = self.browser.find_element_by_id("lname")
        lname.send_keys("Gonnage")
        username = self.browser.find_element_by_id("username")
        username.send_keys("rgonnage")
        email = self.browser.find_element_by_id("email")
        email.send_keys("test@test.com")
        password1 = self.browser.find_element_by_id("pass")
        password1.send_keys("ranga12345")
        password2 = self.browser.find_element_by_id("re_pass")
        password2.send_keys("ranga12345")
        agree_term = self.browser.find_element_by_id("agree-term")
        agree_term.click()
        signup = self.browser.find_element_by_id("signup")
        signup.click()

    def signin(self):
        self.signup()

        username = self.browser.find_element_by_id("your_name")
        username.send_keys("rgonnage")
        password = self.browser.find_element_by_id("your_pass")
        password.send_keys("ranga12345")
        signin = self.browser.find_element_by_id("signin")
        signin.click()

    def check_if_element_exists_by_id(self, element):
        try:
            self.browser.find_element_by_id("element")
        except NoSuchElementException:
            return False
        return True

    def test_home_with_logged_user(self):
        self.signin()

        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("home")
        )
        self.assertNotEqual(self.browser.page_source.find("LOGOUT"), -1)

    def test_home_with_not_logged_user(self):
        self.browser.get(self.live_server_url + reverse("home"))
        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("home")
        )
        self.assertNotEqual(self.browser.page_source.find("LOGIN"), -1)
