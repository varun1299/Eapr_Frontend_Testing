from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import unittest
from Pages.LoginPage import LoginPage
from Pages.PatientDashboard import PatientDashboard
from Pages.Patient_Medication_summary import PatientViewMedicationsummary
import HtmlTestRunner


class PatientViewMedicationSummary(unittest.TestCase):
    
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    
    def test_patient_medication_summary(self):
        driver = self.driver
        driver.get("http://18.220.234.108:3000/")
        time.sleep(2)
        
        login = LoginPage(driver)
        login.patient_select()
        login.username_enter("vedu@gmail.com")
        login.password_enter("1234")
        login.loginclick()
        driver.find_element(By.XPATH, ("//*[ contains (text(), 'Patient Dashboard') ]"))
        time.sleep(2)
        pdashboard = PatientDashboard(driver)
        pdashboard.view_medication_summary()
        time.sleep(2)
        pmedrecords = PatientViewMedicationsummary(driver)
        pmedrecords.view_painkiller()
        time.sleep(2)

        

        
    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
        
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/i1637/Desktop/Frontcopy1/Reports"))



