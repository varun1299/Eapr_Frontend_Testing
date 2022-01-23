from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import unittest
from Pages.DoctorRegister import DoctorRegister
from Pages.LoginPage import LoginPage
import HtmlTestRunner


class PatientRegisterTest(unittest.TestCase):
    
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        
    def test_doctor_registration(self):
        driver = self.driver
        driver.get("http://18.220.234.108:3000/")
        time.sleep(2)
        reg = LoginPage(driver)
        reg.registerclick()
        time.sleep(2)
        docreg = DoctorRegister(driver)
        docreg.doctor_select()
        docreg.name_enter("Tarunjit Kalra")
        docreg.email_enter("tarun@gmail.com")
        docreg.password_enter("tarara")
        docreg.specialization_enter("Psychiatrist")
        docreg.registerclick()
            
    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/i1637/Desktop/Frontcopy1/Reports"))