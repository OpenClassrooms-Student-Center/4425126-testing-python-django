from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse


class TestAuthentification(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("tests/functional_tests/chromedriver")
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

    def tearDown(self):
        self.browser.close()

    def test_signup(self):
        self.assertEqual(self.browser.find_element_by_tag_name("h2").text, "Log In")
        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("login")
        )

    def test_signin(self):
        username = self.browser.find_element_by_id("your_name")
        username.send_keys("rgonnage")
        password = self.browser.find_element_by_id("your_pass")
        password.send_keys("ranga12345")
        signin = self.browser.find_element_by_id("signin")
        signin.click()

        self.assertEqual(
            self.browser.find_element_by_tag_name("h1").text, "OC-COMMERCE"
        )
        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("home")
        )

    def test_logout(self):
        username = self.browser.find_element_by_id("your_name")
        username.send_keys("rgonnage")
        password = self.browser.find_element_by_id("your_pass")
        password.send_keys("ranga12345")
        signin = self.browser.find_element_by_id("signin")
        signin.click()

        logout = self.browser.find_element_by_xpath("//a[contains(text(), 'LOGOUT')]")
        logout.click()

        self.assertNotEqual(self.browser.page_source.find("LOGIN"), -1)
        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("home")
        )


class TestAuthentificationFailed(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("tests/functional_tests/chromedriver")

    def tearDown(self):
        self.browser.close()

    def test_signup_with_wrong_email(self):
        self.browser.get(self.live_server_url + reverse("signup"))

        fname = self.browser.find_element_by_id("fname")
        fname.send_keys("Ranga")
        lname = self.browser.find_element_by_id("lname")
        lname.send_keys("Gonnage")
        username = self.browser.find_element_by_id("username")
        username.send_keys("rgonnage")
        email = self.browser.find_element_by_id("email")
        email.send_keys("test@testcom")
        password1 = self.browser.find_element_by_id("pass")
        password1.send_keys("ranga12345")
        password2 = self.browser.find_element_by_id("re_pass")
        password2.send_keys("ranga12345")
        agree_term = self.browser.find_element_by_id("agree-term")
        agree_term.click()
        signup = self.browser.find_element_by_id("signup")
        signup.click()

        self.assertNotEqual(
            self.browser.page_source.find("Enter a valid email address."), -1
        )
        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("signup")
        )

    def test_signup_with_two_different_password(self):
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
        password2.send_keys("ranga123456")
        agree_term = self.browser.find_element_by_id("agree-term")
        agree_term.click()
        signup = self.browser.find_element_by_id("signup")
        signup.click()

        self.assertNotEqual(
            self.browser.page_source.find("The two password fields didn’t match."), -1
        )
        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("signup")
        )

    def test_signup_with_same_username(self):
        for i in range(2):
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

        self.assertNotEqual(
            self.browser.page_source.find("A user with that username already exists."),
            -1,
        )
        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("signup")
        )
