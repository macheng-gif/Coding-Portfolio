from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time



chrome_driver = 'C:/Users/HOUSINGADMIN/Desktop/chromedriver/chromedriver.exe'
service = Service(chrome_driver)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)


url = "https://totalcard.housing.olemiss.edu:7052/portal/#17020634604852520"

driver.get(url)

time.sleep(20)

#Enters unsername and password
username_input = wait.until(
    EC.presence_of_element_located((By.ID, 'textfield-1012-inputEl'))
)
username_input.send_keys('******')



password_input = wait.until(
    EC.element_to_be_clickable((By.ID, 'textfield-1013-inputEl'))
)
password_input.send_keys('**********')

#Clicks login button
login_button = wait.until(
    EC.element_to_be_clickable((By.ID, 'button-1014-btnInnerEl'))
)

login_button.click()

time.sleep(20)

#Finds and clicks battery button
battery_button = driver.find_element(By.ID, 'vv-lpad-bdg-1012')

hover = ActionChains(driver).move_to_element(battery_button)
hover.perform()

driver.execute_script("arguments[0].click();", battery_button)

time.sleep(10)


#Finds and clicks tab
tab = driver.find_element(By.ID, "tab-1050-btnInnerEl")
tab.click()

time.sleep(15)

#Finds second URL
wait.until(EC.url_changes(url))
new_page_url = driver.current_url
index = list(new_page_url)
frame1 = index[-17:]
frame2 = "".join(frame1)
while "#" in frame2:
    frame2.replace("#", "")
iframe_id = (frame2)
driver.switch_to.frame("BatteryLowReport-%s-iframeEl" % iframe_id)

#Clicks add button

add_button_xpath = "/html/body/form/table/tbody/tr/td[3]/a"
add_button = driver.find_element(By.XPATH, add_button_xpath)
action = ActionChains(driver).move_to_element(add_button)
action.perform()

driver.execute_script("arguments[0].click(0);", add_button)

time.sleep(15)

#Clicks save button
save_button_xpath = "/html/body/table[2]/tbody/tr/td[2]/a[1]"
save_button = driver.find_element(By.XPATH, save_button_xpath)
actions = ActionChains(driver).move_to_element(save_button)
actions.perform()

driver.execute_script("arguments[0].click(0);", save_button)

time.sleep(20)

#Clicks export to excel button
excel_button_xpath = "/html/body/table[2]/tbody/tr[2]/td[5]/input[4]"
excel_button = driver.find_element(By.XPATH, excel_button_xpath)
actions = ActionChains(driver).move_to_element(excel_button)
actions.perform()

driver.execute_script("arguments[0].click(0);", excel_button)

time.sleep(30)

quit()
