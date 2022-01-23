from selenium.webdriver.common.by import By

class DoctorDashboard():
    def __init__(self, driver):
        self.driver = driver
        
        self.patient_mail = "/html/body/div/div[2]/div/div[2]/div[1]/div[2]/input" 
        self.search_patient = "/html/body/div/div[2]/div/div[2]/div[1]/div[3]/div[1]/button"
        self.create_prescription = "/html/body/div/div[2]/div/div[2]/div[1]/div[3]/div[2]/button"
        self.medication_summary= "/html/body/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div[1]/h1"
        self.allergies_intolerances = "/html/body/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div[2]/h1"
        self.problem_list = "/html/body/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div[3]/h1"
        self.immunizations = "/html/body/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div[4]/h1"
        self.history_of_procedures= "/html/body/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div[5]/h1"
        self.medical_devices = "/html/body/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div[6]/h1"
        self.vital_signs = "/html/body/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div[7]/h1"
        self.past_history_of_illness= "/html/body/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div[8]/h1"
        self.pregnancy = "/html/body/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div[9]/h1"
        self.diagnostic_results = "/html/body/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div[10]/h1"
        self.social_history= "/html/body/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div[11]/h1"
        self.plan_of_care = "/html/body/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div[12]/h1"
        self.functional_status = "/html/body/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div[13]/h1"
        self.Advanced_directives= "/html/body/div/div[2]/div/div[3]/div[2]/div[2]/div[2]/div/div[14]/h1"
        self.logout = "/html/body/div/div[2]/div/div[4]/div/button"
        
        
    def enter_patient_email(self, email):
        self.driver.find_element(By.XPATH, self.patient_mail).clear()
        self.driver.find_element(By.XPATH, self.patient_mail).send_keys(email)
        
    def searchpatient_click(self):
        self.driver.find_element(By.XPATH, self.search_patient).click()
                
    def medication_summary_click(self):
        self.driver.find_element(By.XPATH, self.medication_summary).click()
      
