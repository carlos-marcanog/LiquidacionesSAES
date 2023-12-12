import pytest
import sys
import os

from src.clases.Login import Login
from src.utils.Utils import *

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Seleccione Navegador")
    parser.addoption("--ambiente", action="store", default="desa48", help="Ingrese el Ambiente de Pruebas")
    parser.addoption("--user", action="store", default="marcano01", help="Ingrese el Número del Beneficiario")
    parser.addoption("--pass", action="store", default="Externo$$111", help="Ingrese la Clave del Beneficiario")

@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    browser = request.config.getoption("--browser")
    ambiente = request.config.getoption("--ambiente")
    user = request.config.getoption("--user")
    password = request.config.getoption("--pass")

    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    elif browser == 'edge':
        driver = webdriver.Edge()

    driver.implicitly_wait(20)
    driver.maximize_window()
    request.cls.driver = driver

    if ambiente == 'desa35':
        driver.get(SAES35_DESA)
    elif ambiente == 'test35':
        driver.get(SAES35_TEST)
    elif ambiente == 'desa48':
        driver.get(SAES48_DESA)
    elif ambiente == 'test48':
        driver.get(SAES48_TEST)

    login_beneficiario = Login(driver)
    login_beneficiario.loginUsuarioSaes(user, password)

    yield
    driver.close()
    driver.quit()
    print("Test Completed")
