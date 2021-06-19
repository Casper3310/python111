from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager
import random
import time
# 開啟Chrome
# 28135詹克家 28127邱資善 22214謝汶益 21513張展榮 28133陳志槐 28399陳彥誌 28389江智傑
# 22185江秋遠 28138趙珮伶 28131周俊佑 20941沈旻頡 26566張智傑
ID_list = ["28129", "28135", "28127", "22214", "21513", "28399"
           "28133", "28389", "22185", "28138", "28131", "20941", "26566", "26901", "21288"]
for aaa in range(2):
    for empID in ID_list:
        driver = webdriver.Chrome()
        driver.get("https://trtccod.app/covid-health-report/")
        element = driver.find_elements_by_tag_name('button')[1]
        element.click()
    #WebDriverWait(driver, 等待的最長時間, 檢查條件的頻率, 忽略的例外類別).until(expected_conditions條件, 超時例外的錯誤訊息)

        locator = (By.ID, "empid")
        inputID = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(locator))
        inputID.send_keys(empID)
        NextStep = driver.find_element_by_class_name('btn-secondary')
        NextStep.click()
        locator = (By.CSS_SELECTOR, '.btn-sm')
        temp = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(locator))
    # 按鍵數字
    # print(temp[0].text)   35
    # print(temp[1].text)   36
    # print(temp[6].text)   0.1
    # print(temp[14].text)  0.9
        index = random.randint(0, 1)
        temp[index].click()
        index = random.randint(6, 14)
        temp[index].click()

        js = "document.documentElement.scrollTop=10000"
        driver.execute_script(js)
        time.sleep(1)
        healthy = driver.find_element_by_id('healthy')
        healthy.click()
        submit = driver.find_element_by_class_name('btn-primary')
        submit.click()
        driver.close()
        print(empID)
print(ID_list)
