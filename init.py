from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10.0'
desired_caps['deviceName'] = 'rsylfahmjnemwc4h'
desired_caps['udid'] = 'rsylfahmjnemwc4h'
desired_caps['appPackage'] = "com.tanihub.vaesdothrak"
desired_caps['appActivity'] = "com.tanihub.vaesdothrak.MainActivity"
desired_caps['noReset'] = False
desired_caps['automationName'] = 'uiautomator2'
desired_caps['appiumVersion'] = '1.16.0'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def find_element(element, timeout=10):
    try:
        result = WebDriverWait(driver, timeout).until(ec.presence_of_element_located(element))
        return result
    except TimeoutException:
        print("This element couldn't be found : {} ".format(element))
        return None

button_explore_sekarang = (By.XPATH, "//*[@text='Explore Sekarang']")
button_jabodetabek = (By.XPATH, "//*[@text='Jabodetabek']")
button_belanja_sekarang = (By.XPATH, "//*[@text='Belanja Sekarang']")
text_urutkan = (By.XPATH, "//*[contains(@text, 'Urutkan')]")
button_search_bar = (By.XPATH, "//*[contains(@text, 'Cari buah')]")
text_field_search = (By.XPATH, "//android.widget.EditText[contains(@text, 'Cari buah')]")

find_element(button_explore_sekarang).click()
find_element(button_jabodetabek).click()
find_element(button_belanja_sekarang).click()
find_element(text_urutkan)
find_element(button_search_bar).click()
find_element(text_field_search).send_keys("Apel")




