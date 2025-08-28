from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

tenTen_button = "/html/body/form/table[2]/tbody/tr[11]/td[1]/input"
tenTen_txt = "IP Access Controller Number = 1010 - ADMIN - (CMD)"
tenTen_button_txt = "/html/body/form/table[2]/tbody/tr[11]/td[4]"

tenEleven_button = "/html/body/form/table[2]/tbody/tr[15]/td[1]/input"
tenEleven_txt = "IP Access Controller Number = 1011 - RCS - (CMD)"
tenEleven_button_txt = "html/body/form/table[2]/tbody/tr[15]/td[4]"

tenTwelve_button = "/html/body/form/table[2]/tbody/tr[18]/td[1]/input"
tenTwelve_txt = "IP Access Controller Number = 1012 - LRC - (CMD)"
tenTwelve_button_txt = "html/body/form/table[2]/tbody/tr[18]/td[4]"

tenThirteen_button = "/html/body/form/table[2]/tbody/tr[21]/td[1]/input"
tenThirteen_txt = "IP Access Controller Number = 1013 - LRC Ext - (CMD)"
tenThirteen_button_txt = "html/body/form/table[2]/tbody/tr[21]/td[4]"

tenFifthteen_button = "/html/body/form/table[2]/tbody/tr[24]/td[1]/input"
tenFifthteen_txt = "IP Access Controller Number = 1015 - Deaton - (CMD)"
tenFifthteen_button_txt = "html/body/form/table[2]/tbody/tr[24]/td[4]"

tenSixteen_button = "/html/body/form/table[2]/tbody/tr[27]/td[1]/input"
tenSixteen_txt = "IP Access Controller Number = 1016 - RCS03 - (CMD)"
tenSixteen_button_txt = "html/body/form/table[2]/tbody/tr[27]/td[4]"

tenSeventeen_button = "/html/body/form/table[2]/tbody/tr[30]/td[1]/input"
tenSeventeen_txt = "IP Access Controller Number = 1017 - Brown - (CMD)"
tenSeventeen_button_txt = "html/body/form/table[2]/tbody/tr[30]/td[4]"

tenEighteen_button = "/html/body/form/table[2]/tbody/tr[33]/td[1]/input"
tenEighteen_txt = "IP Access Controller Number = 1018 - Stewart - (CMD)"
tenEighteen_button_txt = "html/body/form/table[2]/tbody/tr[33]/td[4]"

tenNineteen_button = "/html/body/form/table[2]/tbody/tr[36]/td[1]/input"
tenNineteen_txt = "IP Access Controller Number = 1019 - Stockard - (CMD)"
tenNineteen_button_txt = "html/body/form/table[2]/tbody/tr[36]/td[4]"

tenTwenty_button = "/html/body/form/table[2]/tbody/tr[39]/td[1]/input"
tenTwenty_txt = "IP Access Controller Number = 1020 - Martin - (CMD)"
tenTwenty_button_txt = "html/body/form/table[2]/tbody/tr[39]/td[4]"

tenTwentyone_button = "/html/body/form/table[2]/tbody/tr[42]/td[1]/input"
tenTwentyone_txt = "IP Access Controller Number = 1021 - RH1 - (CMD)"
tenTwentyone_button_txt = "html/body/form/table[2]/tbody/tr[42]/td[4]"

tenTwentytwo_button = "/html/body/form/table[2]/tbody/tr[45]/td[1]/input"
tenTwentytwo_txt = "IP Access Controller Number = 1022 - RH2 - (CMD)"
tenTwentytwo_button_txt = "html/body/form/table[2]/tbody/tr[45]/td[4]"

tenTwentythree_button = "/html/body/form/table[2]/tbody/tr[48]/td[1]/input"
tenTwentythree_txt = "IP Access Controller Number = 1023 - RH3 - (CMD)"
tenTwentythree_button_txt = "html/body/form/table[2]/tbody/tr[48]/td[4]"

tenFourteen_button = "/html/body/form/table[2]/tbody/tr[51]/td[1]/input"
tenFourteen_txt = "IP Access Controller Number = 1014 - LRC Gen - (CMD)"
tenFourteen_button_txt = "html/body/form/table[2]/tbody/tr[51]/td[4]"

chrome_driver = "C:/Users/HOUSINGADMIN/Desktop/chromedriver/chromedriver.exe"
service = Service(chrome_driver)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

url = "https://totalcard.housing.olemiss.edu:7052/portal/#17020634604852520"

driver.get(url)

time.sleep(20)

# Enters username and password
username_input = wait.until(
    EC.presence_of_element_located((By.ID, 'textfield-1012-inputEl'))
)
username_input.send_keys('****')

