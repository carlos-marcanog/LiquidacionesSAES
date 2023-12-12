# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestlogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(executable_path="C:/Users/cmarcano/OneDrive - Capgemini/Desktop/Automation/SAES/drivers/chromedriver.exe")
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testlogin(self):
    self.driver.get("https://saesdesa.ospesalud.com.ar/saes/")
    self.driver.find_element(By.ID, "txtUser").send_keys('marcano01')
    self.driver.find_element(By.ID, "txtPassword").send_keys('Externo$$111')
    self.driver.find_element(By.ID, "btnLogin").click()
    self.driver.switch_to.frame(1)
    self.driver.find_element(By.LINK_TEXT, "Liquidaciones").click()
    self.driver.find_element(By.LINK_TEXT, "Liquidación de Comprobantes").click()
    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(2)
    self.driver.find_element(By.ID, "ctl00_cMain_imgAdd").click()
  