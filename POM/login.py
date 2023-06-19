# Esto lo utilizamos para poder selecionar nuestros elementos
from appium.webdriver.common.appiumby import AppiumBy

# Importamos la clase que vamos a heredar
from utilities.commonMethods import BaseClass

# Esto nos sirve para incializar nuestro objeto con el driver y pasarlo al test
from POM.home import HomePage


class LoginPage(BaseClass):
    pass

    ####
    # Los selectores van aqui como variables
    ####

    ####
    # Los metodos / acciones de pagina especifica van aqui
    # El constructor viene de la clase padre
    # Podemos usar el driver aqui con self.driver
    # Podemos llamar a los metodos de BaseClass por la herencia como self.nombre_metodo_de_BaseClass
    #
    ####

