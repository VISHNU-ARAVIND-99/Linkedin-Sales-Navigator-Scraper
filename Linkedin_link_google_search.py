from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.keys import Keys
import re


def craft_scraping(name, title, company, location):
    driver.get("https://www.google.com/")
    driver.maximize_window()
    time.sleep(1)
    search1 = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
    search1.send_keys(f'{name} + {title} + {location} + {company} + Linkedin')
    search1.send_keys()
    time.sleep(1)
    search1.send_keys(Keys.RETURN)
    time.sleep(1)
    source = BeautifulSoup(driver.page_source, "html.parser")

    links = []
    count = 0

    info = source.find_all('div', class_='yuRUbf')
    for div in info:
        a_tags = div.find_all('a')
        links.extend([a.get('href') for a in a_tags if a.get('href')])
        count += 1
        if count >= 5:
            break
    return links


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

df = pd.read_excel('Sales_Navigator_output.xlsx')

out = []
q = 0
for i, row in df.iterrows():
    #Hierarchy N0', 'Name', 'Current Company Title', 'Role', 'Location', 'Sales Navigator Link', 'Company'
    links = craft_scraping(name=row[1], title=row[2], company=row[6], location=row[4])
    out.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6]] + links)
    q += 1
    print(q)
df = pd.DataFrame(out)
df.to_excel('Final_out.xlsx', index=False)
