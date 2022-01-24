from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import unittest
from Pages.PatientRegister import PatientRegister
from Pages.LoginPage import LoginPage
import HtmlTestRunner


class PatientRegisterTest(unittest.TestCase):
    
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    
    def test_patient_register(self):
        driver = self.driver
        driver.get("http://18.220.234.108:3000/")
        time.sleep(2)
        reg = LoginPage(driver)
        reg.registerclick()
        time.sleep(2)        
        patreg = PatientRegister(driver)
        patreg.patient_select()
        patreg.name_enter("Kattappa")
        patreg.age_enter("55")
        patreg.address_enter("Andhra Pradesh")
        patreg.email_enter("kattappa@gmail.com")
        patreg.contact_enter("9876546897")
        patreg.password_enter("rajmaata")
        patreg.registerclick()
        time.sleep(2)
        
    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/i1637/Desktop/Frontcopy1/Reports"))