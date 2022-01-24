from selenium.webdriver.common.by import By

class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        
        self.admin = "/html/body/div/div[2]/div[2]/div/div[2]/div[3]"
        self.username = "/html/body/div/div[2]/div[2]/div/div[3]/div/div[3]/input"
        self.password = "/html/body/div/div[2]/div[2]/div/div[3]/div/div[5]/input"
        self.login_button = "/html/body/div/div[2]/div[2]/div/div[3]/div/div[6]/div/button"
        self.regiser_button = "/html/body/div/div[2]/div[2]/div/div[3]/div/a"
        self.patient = "/html/body/div/div[2]/div[2]/div/div[2]/div[2]"
        self.doctor = "/html/body/div/div[2]/div[2]/div/div[2]/div[1]"       
        
        
    def admin_select(self):
        self.driver.find_element(By.XPATH, self.admin).click()
        
    def doctor_select(self):
        self.driver.find_element(By.XPATH, self.doctor).click()
        
    def patient_select(self):
        self.driver.find_element(By.XPATH, self.patient).click()
        
    def username_enter(self, username):
        self.driver.find_element(By.XPATH, self.username).clear()
        self.driver.find_element(By.XPATH, self.username).send_keys(username)
        
    def password_enter(self, password):
        self.driver.find_element(By.XPATH, self.password).clear()
        self.driver.find_element(By.XPATH, self.password).send_keys(password)
        
    def loginclick(self):
        self.driver.find_element(By.XPATH, self.login_button).click()
        
    def registerclick(self):
        self.driver.find_element(By.XPATH, self.regiser_button).click()
        
      
