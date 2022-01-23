from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import unittest
from Pages.LoginPage import LoginPage
from Pages.DoctorDashboard import DoctorDashboard
from Pages.Doctor_Medication_Summary import DoctorViewMedicationSummary
import HtmlTestRunner


class Doctor_Medication_Summary(unittest.TestCase):
    
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(2)
        cls.driver.maximize_window()
    
    def test_doctor_medication_summary(self):
        driver = self.driver
        driver.get("http://18.220.234.108:3000/")
        time.sleep(2)
        login = LoginPage(driver)
        login.doctor_select()
        login.username_enter("vishal@gmail.com")
        login.password_enter("1234")
        login.loginclick()
        time.sleep(2)
        doctor = DoctorDashboard(driver)
        doctor.enter_patient_email("vedu@gmail.com")
        doctor.searchpatient_click()
        time.sleep(2)
        doctor.medication_summary_click()
        time.sleep(3)
        medview = DoctorViewMedicationSummary(driver)
        medview.view_pain_killer()
        
    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/i1637/Desktop/Frontcopy1/Reports"))
 