password_input = wait.until(
    EC.element_to_be_clickable((By.ID, 'textfield-1013-inputEl'))
)
password_input.send_keys('*****')

# Clicks login button
login_button = wait.until(
    EC.element_to_be_clickable((By.ID, 'button-1014-btnInnerEl'))
)

login_button.click()

time.sleep(45)

# Finds and clicks search button
search_button = wait.until(
    EC.element_to_be_clickable((By.ID, "button-1030-btnIconEl"))
)

search_button.click()

search_bar = wait.until(
    EC.presence_of_element_located((By.ID, "combo-1029-inputEl"))
)
search_bar.send_keys("Work with servers")
search_bar.send_keys(Keys.ENTER)

time.sleep(10)

# Switches to new page
tab_button = driver.find_element(By.ID, "tab-1051-btnInnerEl")

tab_button.click()

wait.until(EC.url_changes(url))
new_page_url = driver.current_url
index = list(new_page_url)
frame1 = index[-17:]
frame2 = "".join(frame1)
while "#" in frame2:
    frame2.replace("#", "")
iframe_id = (frame2)
driver.switch_to.frame("WorkWithServers-%s-iframeEl" % iframe_id)

time.sleep(5)


# Clicks check boxes for servers buttons
def buttonClicks():
    ten_result = check1(tenTen_button, tenTen_txt, tenTen_button_txt)

    eleven_result = check1(tenEleven_button, tenEleven_txt, tenEleven_button_txt)

    twelve_result = check1(tenTwelve_button, tenTwelve_txt, tenTwelve_button_txt)

    thirteen_result = check1(tenThirteen_button, tenThirteen_txt, tenThirteen_button_txt)

    fourteen_result = check1(tenFourteen_button, tenFourteen_txt, tenFourteen_button_txt)

    fifthteen_result = check1(tenFifthteen_button, tenFifthteen_txt, tenFifthteen_button_txt)

    sixteen_result = check1(tenSixteen_button, tenSixteen_txt, tenSixteen_button_txt)

    seventeen_result = check1(tenSeventeen_button, tenSeventeen_txt, tenSeventeen_button_txt)

    eighteen_result = check1(tenEighteen_button, tenEighteen_txt, tenEighteen_button_txt)

    nineteen_result = check1(tenNineteen_button, tenNineteen_txt, tenNineteen_button_txt)

    twenty_result = check1(tenTwenty_button, tenTwenty_txt, tenTwenty_button_txt)

    twentyone_result = check1(tenTwentyone_button, tenTwentyone_txt, tenTwentyone_button_txt)

    twentytwo_result = check1(tenTwentytwo_button, tenTwentytwo_txt, tenTwentytwo_button_txt)

    twentythree_result = check1(tenTwentythree_button, tenTwentythree_txt, tenTwentythree_button_txt)




def check1(xpath, txt, txt1):
    text_found = False
    try:
        button_txt = driver.find_element(By.XPATH, txt1)
        print(f"Found text: {button_txt.text}")
        if txt == button_txt.text:
            button = driver.find_element(By.XPATH, xpath)
            button.click()
            print(f"Clicked button for text: {txt}")
            text_found = True
    except NoSuchElementException:
        pass
    if not text_found:
        result = check2(txt)
        print(result)
        if result:
            button1 = driver.find_element(By.XPATH, result)
            button1.click()
        else:
            print("checkTen() did not provide a valid XPath. Handling missing XPath scenario.")


def check2(text1):
    for i in range(10, 101):
        xpath = ("/html/body/form/table[2]/tbody/tr[%s]/td[4]" % i)
        print("Attempting Xpath:", xpath)
        try:
            button_text = driver.find_element(By.XPATH, xpath)
            text = button_text.text
            print(text)
            if text == text1:
                xpath1 = ("/html/body/form/table[2]/tbody/tr[%s]/td[1]/input" % i)
                print(xpath1)
                return xpath1

        except:
            print("Button not found for xpath:", xpath)
            continue

    return None


buttonClicks()

time.sleep(10)

end_checked_button = driver.find_element(By.XPATH, "/html/body/form/table[1]/tbody/tr/td[3]/input[2]")
end_checked_button.click()

time.sleep(30)

buttonClicks()

time.sleep(10)

start_checked_button = driver.find_element(By.XPATH, "/html/body/form/table[1]/tbody/tr/td[3]/input[1]")
start_checked_button.click()

#start_all_button = driver.find_element(By.XPATH, "/html/body/form/table[1]/tbody/tr/td[1]/input[1]")
#start_all_button.click()

time.sleep(10)

quit()
