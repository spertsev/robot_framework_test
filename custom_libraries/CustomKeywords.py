import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def verify_city_name_after_change(entered_city_name):
    driver = webdriver.Chrome()
    driver.get("https://weather-app-madza.netlify.app")
    driver.implicitly_wait(20)
    time.sleep(3)
    city_input_bar = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/input')
    city_input_bar.send_keys(entered_city_name)
    city_input_bar.send_keys(Keys.ENTER)
    time.sleep(3)
    city_name_element = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/h1[1]')
    if not city_name_element.text.__contains__(entered_city_name):
        raise Exception('City name on the page differs from the entered one')
    time.sleep(1)
    driver.close()

# current_city_name = "Moscow"
# verify_city_name_after_change(current_city_name)