from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import pandas as pd
import re
from role import role_find


def sign_in():
    driver.get("https://www.linkedin.com/login")
    time.sleep(3)
    driver.maximize_window()
    time.sleep(3)
    email_input = driver.find_element(By.XPATH, '//*[@id="username"]')

    email_input.send_keys("n-vishnuaravind.s@draup.com")
    time.sleep(4)
    password_input = driver.find_element(By.XPATH, '//*[@id="password"]')

    password_input.send_keys("Nemili@1805")
    time.sleep(5)
    button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
    button.click()
    time.sleep(5)


def sales_navigator_scraper():
    sign_in()
    link = input("enter the link here = ")
    driver.get(link)
    check = input("next button:")
    out = []
    while check:
        source = BeautifulSoup(driver.page_source, "html.parser")
        info = source.find_all('div', class_='artdeco-entity-lockup artdeco-entity-lockup--size-4 ember-view')
        for i in info:
            mid = i.find('div', class_='artdeco-entity-lockup__title ember-view')
            name = mid.get_text().lstrip().strip()
            link = mid.find('a', href=True)['href']
            link = f"https://www.linkedin.com{link}"
            mid = i.find('div', class_='artdeco-entity-lockup__subtitle ember-view t-14').get_text().lstrip().strip()
            title, company = re.split(r'\s{5,}', mid)
            title = title.strip()
            company = company.strip()
            location = i.find('div', class_='artdeco-entity-lockup__caption ember-view').get_text().lstrip().strip()
            x = role_find(title=title)
            out.append([x[0], name, title, x[1], location, link, company])
        check = input("next button:")
    return out


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

list_of_list = sales_navigator_scraper()

df = pd.DataFrame(list_of_list, columns=['Hierarchy N0', 'Name', 'Current Company Title', 'Role', 'Location', 'Sales Navigator Link', 'Company'])
df.to_excel('Sales_Navigator_output.xlsx', index=False)
