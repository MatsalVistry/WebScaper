from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

driver = webdriver.Chrome(executable_path=r'C:/Vatsal/Python/chromedriver.exe')
page = "https://www.nhsinform.scot/illnesses-and-conditions/a-to-z"

driver.get(page)
content = driver.page_source
soup = BeautifulSoup(content, features='html.parser')
names = []

for header in soup.findAll('h2', attrs={'class':'module__title'}):
    if header is not None and header.text is not None:
        names.append([(header.text+"").strip()])


print("finished")
# df = pd.DataFrame({'Name':names}) 
# df.to_csv('stored.csv', index=False, encoding='utf-8')

for loc in range(0,25):
    print(loc)
    page = "https://www.google.com/search?q=symptoms+of+"+names[loc][0].replace(" ","+")
    driver.get(page)
    content = driver.page_source
    soup = BeautifulSoup(content, features='html.parser')

    results = soup.find('div', attrs={'class':'kp-blk c2xzTb Wnoohf OJXvsb'})
    if results is not None:
        results2 = results.findAll('li', attrs={'class':'TrT0Xe'})
        if results2 is not None:
            for li in results2:
                if li.text is not None:
                    text = li.text.strip().replace(".","")
                    if len(text)<50:
                        names[loc].append(text)

print("finished2")

df = pd.DataFrame({'Name':names}) 
df.to_csv('stored.csv', mode='a',index=False, encoding='utf-8')