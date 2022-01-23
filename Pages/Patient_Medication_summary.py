from selenium.webdriver.common.by import By

class PatientViewMedicationsummary():
    def __init__(self, driver):
        self.driver = driver
        
        self.painkiller = "/html/body/div/div[2]/div/div[2]/div/h3"
        
    def view_painkiller(self):
        self.driver.find_element(By.XPATH, self.painkiller).click()
        