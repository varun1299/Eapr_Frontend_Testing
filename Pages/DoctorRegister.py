from selenium.webdriver.common.by import By

class DoctorRegister():
    def __init__(self, driver):
        self.driver = driver
        
        self.name = "/html/body/div/div[2]/div[2]/div/div[3]/div/div[3]/input"
        self.login_button = "/html/body/div/div[2]/div[2]/div/div[3]/div/a"
        self.email = "/html/body/div/div[2]/div[2]/div/div[3]/div/div[5]/input"
        self.Password = "/html/body/div/div[2]/div[2]/div/div[3]/div/div[7]/input"
        self.Specialization = "/html/body/div/div[2]/div[2]/div/div[3]/div/div[9]/input"
        self.regiser_button = "/html/body/div/div[2]/div[2]/div/div[3]/div/div[10]/div/button"
        self.doctor = "/html/body/div/div[2]/div[2]/div/div[2]/div[1]"
               
        
    def doctor_select(self):
        self.driver.find_element(By.XPATH, self.doctor).click()
        
    def name_enter(self, name):
        self.driver.find_element(By.XPATH, self.name).clear()
        self.driver.find_element(By.XPATH, self.name).send_keys(name)
        
    def email_enter(self, mail):
        self.driver.find_element(By.XPATH, self.email).clear()
        self.driver.find_element(By.XPATH, self.email).send_keys(mail)
        
    def specialization_enter(self, spec):
        self.driver.find_element(By.XPATH, self.Specialization).clear()
        self.driver.find_element(By.XPATH, self.Specialization).send_keys(spec)
        
    def password_enter(self, password):
        self.driver.find_element(By.XPATH, self.Password).clear()
        self.driver.find_element(By.XPATH, self.Password).send_keys(password)
        
    def registerclick(self):
        self.driver.find_element(By.XPATH, self.regiser_button).click()