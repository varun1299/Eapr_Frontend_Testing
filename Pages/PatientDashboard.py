from selenium.webdriver.common.by import By

class PatientDashboard():
    def __init__(self, driver):
        self.driver = driver
        
        self.previous_prescrition= "/html/body/div/div[2]/div/div[3]/div[1]/div/div/div/h3"
        self.medication_summary = "/html/body/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[1]/h1"
        self.allergies_intolerance = "/html/body/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[2]/h1"
        self.problem_list= "/html/body/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[3]/h1"
        self.immunizations = "/html/body/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[4]/h1"
        self.history_of_procedures = "/html/body/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[5]/h1"
        self.medical_devices = "/html/body/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[6]/h1"
        self.vital_signs = "/html/body/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[7]/h1"
        self.past_history_of_illness = "/html/body/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[8]/h1"
        self.pregnancy = "/html/body/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[9]/h1"
        self.diagnostic_results = "/html/body/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[10]/h1"
        self.social_history = "/html/body/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[11]/h1"
        self.plan_of_care = "/html/body/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[12]/h1"
        self.functional_status = "/html/body/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[13]/h1"
        self.Advanced_Directives= "/html/body/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div[14]/h1"
        self.logout_button = "/html/body/div/div[2]/div/button"

        
        
        
        
        
    def view_medication_summary(self):
        self.driver.find_element(By.XPATH, self.medication_summary).click()
        
    def view_prescription(self):
        self.driver.find_element(By.XPATH, self.previous_prescrition).click()
        
    def view_allergies(self):
        self.driver.find_element(By.XPATH, self.allergies_intolerance).click()
        
    def view_immunizations(self):
        self.driver.find_element(By.XPATH, self.immunizations).click()
        
    def view_vital_signs(self):
        self.driver.find_element(By.XPATH, self.vital_signs).click()
        
    def log_out(self):
        self.driver.find_element(By.XPATH, self.logout_button).click()
       
        
    
        
    
      
        
        
      
