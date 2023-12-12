import sys
import os
import time
import allure
from selenium.webdriver.common.by import By
from src.utils.Utils import *
from src.utils.Locators import *

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

class Login():

    def __init__(self, driver):
        self.driver = driver

    def loginUsuarioSaes(self, nombreUsuario, clave):
        try:
            self.driver.find_element(By.XPATH, INPUT_LOGIN_USER).clear()
            self.driver.find_element(By.XPATH, INPUT_LOGIN_USER).send_keys(nombreUsuario)
            time.sleep(1)
            self.driver.find_element(By.XPATH, INPUT_LOGIN_PASS).clear()
            self.driver.find_element(By.XPATH, INPUT_LOGIN_PASS).send_keys(clave)
            time.sleep(1)
            self.driver.find_element(By.XPATH, BUTTON_LOGIN).click()
            self.driver.switch_to.frame(0)
            texto = self.driver.find_element(By.XPATH, HOME_IDENTIFIER).text
            assert texto == "[inicio]"
            time.sleep(2)
        except AssertionError as error:
            print("No coincide el texto del elemento web con el texto esperado: " + texto + " =! [inicio]")
            dateTime = time.strftime("%m/%d/%Y_%H:%M:%S")
            testName = whoami()
            screenshotName = testName + "_" + dateTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName, attachment_type=allure.attachment_type.PNG)
            print(error)
            raise

