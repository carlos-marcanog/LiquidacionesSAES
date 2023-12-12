import inspect

#URLS
SAES35_DESA = 'http://saeswebdesa.ospe.intra/SAES/default.aspx'
SAES35_TEST = 'http://saeswebtest.ospe.intra/saes/default.aspx'

SAES48_DESA = 'https://saesdesa.ospesalud.com.ar/saes/'
SAES48_TEST = 'https://saestest.ospesalud.com.ar/saes/'

#USUARIOS
USER1 = 'marcano01'
PASS1 = 'Externo$$111'

#FECHA
FECHA = '30/10/2023'




#METODOS DE UTILIDAD

#Devuelve el nombre del metodo
def whoami():
    return inspect.stack()[1][3]