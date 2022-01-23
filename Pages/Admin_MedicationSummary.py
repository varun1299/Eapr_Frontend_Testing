from selenium.webdriver.common.by import By

class AdminFillMedicationsummary():
    def __init__(self, driver):
        self.driver = driver
        
        self.medication_item = "/html/body/div/div[2]/div/input[1]"
        self.medication_name = "/html/body/div/div[2]/div/input[2]"
        self.medication_form = "/html/body/div/div[2]/div/input[3]"
        self.strength_numerator= "/html/body/div/div[2]/div/input[4]"
        self.strength_numerator_unit = "/html/body/div/div[2]/div/input[5]"
        self.denominator = "/html/body/div/div[2]/div/input[6]"
        self.denominator_unit = "/html/body/div/div[2]/div/input[7]"
        self.unit_of_presentation= "/html/body/div/div[2]/div/input[8]"
        self.strength_concentration = "/html/body/div/div[2]/div/input[9]"
        self.manufacturer = "/html/body/div/div[2]/div/input[10]"
        self.batch_id = "/html/body/div/div[2]/div/input[11]"
        self.expiry = "/html/body/div/div[2]/div/input[12]"
        self.amount = "/html/body/div/div[2]/div/input[13]"
        self.amount_unit= "/html/body/div/div[2]/div/input[14]"
        self.alternate_amount = "/html/body/div/div[2]/div/input[15]"
        self.alternate_amount_unit = "/html/body/div/div[2]/div/input[16]"
        self.description= "/html/body/div/div[2]/div/input[17]"
        self.dosage_amount = "/html/body/div/div[2]/div/input[18]"
        self.lower = "/html/body/div/div[2]/div/input[19]"
        self.upper = "/html/body/div/div[2]/div/input[20]"
        self.dosage_unit = "/html/body/div/div[2]/div/input[21]"
        self.dosage_formula = "/html/body/div/div[2]/div/input[22]"
        self.timing_daily_frequency = "/html/body/div/div[2]/div/input[24]"
        self.lower = "/html/body/div/div[2]/div/input[25]"
        self.upper = "/html/body/div/div[2]/div/input[26]"
        self.specific_event_name = "/html/body/div/div[2]/div/input[33]"
        self.specific_event_timeoffset = "/html/body/div/div[2]/div/input[34]"
        self.administration_details_route = "/html/body/div/div[2]/div/input[38]"
        self.administration_details_bodysite = "/html/body/div/div[2]/div/input[39]"
        self.timingnondaily_repitition_interval = "/html/body/div/div[2]/div/input[40]"
        self.timingnondaily_frequency = "/html/body/div/div[2]/div/input[41]"
        self.specific_event_name = "/html/body/div/div[2]/div/input[48]"
        self.specific_event_timeoffset = "/html/body/div/div[2]/div/input[49]"
        self.protocol_order_id = "/html/body/div/div[2]/div/input[53]"
        self.absenceofinforamtion_lastupdated = "/html/body/div/div[2]/div/input[54]"
        self.temporary_save = "/html/body/div/div[2]/div/button[1]"
        self.final_save= "/html/body/div/div[2]/div/button[2]"         
        
        
        
        
        
    def fill_medication_item(self, item):
        self.driver.find_element(By.XPATH, self.medication_item).clear()
        self.driver.find_element(By.XPATH, self.medication_item).send_keys(item)
        
    def fill_medication_name(self, name):
        self.driver.find_element(By.XPATH, self.medication_name).clear()
        self.driver.find_element(By.XPATH, self.medication_name).send_keys(name)
        
    def fill_medication_form(self, form):
        self.driver.find_element(By.XPATH, self.medication_form).clear()
        self.driver.find_element(By.XPATH, self.medication_form).send_keys(form)
        
    def final_save_click(self):
        self.driver.find_element(By.XPATH, self.final_save).click()
      
