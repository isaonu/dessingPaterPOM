import pytest
from POM.login import LoginPage

# Usamos fixture para iniciar el server de appium, solo se llama una vez en el archivo
@pytest.mark.usefixtures("appium_start")
class TestSignIn:

    ####
    # Aqui van los test cases de la suite
    ####

    ####
    # Uso driver_setup como Arrange y cleanup
    #def test_login_user_with_issues(self, driver_setup, user, password, errormsg):
    #    Act
    #   Assert
    ####


