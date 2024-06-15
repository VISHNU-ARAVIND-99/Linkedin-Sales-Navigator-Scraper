from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import pandas as pd
import re
from role import role_find
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def sign_in():
    driver.get("https://www.linkedin.com/login")
    time.sleep(3)
    driver.maximize_window()
    time.sleep(3)
    email_input = driver.find_element(By.XPATH, '//*[@id="username"]')

    email_input.send_keys("type_Yourid")
    time.sleep(4)
    password_input = driver.find_element(By.XPATH, '//*[@id="password"]')

    password_input.send_keys("type_yourpassword")
    time.sleep(5)
    button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
    button.click()
    time.sleep(5)


def scroll_down_page_action_chains(scroll_pause_time=2,  scroll_increment=550, max_duration=13):
    scrollable_div = driver.find_element(By.XPATH, '//*[@id="search-results-container"]')
    start_time = time.time()

    while True:
        driver.execute_script("arguments[0].scrollTop += arguments[1]", scrollable_div, scroll_increment)
        time.sleep(scroll_pause_time)

        if time.time() - start_time > max_duration:
            break


def sales_navigator_scraper():
    sign_in()
    link = input("enter the link here = ")
    driver.get(link)
    time.sleep(15)
    scroll_down_page_action_chains()
    button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Next"]')
    out = []
    for _ in range(14):
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
            updated_url = link.replace("https://www.linkedin.com/sales/lead/", "https://www.linkedin.com/in/")
            parts = updated_url.split(",")
            final_url = parts[0]
            out.append([x[0], name, title, x[1], location, final_url, link, company])

        button.click()
        time.sleep(7)
        scroll_down_page_action_chains()
        button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Next"]')
    return out


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

list_of_list = sales_navigator_scraper()

df = pd.DataFrame(list_of_list, columns=['Hierarchy N0', 'Name', 'Current Company Title', 'Role', 'Location',
                                         'Linkedin Url', 'Sales Navigator Link', 'Company'])
df.to_excel('Sales_Navigator_output.xlsx', index=False)
