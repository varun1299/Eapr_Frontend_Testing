from selenium.webdriver.common.by import By

class PatientRegister():
    def __init__(self, driver):
        self.driver = driver
        
        self.name = "/html/body/div/div[2]/div[2]/div/div[3]/div/div[3]/input"
        self.age = "/html/body/div/div[2]/div[2]/div/div[3]/div/div[5]/input"
        self.address = "/html/body/div/div[2]/div[2]/div/div[3]/div/div[7]/textarea"
        self.login_button = "/html/body/div/div[2]/div[2]/div/div[3]/div/a"
        self.email = "/html/body/div/div[2]/div[2]/div/div[3]/div/div[9]/input"
        self.Password = "/html/body/div/div[2]/div[2]/div/div[3]/div/div[11]/input"
        self.Contact = "/html/body/div/div[2]/div[2]/div/div[3]/div/div[13]/input"
        self.regiser_button = "/html/body/div/div[2]/div[2]/div/div[3]/div/div[14]/div/button"
        self.patient = "/html/body/div/div[2]/div[2]/div/div[2]/div[2]"
        self.doctor = "/html/body/div/div[2]/div[2]/div/div[2]/div[1]"
               
        
    def patient_select(self):
        self.driver.find_element(By.XPATH, self.patient).click()
        
    # def doctor_select(self):
    #     self.driver.find_element(By.XPATH, self.doctor).click()
        
    def name_enter(self, name):
        self.driver.find_element(By.XPATH, self.name).clear()
        self.driver.find_element(By.XPATH, self.name).send_keys(name)
        
    def age_enter(self, age):
        self.driver.find_element(By.XPATH, self.age).clear()
        self.driver.find_element(By.XPATH, self.age).send_keys(age)
        
    def address_enter(self, address):
        self.driver.find_element(By.XPATH, self.address).clear()
        self.driver.find_element(By.XPATH, self.address).send_keys(address)
        
    def email_enter(self, email):
        self.driver.find_element(By.XPATH, self.email).clear()
        self.driver.find_element(By.XPATH, self.email).send_keys(email)
        
    def contact_enter(self, contact):
        self.driver.find_element(By.XPATH, self.Contact).clear()
        self.driver.find_element(By.XPATH, self.Contact).send_keys(contact)
        
    def password_enter(self, password):
        self.driver.find_element(By.XPATH, self.Password).clear()
        self.driver.find_element(By.XPATH, self.Password).send_keys(password)
        
    def registerclick(self):
        self.driver.find_element(By.XPATH, self.regiser_button).click()
      
