from selenium.webdriver.common.by import By

class DoctorViewMedicationSummary():
    def __init__(self, driver):
        self.driver = driver
        
        self.docpainkiller = "/html/body/div/div[2]/div/div[2]/div/h3"
        
    def view_pain_killer(self):
        self.driver.find_element(By.XPATH, self.docpainkiller).click()

        
        