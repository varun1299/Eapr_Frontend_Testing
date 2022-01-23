from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import unittest
from Pages.LoginPage import LoginPage
from Pages.adminhome import AdminHome
from Pages.Admin_MedicationSummary import AdminFillMedicationsummary
import HtmlTestRunner


class AdminMedicationSummary(unittest.TestCase):
    
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        
        
    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
   
    def test_admin_medication_summary(self):
        driver=self.driver
        driver.get("http://18.220.234.108:3000/")
        time.sleep(2)
        login = LoginPage(driver)
        login.admin_select()
        login.username_enter("admin@gmail.com")
        login.password_enter("admin")
        login.loginclick()
        time.sleep(3)
        admin = AdminHome(driver)
        admin.admin_patient_email("vedu@gmail.com")
        admin.admin_patient_search()
        time.sleep(4)
        admin.admin_medication_summary()
        time.sleep(5)
        form = AdminFillMedicationsummary(driver)   
        form.fill_medication_item("Pain Killer/Fever Reducer")
        form.fill_medication_name("Dolo 650")
        form.fill_medication_form("Tablet")
        form.final_save_click()
        time.sleep(5)
        
        
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/i1637/Desktop/Frontcopy1/Reports"))



