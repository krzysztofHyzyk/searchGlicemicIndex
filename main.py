import time
import undetected_chromedriver as uc
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

products = ["jabłko", "ziemniak", "gruszka", "śliwka"]
def search(driver, text):
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
        return "no data"
chromedriver = r"chromedriver.exe"
brave = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
option = uc.ChromeOptions()
option.add_argument("--headless")
option.binary_location = brave
driver = uc.Chrome(driver_executable_path=chromedriver, options=option)
driver.get('https://www.bing.com/')

for prod in products:
    print(prod + ": " + search(driver,prod))

input()


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