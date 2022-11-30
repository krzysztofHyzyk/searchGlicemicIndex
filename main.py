# -*- coding: utf-8 -*-
#coding=utf-8
import time
import undetected_chromedriver as uc
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

products = ["jabłko", "ziemniak", "gruszka", "śliwka", "kapusta", "marchewka", "papryka"]
def searchBing(driver, text):
    driver.get('https://www.bing.com/')
    try:
        el = driver.find_element(By.XPATH, "//button[@id='bnp_btn_accept']")
        el.click()
    except:
        pass
    el = driver.find_element(By.XPATH, "//input[@type='search']")
    # create action chain object
    action = ActionChains(driver)
    # click the item
    action.click(on_element=el)
    c = '\u0001';
    action.send_keys(str(c));
    action.perform()
    action.send_keys(Keys.BACKSPACE)
    action.perform()
    # send keys
    action.send_keys(f"indeks glikemiczny {text}")
    action.send_keys(Keys.RETURN);
    # perform the operation
    action.perform()
    time.sleep(2)
    try:
        el = driver.find_element(By.XPATH, "//div[@class='b_focusTextMedium']")
        return el.text
    except:
        pass
    try:
        el = driver.find_element(By.XPATH, "//strong")
        return el.text
    except:
        pass

    return "no data"
chromedriver = r"chromedriver.exe"
#brave = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
option = uc.ChromeOptions()
option.add_argument("--headless")
#option.binary_location = brave
driver = uc.Chrome(driver_executable_path=chromedriver, options=option)
driver.get("https://bmi-online.pl/indeks-glikemiczny")
file = open("ig.txt","w")
i = 1
while True:
    try:
        el = driver.find_element(By.XPATH, f"//*[@class='content__table']/tbody/tr[{i}]/td[1]")
        print(el.text + ";", end="", file = file)
        el = driver.find_element(By.XPATH, f"//*[@class='content__table']/tbody/tr[{i}]/td[2]")
        print(el.text, file = file)
        i+=1
    except:
        break
i = 1
while True:
    try:
        el = driver.find_element(By.XPATH, f"/html/body/section/div/div[2]/div/div[2]/div[3]/div[3]/table/tbody/tr[{i}]/td[1]")
        print(el.text + ";", end="", file = file)
        el = driver.find_element(By.XPATH, f"/html/body/section/div/div[2]/div/div[2]/div[3]/div[3]/table/tbody/tr[{i}]/td[2]")
        print(el.text, file = file)
        i+=1
    except:
        break
file.close()
print("--- END ----")
input()

#for prod in products:
#    print(prod + ": " + searchBing(driver,prod))


# driver.get("https://google.pl")
# time.sleep(2)
# el = driver.find_element(By.XPATH,"//div[text()='Zaakceptuj wszystko']")
# el.click()
# el = driver.find_element(By.XPATH,"//input[@type='text']")
# # create action chain object
# action = ActionChains(driver)
# # click the item
# action.click(on_element=el)
# # send keys
# action.send_keys("indeks glikemiczny jabłko")
# action.send_keys(Keys.RETURN);
# # perform the operation
# action.perform()
#
# i = input()