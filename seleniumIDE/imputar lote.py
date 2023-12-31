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

class TestAgregarcomprobante():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_agregarcomprobante(self):
    self.driver.get("https://saesdesa.ospesalud.com.ar/saes/")
    self.driver.set_window_size(1936, 1048)
    self.driver.find_element(By.ID, "btnLogin").click()
    self.driver.switch_to.frame(1)
    self.driver.find_element(By.LINK_TEXT, "Liquidaciones").click()
    self.driver.find_element(By.LINK_TEXT, "Liquidación de Comprobantes").click()
    self.driver.switch_to.default_content()
    self.driver.switch_to.frame(2)
    self.driver.find_element(By.ID, "ctl00_cMain_ddlEstadoLote").click()
    dropdown = self.driver.find_element(By.ID, "ctl00_cMain_ddlEstadoLote")
    dropdown.find_element(By.XPATH, "//option[. = 'ACTIVO']").click()
    self.driver.find_element(By.ID, "ctl00_cMain_drpTipoLiquidacion").click()
    dropdown = self.driver.find_element(By.ID, "ctl00_cMain_drpTipoLiquidacion")
    dropdown.find_element(By.XPATH, "//option[. = 'PRESTACION']").click()
    self.driver.find_element(By.ID, "ctl00_cMain_imgFilter").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > td:nth-child(1) > input").click()
    self.driver.find_element(By.ID, "ctl00_cMain_imgEdit").click()
    self.driver.find_element(By.CSS_SELECTOR, "font:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "font:nth-child(2)").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "font:nth-child(2)")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_btnAddHead").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpTipoComprobante1").click()
    dropdown = self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpTipoComprobante1")
    dropdown.find_element(By.XPATH, "//option[. = 'RESUMEN DE CUENTA']").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpLetraComprobante1").click()
    dropdown = self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpLetraComprobante1")
    dropdown.find_element(By.XPATH, "//option[. = 'X']").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtSucursal1").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtSucursal1").send_keys("123")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtNumero1").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtNumero1").send_keys("321")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtFechaImpresion1").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtFechaImpresion1").send_keys("01/10/2023")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtFechaEmision1").send_keys("01/10/2023")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtPeriodo1").send_keys("05/2023")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtSubtotal1").send_keys("50000")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtComproCanti").send_keys("1")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtAmbuTotal").send_keys("25000")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtInterTotal").send_keys("25000")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_imgOK1").click()
    self.vars["win3710"] = self.wait_for_window(2000)
    self.vars["root"] = self.driver.current_window_handle
    self.driver.switch_to.window(self.vars["win3710"])
    self.driver.switch_to.window(self.vars["root"])
    self.driver.switch_to.frame(2)
    self.driver.find_element(By.CSS_SELECTOR, "#content > table > tbody > tr:nth-child(1) > td").click()
    self.driver.find_element(By.CSS_SELECTOR, "font:nth-child(3)").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_btnAddSubHead").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_UCPrestadorSubComprob1_btnSearch").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4) > td:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4) > td:nth-child(3)").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4) > td:nth-child(3)")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4) > td:nth-child(3)").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_UCPrestadorSubComprob1_txtCodigo").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_UCPrestadorSubComprob1_txtCodigo").send_keys("60384/0")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_UCPrestadorSubComprob1_btnSearch").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpTipoComprobante1").click()
    dropdown = self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpTipoComprobante1")
    dropdown.find_element(By.XPATH, "//option[. = 'FACTURA']").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpLetraComprobante1").click()
    dropdown = self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpLetraComprobante1")
    dropdown.find_element(By.XPATH, "//option[. = 'A']").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtSucursal1").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtSucursal1").send_keys("123")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtNumero1").send_keys("321")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtFechaImpresion1").send_keys("01/10/2023")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtFechaEmision1").send_keys("01/10/2023")
    self.driver.switch_to.window(self.vars["win3710"])
    self.driver.close()
    self.driver.switch_to.window(self.vars["root"])
    self.driver.switch_to.frame(2)
    element = self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtSucursal1")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtSucursal1")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtSucursal1")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtSucursal1").click()
    self.driver.find_element(By.CSS_SELECTOR, "#ctl00_cMain_UCTree1_UCHead1_tab_Datos1 tr:nth-child(2)").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtSucursal1").send_keys("33")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtNumero1").click()
    self.driver.find_element(By.CSS_SELECTOR, "#ctl00_cMain_UCTree1_UCHead1_tab_Datos1 > tbody").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtNumero1").send_keys("915")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtFechaImpresion1").click()
    self.driver.find_element(By.CSS_SELECTOR, "#ctl00_cMain_UCTree1_UCHead1_tab_Datos1 tr:nth-child(2)").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtFechaImpresion1").send_keys("30/09/2023")
    self.driver.find_element(By.CSS_SELECTOR, "#ctl00_cMain_UCTree1_UCHead1_tab_Datos1 tr:nth-child(2)").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtFechaEmision1").send_keys("30/09/2023")
    self.driver.find_element(By.CSS_SELECTOR, "table:nth-child(32) > tbody > tr > td").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtFechaVtoCai1").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtFechaVtoCai1").send_keys("30/09/2023")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtPeriodo1").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtPeriodo1").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtPeriodo1").send_keys("04/2023")
    self.driver.find_element(By.CSS_SELECTOR, "table:nth-child(32) > tbody > tr > td").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtSubtotal1").send_keys("1041715.68")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpIVASubCompPresmed").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(6) > td:nth-child(3)").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpIVASubCompPresmed").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(6) > .frmLabelText").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpIIBBSubCompPresmed").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpIIBBSubCompPresmed").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpIVASubCompPresmed").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtNetoNoGravado").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtNetoNoGravado").send_keys("1041715.68")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpIVASubCompPresmed").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(6) > td:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#ctl00_cMain_UCTree1_UCHead1_tab_Datos2 > tbody").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpIIBBSubCompPresmed").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtIIBBSubCompPresmed").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtNetoNoGravado").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtSubtotal1").click()
    self.driver.find_element(By.CSS_SELECTOR, "#ctl00_cMain_UCTree1_UCHead1_trBonificacion > .frmLabelText:nth-child(3)").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpIIBBSubCompPresmed").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpIVASubCompPresmed").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpIIBBSubCompPresmed").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtNetoNoGravado").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtNetoNoGravado").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtNetoNoGravado").click()
    element = self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtNetoNoGravado")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtNetoNoGravado").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(6) > td:nth-child(3)").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtBonificacion").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtNetoNoGravado").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtIIBBSubCompPresmed").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(6) > td:nth-child(3)").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtIIBBSubCompPresmed").send_keys("1041.72")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtTotal1").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(7) > td").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtBonificacion").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtTotal1").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtTotal1").click()
    element = self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtTotal1")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtTotal1").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtNetoNoGravado").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtNetoNoGravado").send_keys("1041715.68")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.CSS_SELECTOR, "#ctl00_cMain_UCTree1_UCHead1_trIIBBSubCompPresmed > .frmLabelText").click()
    self.driver.find_element(By.CSS_SELECTOR, "#ctl00_cMain_UCTree1_UCHead1_trIIBBSubCompPresmed > .frmLabelText").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "#ctl00_cMain_UCTree1_UCHead1_trIIBBSubCompPresmed > .frmLabelText")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpIIBBSubCompPresmed").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpIVASubCompPresmed").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(6) > td:nth-child(3)").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.CSS_SELECTOR, ".frmLabelText > label").click()
    self.driver.find_element(By.CSS_SELECTOR, "table:nth-child(32) > tbody > tr > td").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtIVASubCompPresmed").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpIIBBSubCompPresmed").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4) table:nth-child(1) tr:nth-child(1) > td:nth-child(6)").click()
    self.driver.find_element(By.ID, "ctl00_cMain_ddlEstadoLote").click()
    dropdown = self.driver.find_element(By.ID, "ctl00_cMain_ddlEstadoLote")
    dropdown.find_element(By.XPATH, "//option[. = 'ACTIVO']").click()
    self.driver.find_element(By.ID, "ctl00_cMain_drpTipoLiquidacion").click()
    dropdown = self.driver.find_element(By.ID, "ctl00_cMain_drpTipoLiquidacion")
    dropdown.find_element(By.XPATH, "//option[. = 'PRESTACION']").click()
    self.driver.find_element(By.ID, "ctl00_cMain_imgEdit").click()
    self.driver.find_element(By.ID, "ctl00_cMain_imgFilter").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > td:nth-child(1) > input").click()
    self.driver.find_element(By.ID, "ctl00_cMain_imgEdit").click()
    self.driver.find_element(By.CSS_SELECTOR, "font:nth-child(3)").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_btnAddSubHead").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpIIBBSubCompPresmed").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpIIBBSubCompPresmed").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpTipoComprobante1").click()
    dropdown = self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpTipoComprobante1")
    dropdown.find_element(By.XPATH, "//option[. = 'FACTURA']").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpLetraComprobante1").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_UCPrestadorSubComprob1_txtDescripcion").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_UCPrestadorSubComprob1_btnSearch").click()
    self.driver.find_element(By.CSS_SELECTOR, "#ctl00_cMain_UCTree1_UCHead1_UCPrestadorSubComprob1_GridView1 tr:nth-child(2) > td:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#ctl00_cMain_UCTree1_UCHead1_UCPrestadorSubComprob1_GridView1 tr:nth-child(2) > td:nth-child(3)").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "#ctl00_cMain_UCTree1_UCHead1_UCPrestadorSubComprob1_GridView1 tr:nth-child(2) > td:nth-child(3)")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "#ctl00_cMain_UCTree1_UCHead1_UCPrestadorSubComprob1_GridView1 tr:nth-child(2) > td:nth-child(3)").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_UCPrestadorSubComprob1_txtCodigo").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_UCPrestadorSubComprob1_txtCodigo").send_keys("60389/0")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_UCPrestadorSubComprob1_btnSearch").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpTipoComprobante1").click()
    dropdown = self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpTipoComprobante1")
    dropdown.find_element(By.XPATH, "//option[. = 'FACTURA']").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpLetraComprobante1").click()
    dropdown = self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpLetraComprobante1")
    dropdown.find_element(By.XPATH, "//option[. = 'A']").click()
    self.driver.find_element(By.CSS_SELECTOR, "#ctl00_cMain_UCTree1_UCHead1_tab_Datos1 .frmLabelText:nth-child(4)").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtSucursal1").send_keys("33")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtNumero1").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtNumero1").send_keys("915")
    self.driver.find_element(By.CSS_SELECTOR, "table:nth-child(32) > tbody > tr > td").click()
    self.driver.find_element(By.CSS_SELECTOR, "table:nth-child(32) > tbody > tr > td").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpIIBBSubCompPresmed").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpIIBBSubCompPresmed").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(6) > td:nth-child(4)").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtFechaImpresion1").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtFechaImpresion1").send_keys("30/09/2023")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtFechaEmision1").send_keys("30/09/2023")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtFechaVtoCai1").send_keys("30/09/2023")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtPeriodo1").send_keys("04/2023")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtSubtotal1").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtNetoNoGravado").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtSubtotal1").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtSubtotal1").send_keys("1041715.68")
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(6) > td:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".frmLabelText > label").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtCAE").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtCAE").send_keys("73399781577827")
    self.driver.find_element(By.CSS_SELECTOR, "table:nth-child(32) > tbody > tr > td").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_imgOK1").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_imgCANCEL1").click()
    self.driver.find_element(By.CSS_SELECTOR, "font:nth-child(5)").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_btnEditHead").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtSubtotal1").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtSubtotal1").send_keys("2000000")
    self.driver.find_element(By.CSS_SELECTOR, "#content > table > tbody > tr:nth-child(1) > td").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_imgOK1").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ctl00_cMain_UCTree1_tvHierarchyView_5").click()
    self.driver.find_element(By.CSS_SELECTOR, "font > font:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#ctl00_cMain_UCTree1_tvHierarchyViewn0 > img").click()
    self.driver.find_element(By.CSS_SELECTOR, "#ctl00_cMain_UCTree1_tvHierarchyViewt1 > font:nth-child(2)").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_btnDelHead").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_imgOK1").click()
    self.driver.find_element(By.CSS_SELECTOR, "font > font:nth-child(1)").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_btnAddHead").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpTipoComprobante1").click()
    dropdown = self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpTipoComprobante1")
    dropdown.find_element(By.XPATH, "//option[. = 'RESUMEN DE CUENTA']").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpLetraComprobante1").click()
    dropdown = self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpLetraComprobante1")
    dropdown.find_element(By.XPATH, "//option[. = 'X']").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtSucursal1").send_keys("123")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtNumero1").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtNumero1").send_keys("321")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtFechaImpresion1").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtFechaImpresion1").send_keys("30/09/2023")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtFechaEmision1").send_keys("30/09/2023")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtPeriodo1").send_keys("04/2023")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtSubtotal1").send_keys("2000000")
    self.driver.find_element(By.CSS_SELECTOR, "table:nth-child(32) > tbody > tr > td").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtComproCanti").send_keys("1")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtSubtotal1").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtSubtotal1").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtSubtotal1").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtSubtotal1").send_keys("20000000")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtAmbuTotal").send_keys("10000000")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtInterTotal").send_keys("10000000")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_imgOK1").click()
    self.vars["win8505"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win8505"])
    self.driver.close()
    self.driver.switch_to.window(self.vars["root"])
    self.driver.switch_to.frame(2)
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_btnAddSubHead").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_UCPrestadorSubComprob1_txtCodigo").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_UCPrestadorSubComprob1_txtCodigo").send_keys("60389/0")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_UCPrestadorSubComprob1_btnSearch").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpTipoComprobante1").click()
    dropdown = self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpTipoComprobante1")
    dropdown.find_element(By.XPATH, "//option[. = 'FACTURA']").click()
    dropdown = self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_drpLetraComprobante1")
    dropdown.find_element(By.XPATH, "//option[. = 'A']").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtSucursal1").send_keys("33")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtNumero1").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtNumero1").send_keys("915")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtFechaImpresion1").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtFechaImpresion1").send_keys("30/09/2023")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtFechaEmision1").send_keys("30/09/2023")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtFechaVtoCai1").send_keys("30/09/2023")
    self.driver.find_element(By.CSS_SELECTOR, "table:nth-child(32) > tbody > tr > td").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtPeriodo1").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtPeriodo1").send_keys("04/2023")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtSubtotal1").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtSubtotal1").send_keys("1041715.68")
    self.driver.find_element(By.CSS_SELECTOR, ".frmLabelText > label").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtCAE").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_txtCAE").send_keys("73399781577827")
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_tab_Datos2").click()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCHead1_imgOK1").click()
    self.vars["win8263"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win8263"])
    self.driver.close()
    self.driver.switch_to.window(self.vars["root"])
    self.driver.switch_to.frame(2)
    self.driver.find_element(By.CSS_SELECTOR, "#ctl00_cMain_UCTree1_tvHierarchyViewt2 > font:nth-child(5)").click()
    self.driver.find_element(By.CSS_SELECTOR, "#ctl00_cMain_UCTree1_tvHierarchyViewt2 > font:nth-child(5)").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "#ctl00_cMain_UCTree1_tvHierarchyViewt2 > font:nth-child(5)")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "font > font:nth-child(2)").click()
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_btnImputarLote").click()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.ID, "ctl00_cMain_UCTree1_UCLote1_imgOK").click()
    self.vars["win4917"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win4917"])
    self.driver.close()
    self.driver.switch_to.window(self.vars["root"])
  
