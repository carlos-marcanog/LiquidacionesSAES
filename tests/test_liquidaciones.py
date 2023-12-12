import pytest

from src.clases.Liquidaciones import Liquidaciones
from src.clases.Login import Login
from src.utils.Utils import *
from src.utils.Locators import *


@pytest.mark.usefixtures("test_setup")
class TestLiquidaciones():

    @pytest.mark.skip
    def test_1_login(self):
        driver = self.driver
        loginUsuarios = Login(driver)
        loginUsuarios.loginUsuarioSaes(USER1, PASS1)

    def test_2_lote_prestacion(self):
        driver = self.driver
        liquidaciones = Liquidaciones(driver)
        liquidaciones.altaLote(TIPO_PRESTACION, 'ACLIBA I')

    @pytest.mark.skip
    def test_3_lote_presmed(self):
        driver = self.driver
        liquidaciones = Liquidaciones(driver)
        liquidaciones.altaLote(TIPO_PRESMED, 'ACLIBA I')

    @pytest.mark.skip
    def test_4_lote_medicamentos(self):
        driver = self.driver
        liquidaciones = Liquidaciones(driver)
        liquidaciones.altaLote(TIPO_MEDICAMENTOS)

    @pytest.mark.skip
    def test_5_lote_protesis(self):
        driver = self.driver
        liquidaciones = Liquidaciones(driver)
        liquidaciones.altaLote(TIPO_PROTESIS)

    @pytest.mark.skip
    def test_6_lote_varios(self):
        driver = self.driver
        liquidaciones = Liquidaciones(driver)
        liquidaciones.altaLote(TIPO_VARIOS)

    @pytest.mark.skip
    def test_7_lote_discapacidad(self):
        driver = self.driver
        liquidaciones = Liquidaciones(driver)
        liquidaciones.altaLote(TIPO_DISCAPACIDAD)

