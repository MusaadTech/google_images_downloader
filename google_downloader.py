import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

warnings.filterwarnings('ignore', category=DeprecationWarning)

driver_path = 'C:\\complete\\path\\to\\chromedriver.exe'
keyword = 'سعودية لوحة'
directory_number = 7
driver = webdriver.Chrome(driver_path)
driver.maximize_window()
driver.get('https://www.google.com/')

search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search_box.send_keys(keyword)
search_box.send_keys(Keys.ENTER)

image_box = driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
image_box.click()

# the following code snippet will keep scrolling down the webpage until it cannot scroll down anymore
last_height = driver.execute_script('return document.body.scrollHeight')
delay_time = 4  # In seconds
while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(delay_time)
    new_height = driver.execute_script('return document.body.scrollHeight')
    try:
        driver.find_element(By.XPATH, '//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
        time.sleep(delay_time)
    except:
        pass
    if new_height == last_height:
        try:
            driver.find_element(By.XPATH, '//*[@id="islmp"]/div/div/div/div[2]/span').click()
            time.sleep(delay_time)
        except:
            try:
                driver.find_element(By.XPATH, '//*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input').click()
                time.sleep(delay_time)
            except:
                break
    last_height = new_height

counter_start = 1
counter_end = 1000
naming_counter = 1
temp = 1
for i in range(counter_start, counter_end):
    if i == 25*temp:
        temp += 1
        naming_counter += 1
        continue
    try:
        driver.find_element(By.XPATH, f'//*[@id="islrg"]/div[1]/div[{naming_counter}]/a[1]/div[1]/img').click()
        driver.find_element(By.XPATH,
                            f'//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img')\
            .screenshot(f'C:\\datasets\\Saudi_Plates\\{directory_number}\\SP_{naming_counter}.png')
        naming_counter += 1
    except:
        pass
