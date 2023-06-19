import pytest
from appium import webdriver
from appium.webdriver.appium_service import AppiumService


@pytest.fixture
def driver_setup(request):
    # Desire capabilities section
    desired_cap = {
        "platformName": "android",
        "platformVersion": "10",
        "deviceName": "emulator-5554",
        "automationName": "UiAutomator2",
        "appPackage": "com.swaglabsmobileapp",
        "appActivity": ".MainActivity"
    }
    # Creating the driver by passing the desired capabilities
    driver = webdriver.Remote("http://0.0.0.0:4723", desired_cap)
    yield driver
    print("Closing the driver")
    driver.quit()

@pytest.fixture(scope="module")
def appium_start():
    appium_service = AppiumService()
    print("Start appium server")
    appium_service.start()
    yield
    print("Stop appium server")
    appium_service.stop()

