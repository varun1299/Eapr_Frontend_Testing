from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import unittest
from Pages.LoginPage import LoginPage
from Pages.adminhome import AdminHome
import HtmlTestRunner


class DoctorHome(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        driver=self.driver
        driver.get("http://18.220.234.108:3000/")
        time.sleep(2)
        login = LoginPage(driver)
        login.doctor_select()
        login.username_enter("vishal@gmail.com")
        login.password_enter("1234")
        login.loginclick()
        time.sleep(1)
        
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        
    def test_search_patient(self):
        driver = self.driver
        search_pat = AdminHome(driver)
        search_pat.admin_patient_email("vedu@gmail.com")
        search_pat.admin_patient_search()
        print("Patient Search Completed Successfully")

   
    def test_detailed_medical_recordof_ptient_heading(self):
        driver=self.driver
        view_medrecpat =  driver.find_element(By.XPATH, ("//*[ contains (text(), 'Detailed Medical record of patient') ]"))
        print(view_medrecpat.is_displayed())
        
    def test_search_visible(self):
        driver = self.driver
        patient_search = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[1]/div[2]/input")
        print(patient_search.is_displayed())
        
    def test_searchbutton_visible(self):
        driver = self.driver
        search_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/button")
        print(search_button.is_displayed())
        
    def test_createprescription_visible(self):
        driver = self.driver
        createpres_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[1]/div[3]/div[2]/button")
        print(createpres_button.is_displayed())
        
    def test_category_heading_visible(self):
        driver = self.driver
        category_heading = driver.find_element(By.XPATH, ("//*[ contains (text(), 'Medical Record Categories') ]"))
        print(category_heading.is_displayed())
        
    def test_medicationsummary_visible(self):
        driver = self.driver
        view_medsum = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div[1]/h1")
        print(view_medsum.is_displayed())
        
    def test_allergies_visible(self):
        driver = self.driver
        view_allergies = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/h1")
        print(view_allergies.is_displayed())
        
    def test_problemlist_visible(self):
        driver = self.driver
        view_problemlist = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div[3]/h1")
        print(view_problemlist.is_displayed())
        
    def test_immunizations_visible(self):
        driver = self.driver
        view_immunizations = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div[4]/h1")
        print(view_immunizations.is_displayed())
        
    def test_historyofprocedures_visible(self):
        driver = self.driver
        view_hop = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div[5]/h1")
        print(view_hop.is_displayed())
        
    def test_medicaldevices_visible(self):
        driver = self.driver
        view_md = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div[6]/h1")
        print(view_md.is_displayed())
        
    def test_diagnosticresult_visible(self):
        driver = self.driver
        view_dr = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div[10]/h1")
        print(view_dr.is_displayed())
        
    def test_vitalsigns_visible(self):
        driver = self.driver
        view_vs = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div[7]/h1")
        print(view_vs.is_displayed())
        
    def test_pasthistoryofillness_visible(self):
        driver = self.driver
        view_phoi = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div[8]/h1")
        print(view_phoi.is_displayed())
        
    def test_pregnancy_visible(self):
        driver = self.driver
        view_preg = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div[9]/h1")
        print(view_preg.is_displayed())
        
    def test_socialhistory_visible(self):
        driver = self.driver
        view_sh = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div[11]/h1")
        print(view_sh.is_displayed())
        
    def test_planofcare_visible(self):
        driver = self.driver
        view_poc = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div[12]/h1")
        print(view_poc.is_displayed())
        
    def test_functionalstatus_visible(self):
        driver = self.driver
        view_fs = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div[13]/h1")
        print(view_fs.is_displayed())
        
    def test_advanced_directives_visible(self):
        driver = self.driver
        view_ad = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div[14]/h1")
        print(view_ad.is_displayed())
    
    def test_vitalsigns_heading_visible(self):
        driver = self.driver
        view_vshead = driver.find_element(By.XPATH, ("//*[ contains (text(), 'Vital signs') ]"))
        print(view_vshead.is_displayed())
        
    def test_bodytemp_visible(self):
        driver = self.driver
        view_bodytemp = driver.find_element(By.XPATH, ("//*[ contains (text(), 'Body Temperature:') ]"))
        print(view_bodytemp.is_displayed())
        
    def test_bloodpressure_visible(self):
        driver = self.driver
        view_bloodpressure = driver.find_element(By.XPATH, ("//*[ contains (text(), 'Blood Pressure:') ]"))
        print(view_bloodpressure.is_displayed())
        
    def test_respiration_rate_visible(self):
        driver = self.driver
        view_resr = driver.find_element(By.XPATH, ("//*[ contains (text(), 'Respiration Rate:') ]"))
        print(view_resr.is_displayed())
        
    def test_pulse_rate_visible(self):
        driver = self.driver
        view_pulserate = driver.find_element(By.XPATH, ("//*[ contains (text(), 'Pulse rate:') ]"))
        print(view_pulserate.is_displayed())
        
    def test_bodyweight_visible(self):
        driver = self.driver
        view_bw = driver.find_element(By.XPATH, ("//*[ contains (text(), 'Body Weight:') ]"))
        print(view_bw.is_displayed())
        
    def test_bodymassindex_visible(self):
        driver = self.driver
        view_bmi = driver.find_element(By.XPATH, ("//*[ contains (text(), 'Body Mass Index:') ]"))
        print(view_bmi.is_displayed())
        
    def test_logout_button_visible(self):
        driver = self.driver
        view_lgout = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[4]/div/button")
        print(view_lgout.is_displayed())
             
        
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/i1637/Desktop/Frontcopy1/Reports"))