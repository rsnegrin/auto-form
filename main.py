from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import pandas as pd


df = pd.read_csv("data.csv", encoding="utf-8")

input_names_login = ["username", "password"]

input_names_form = [
    "campus",
    "lugar",
    "pre_1",
    "pre_2",
    "temperatura2",
    "anosmia",
    "ageusia",
    "tos_estornudos",
    "calofrios",
    "cefalea",
    "odinofagia",
    "mialgias",
    "diarrea",
    "dolortorax",
    "disnea",
    "congestion",
    "taquipnea",
    "fatiga",
    "nauseas_vomito",
]

browser = webdriver.Chrome(
    executable_path="./drivers/chromedriver_linux64/chromedriver"
)

browser.get("https://formulariocovid19.uc.cl/accesouc/")

for input_name in input_names_login:
    name_input = browser.find_elements_by_name(input_name)[0]
    name_input.send_keys(df[input_name])

browser.find_elements_by_name("submit")[0].click()

for input_name in input_names_form:
    if input_name == "campus":
        elem = browser.find_elements_by_name(input_name)
        select = Select(elem[1])
        select.select_by_index(int(df[input_name]))

    elif input_name == "lugar":
        name_input = browser.find_elements_by_name(input_name)[1]
        name_input.send_keys(df[input_name])

    elif input_name in ["pre_1", "pre_2"]:

        name_input = browser.find_elements_by_name(input_name)[2]
        browser.execute_script("arguments[0].click();", name_input)
    else:
        name_input = browser.find_elements_by_name(input_name)[1]
        browser.execute_script("arguments[0].click();", name_input)

browser.find_element_by_class_name("uc-btn.btn-primary.btn-inline").click()
# Alert(browser).accept()
