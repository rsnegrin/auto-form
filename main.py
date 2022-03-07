from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from settings import INPUT_NAMES_LOGIN, INPUT_NAMES_FORM
import os


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
browser = webdriver.Chrome(
    executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options
)

browser.get("https://formulariocovid19.uc.cl/accesouc/")

for input_name in INPUT_NAMES_LOGIN:
    name_input = browser.find_elements_by_name(input_name)[0]
    name_input.send_keys(os.getenv(input_name, "None"))

browser.find_elements_by_name("submit")[0].click()

for input_name in INPUT_NAMES_FORM:
    if input_name == "campus":
        elem = browser.find_elements_by_name(input_name)
        select = Select(elem[1])
        select.select_by_index(int(os.getenv("campus", 3)))

    elif input_name == "lugar":
        name_input = browser.find_elements_by_name(input_name)[1]
        name_input.send_keys(os.getenv("lugar", "Ingeniería"))

    elif input_name in ["pre_1", "pre_2"]:

        name_input = browser.find_elements_by_name(input_name)[2]
        browser.execute_script("arguments[0].click();", name_input)
    else:
        name_input = browser.find_elements_by_name(input_name)[1]
        browser.execute_script("arguments[0].click();", name_input)

browser.find_element_by_class_name("uc-btn.btn-primary.btn-inline").click()
# Alert(browser).accept()
