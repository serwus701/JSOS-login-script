from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import login_details

if __name__ == '__main__':

    username = login_details.username
    password = login_details.password

    driver = webdriver.Chrome()

    driver.set_page_load_timeout(10)
    driver.get("https://jsos.pwr.edu.pl/")
    driver.maximize_window()

    # accept conditions
    driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/a[2]/i").click()

    # credentials input and login
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/form/div[2]/div[1]/input").send_keys(username)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/form/div[2]/div[2]/input").send_keys(password)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/form/div[3]/div[1]/input").click()

    # zajecia button
    driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/ul/li[3]/a").click()
    # tygodnie button
    driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div[1]/div/div/div/div/div[2]/ul/li[1]/ul/li[3]/a").click()

    # non-active student to active student
    if (login_details.correct_student_status):
        driver.find_element(By.CLASS_NAME, "sbSelector").click()

        time.sleep(0.5)
        driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div[2]/div[2]/div/div/ul/li[2]/a").click()
        time.sleep(0.5)
        driver.refresh()

    driver.execute_script("window.scrollTo(0, 600)")
    time.sleep(10000)
