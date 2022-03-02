from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def table_data(url):
    s = Service('c:\selenium browser drivers\chromedriver.exe')
    driver = webdriver.Chrome(service=s)

    driver.get(url)
    try:
        button = driver.find_element(By.XPATH, '//*[@class="_5b77d672 da62f2ae _8a1d083b"]')
        driver.execute_script("arguments[0].click();", button)
    except Exception as e:
        print("call button is not clicked")

    try:
        agent_name = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//span[@class = "f2186d94"]'))).text
    except Exception as e:
        agent_name = None

    try:
        mobile_number = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '//*[@class="f1b2ae85"]/tbody/tr[1]/td[2]/a/span'))).text
    except Exception as e:
        mobile_number = None

    try:
        phone_number = WebDriverWait(driver,2).until(EC.presence_of_element_located( (By.XPATH,'//*[@class="f1b2ae85"]/tbody/tr[2]/td[2]/a/span') )).text
    except Exception as e:
        phone_number = None

        driver.quit()
    return agent_name,mobile_number,phone_number
