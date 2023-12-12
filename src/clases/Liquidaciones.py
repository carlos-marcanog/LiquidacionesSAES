import sys
import os
import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from src.utils.Utils import *
from src.utils.Locators import *

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

class Liquidaciones():

    def __init__(self, driver):
        self.driver = driver


    def altaLote(self, tipo_liquidacion, razon_social):
        try:
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(1)
            time.sleep(1)
            self.driver.find_element(By.XPATH, MN_LIQUIDACIONES).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, MN_LIQUIDACIONES_COMPB).click()
            time.sleep(1)
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(2)
            time.sleep(1)
            self.driver.find_element(By.XPATH, PER_NUEVO_LOTE).click()
            time.sleep(1)
            dropdown = self.driver.find_element(By.XPATH, DD_TIPO_LIQUIDACION)
            dropdown.find_element(By.XPATH, tipo_liquidacion).click()
            self.driver.find_element(By.XPATH, TXT_RAZON_SOCIAL).send_keys(razon_social)
            time.sleep(1)
            self.driver.find_element(By.XPATH, BTN_BUSCAR_RAZON_SOCIAL).click()
            self.driver.find_element(By.XPATH, BTN_BUSCAR_RAZON_SOCIAL).click()
            self.driver.find_element(By.XPATH, FECHA_RECEPCION_LOTE).send_keys(FECHA)
            time.sleep(1)
            self.driver.find_element(By.XPATH, BTN_OK_LOTE).click()
            self.driver.find_element(By.XPATH, BTN_OK_LOTE).click()
            time.sleep(2)
            texto_inicial = self.driver.find_element(By.XPATH, LOTE_GENERADO).text
            texto_final = texto_inicial[:6]
            assert texto_final == '[ LOTE'
        except AssertionError as error:
            print("No coincide el texto del elemento web con el texto esperado: [" + texto_final + "] =! [ LOTE ")
            dateTime = time.strftime("%m/%d/%Y_%H:%M:%S")
            testName = whoami()
            screenshotName = testName + "_" + dateTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName, attachment_type=allure.attachment_type.PNG)
            print(error)
            raise

    def agregarComprobante(self, tipo_liquidacion, razon_social):
        self.altaLote(tipo_liquidacion, razon_social)
        self.driver.find_element(By.XPATH, LOTE_GENERADO).click()
        self.driver.find_element(By.XPATH, AGREGAR_COMPROBANTE).click()
        dropdown1 = self.driver.find_element(By.XPATH, TIPO_COMPROBANTE)
        dropdown1.find_element(By.XPATH, "//option[. = 'RESUMEN DE CUENTA']").click()
        dropdown2 = self.driver.find_element(By.XPATH, LETRA_COMPROBANTE)
        dropdown2.find_element(By.XPATH, "//option[. = 'X']").click()
        self.driver.find_element(By.XPATH, PTO_VENTA_COMPROBANTE).send_keys("1234")
        self.driver.find_element(By.XPATH, NUMERO_COMPROBANTE).send_keys("1789")
        self.driver.find_element(By.XPATH, FECHA_IMPRESION_COMPROBANTE).send_keys("11/12/2023")
        self.driver.find_element(By.XPATH, FECHA_COMPROBANTE).send_keys("11/12/2023")
        self.driver.find_element(By.XPATH, PERIODO_COMPROBANTE).send_keys("11/2023")
        self.driver.find_element(By.XPATH, NETO_GRAVADO_COMPROBANTE).send_keys("200000")
        self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtComproCanti").click()
        self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtComproCanti").send_keys("1")
        self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
        self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtAmbuTotal").click()
        self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtAmbuTotal").send_keys("100000")
        self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtInterTotal").click()
        self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtInterTotal").send_keys("100000")
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_imgOK1").click()
        self.vars["win4912"] = self.wait_for_window(2000)
        self.vars["root"] = self.driver.current_window_handle
        self.driver.switch_to.window(self.vars["win4912"])
        self.driver.close()
        self.driver.switch_to.window(self.vars["root"])
        self.driver.switch_to.frame(2)
        self.driver.find_element(By.CSS_SELECTOR, "#ctl00_cMain_UCTree1_tvHierarchyViewt1 > font:nth-child(1)").click()







