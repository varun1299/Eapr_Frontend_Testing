from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import unittest
from Pages.LoginPage import LoginPage
from Pages.adminhome import AdminHome
import HtmlTestRunner


class AdminLoginTest(unittest.TestCase):
    
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        
        
    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
   
    def test_admin_login(self):
        driver=self.driver
        driver.get("http://18.220.234.108:3000/")
        time.sleep(2)
        login = LoginPage(driver)
        login.admin_select()
        login.username_enter("admin@gmail.com")
        login.password_enter("admin")
        login.loginclick()
        driver.find_element(By.XPATH, ("//*[ contains (text(), 'Admin Panel') ]"))
        time.sleep(3)
        
        
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/i1637/Desktop/Frontcopy1/Reports"))



