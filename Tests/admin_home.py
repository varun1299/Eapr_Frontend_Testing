from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import unittest
from Pages.LoginPage import LoginPage
from Pages.adminhome import AdminHome
import HtmlTestRunner


class AdminHomePage(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        driver=self.driver
        driver.get("http://18.220.234.108:3000/")
        time.sleep(2)
        login = LoginPage(driver)
        login.admin_select()
        login.username_enter("admin@gmail.com")
        login.password_enter("admin")
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
   
    def test_admin_panel(self):
        driver=self.driver
        admin_panel =  driver.find_element(By.XPATH, ("//*[ contains (text(), 'Admin Panel') ]"))
        print(admin_panel.is_displayed())
        
    def test_search_visible(self):
        driver = self.driver
        patient_search = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[1]/div[2]/input")
        print(patient_search.is_displayed())
        
    def test_searchbutton_visible(self):
        driver = self.driver
        search_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/button")
        print(search_button.is_displayed())
        
    def test_addrecord_visible(self):
        driver = self.driver
        addrecord_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[1]/div[3]/div[2]/button")
        print(addrecord_button.is_displayed())
        
    def test_category_heading_visible(self):
        driver = self.driver
        category_heading = driver.find_element(By.XPATH, ("//*[ contains (text(), 'Choose which category record is to be added:') ]"))
        print(category_heading.is_displayed())
        
    def test_medicationsummary_visible(self):
        driver = self.driver
        view_medsum = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div[1]/h3")
        print(view_medsum.is_displayed())
        
    def test_allergies_visible(self):
        driver = self.driver
        view_allergies = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div[2]/h3")
        print(view_allergies.is_displayed())
        
    def test_problemlist_visible(self):
        driver = self.driver
        view_problemlist = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div[3]/h3")
        print(view_problemlist.is_displayed())
        
    def test_immunizations_visible(self):
        driver = self.driver
        view_immunizations = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div[4]/h3")
        print(view_immunizations.is_displayed())
        
    def test_historyofprocedures_visible(self):
        driver = self.driver
        view_hop = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div[5]/h3")
        print(view_hop.is_displayed())
        
    def test_medicaldevices_visible(self):
        driver = self.driver
        view_md = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div[6]/h3")
        print(view_md.is_displayed())
        
    def test_diagnosticresult_visible(self):
        driver = self.driver
        view_dr = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div[7]/h3")
        print(view_dr.is_displayed())
        
    def test_vitalsigns_visible(self):
        driver = self.driver
        view_vs = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div[8]/h3")
        print(view_vs.is_displayed())
        
    def test_pasthistoryofillness_visible(self):
        driver = self.driver
        view_phoi = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div[9]/h3")
        print(view_phoi.is_displayed())
        
    def test_pregnancy_visible(self):
        driver = self.driver
        view_preg = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div[10]/h3")
        print(view_preg.is_displayed())
        
    def test_socialhistory_visible(self):
        driver = self.driver
        view_sh = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div[11]/h3")
        print(view_sh.is_displayed())
        
    def test_planofcare_visible(self):
        driver = self.driver
        view_poc = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div[12]/h3")
        print(view_poc.is_displayed())
        
    def test_functionalstatus_visible(self):
        driver = self.driver
        view_fs = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div[13]/h3")
        print(view_fs.is_displayed())
        
    def test_advanced_directives_visible(self):
        driver = self.driver
        view_ad = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div[14]/h3")
        print(view_ad.is_displayed())
        
    def test_logout_button_visible(self):
        driver = self.driver
        view_lgout = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[4]/div/button")
        print(view_lgout.is_displayed())
             
        
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/i1637/Desktop/Frontcopy1/Reports"))