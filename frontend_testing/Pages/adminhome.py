from selenium.webdriver.common.by import By


class AdminHome():
    def __init__(self, driver):
        self.driver = driver
        
        self.admin_home = "//*[ contains (text(), 'Admin Panel') ]"
        self.patient_email = "/html/body/div/div[2]/div/div[2]/div[1]/div[2]/input"
        self.search_patient_button = "/html/body/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/button"
        self.Add_new_record = "/html/body/div/div[2]/div/div[2]/div[1]/div[3]/div[2]/button"
        self.medication_summary = "/html/body/div/div[2]/div/div[3]/div/div[1]/h3"
        self.allergies_intolerance = "/html/body/div/div[2]/div/div[3]/div/div[2]/h3"
        self.problem_list = "/html/body/div/div[2]/div/div[3]/div/div[3]/h3"
        self.immunizations = "/html/body/div/div[2]/div/div[3]/div/div[4]/h3"
        self.history_of_procedures = "/html/body/div/div[2]/div/div[3]/div/div[5]/h3"
        self.medical_devices = "/html/body/div/div[2]/div/div[3]/div/div[6]/h3"
        self.diagnostic_results = "/html/body/div/div[2]/div/div[3]/div/div[7]/h3"
        self.vital_signs = "/html/body/div/div[2]/div/div[3]/div/div[8]/h3"
        self.past_history_of_illness = "/html/body/div/div[2]/div/div[3]/div/div[9]/h3"
        self.pregnancy = "/html/body/div/div[2]/div/div[3]/div/div[10]/h3"
        self.social_history = "/html/body/div/div[2]/div/div[3]/div/div[11]/h3"
        self.plan_of_care = "/html/body/div/div[2]/div/div[3]/div/div[12]/h3"
        self.functional_status = "/html/body/div/div[2]/div/div[3]/div/div[13]/h3"
        self.Advanced_Directives= "/html/body/div/div[2]/div/div[3]/div/div[14]/h3"
        self.logout_button = "/html/body/div/div[2]/div/div[4]/div/button"

        
        
        
        
        
    def admin_panel(self):
        self.driver.find_element(By.XPATH, self.admin_home)
        
    def admin_patient_email(self, email):
        self.driver.find_element(By.XPATH, self.patient_email).clear()
        self.driver.find_element(By.XPATH, self.patient_email).send_keys(email)
        
    def admin_patient_search(self):    
        self.driver.find_element(By.XPATH, self.search_patient_button).click()
        
    def admin_medication_summary(self):
        self.driver.find_element(By.XPATH, self.medication_summary).click()
        
    
