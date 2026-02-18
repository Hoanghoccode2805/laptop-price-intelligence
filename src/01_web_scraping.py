from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import random
import pandas as pd

all_name = []
all_price = []
all_detail = []

print("The bot is starting up ... ")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

base_url = "https://www.materiel.net/pc-portable/l409/page"


for page in range(1,10):
    try:
        current_url = f"{base_url}{page}/"

        print(f"--> Scraping data at: Page {page}")
        driver.get(current_url)
        time.sleep(random.uniform(3,5))

        list_name = driver.find_elements(By.TAG_NAME, "h2")
        list_prices = driver.find_elements(By.CSS_SELECTOR, '.o-product__price')
        list_details = driver.find_elements(By.CSS_SELECTOR,'.c-product__description')

        count = 0
        for name,price,detail in zip(list_name,list_prices,list_details):
            all_name.append(name.text)
            all_price.append(price.text)
            all_detail.append(detail.text)
            count += 1
        print(f"   + {count} computers were found on page {page}")

    except Exception as e:
        print(f"Error on the page {page}: {e}")
        continue 

print("-" * 30)
print("SAVING DATA..")

data = {
        'Name' : all_name,
        'Detail': all_detail,
        'Price' : all_price}
df = pd.DataFrame(data)
df.to_csv('D:/Full projet/laptop-price-intelligence/data/laptops_raw.csv', index = False, encoding='utf-8-sig')
print(f"Finish! Total revenue: {len(df)} data")
print("The file was saved at: laptops_raw.csv")

# Close url
print("Work done, going to bed now!")
driver.quit()

















