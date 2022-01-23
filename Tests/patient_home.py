from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import unittest
from Pages.LoginPage import LoginPage
import HtmlTestRunner


class PatientHome(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        driver = cls.driver
        driver.get("http://18.220.234.108:3000/")
        time.sleep(2) 
        login = LoginPage(driver)
        login.patient_select()
        login.username_enter("vedu@gmail.com")
        login.password_enter("1234")
        login.loginclick()
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
    
    def test_patient_panel(self):
        driver=self.driver
        patient_panel = driver.find_element(By.XPATH, ("//*[ contains (text(), 'Patient Dashboard') ]"))
        print(patient_panel.is_displayed())
        
    def test_basicinfo_heading_visible(self):
        driver = self.driver
        view_bih = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div/h2")
        print(view_bih.is_displayed())
        
    def test_name_visible(self):
        driver = self.driver
        view_name = driver.find_element(By.XPATH, ("//*[ contains (text(), 'Patient Name') ]"))
        print(view_name.is_displayed())
        
    def test_age_visible(self):
        driver = self.driver
        view_age = driver.find_element(By.XPATH, ("//*[ contains (text(), 'Patient Age') ]"))
        print(view_age.is_displayed())
        
    def test_contact_visible(self):
        driver = self.driver
        view_contact = driver.find_element(By.XPATH, ("//*[ contains (text(), 'Patient Contact') ]"))
        print(view_contact.is_displayed())
        
    def test_address_visible(self):
        driver = self.driver
        view_address = driver.find_element(By.XPATH, ("//*[ contains (text(), 'Patient Address') ]"))
        print(view_address.is_displayed())
        
    def test_previous_prescriptions_visible(self):
        driver = self.driver
        view_ppres = driver.find_element(By.XPATH, ("//*[ contains (text(), 'Previous Prescriptions') ]"))
        print(view_ppres.is_displayed())
        
    def test_previous_medicalrecord_heading_visible(self):
        driver = self.driver
        view_pmedrec = driver.find_element(By.XPATH, ("//*[ contains (text(), 'Previous Medical Record') ]"))
        print(view_pmedrec.is_displayed())
        
    def test_medicationsummary_visible(self):
        driver = self.driver
        view_medsum = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[1]/h1")
        print(view_medsum.is_displayed())
        
    def test_allergies_visible(self):
        driver = self.driver
        view_allergies = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[2]/h1")
        print(view_allergies.is_displayed())
        
    def test_problemlist_visible(self):
        driver = self.driver
        view_problemlist = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[3]/h1")
        print(view_problemlist.is_displayed())
        
    def test_immunizations_visible(self):
        driver = self.driver
        view_immunizations = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[4]/h1")
        print(view_immunizations.is_displayed())
        
    def test_historyofprocedures_visible(self):
        driver = self.driver
        view_hop = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[5]/h1")
        print(view_hop.is_displayed())
        
    def test_medicaldevices_visible(self):
        driver = self.driver
        view_md = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[6]/h1")
        print(view_md.is_displayed())
        
    def test_diagnosticresult_visible(self):
        driver = self.driver
        view_dr = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[10]/h1")
        print(view_dr.is_displayed())
        
    def test_vitalsigns_visible(self):
        driver = self.driver
        view_vs = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[7]/h1")
        print(view_vs.is_displayed())
        
    def test_pasthistoryofillness_visible(self):
        driver = self.driver
        view_phoi = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[8]/h1")
        print(view_phoi.is_displayed())
        
    def test_pregnancy_visible(self):
        driver = self.driver
        view_preg = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[9]/h1")
        print(view_preg.is_displayed())
        
    def test_socialhistory_visible(self):
        driver = self.driver
        view_sh = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[11]/h1")
        print(view_sh.is_displayed())
        
    def test_planofcare_visible(self):
        driver = self.driver
        view_poc = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[12]/h1")
        print(view_poc.is_displayed())
        
    def test_functionalstatus_visible(self):
        driver = self.driver
        view_fs = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[13]/h1")
        print(view_fs.is_displayed())
        
    def test_advanced_directives_visible(self):
        driver = self.driver
        view_ad = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[14]/h1")
        print(view_ad.is_displayed())
        
    def test_logout_button_visible(self):
        driver = self.driver
        view_lgout = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/button")
        print(view_lgout.is_displayed())
             
        
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/i1637/Desktop/Frontcopy1/Reports"))

        
        
