from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(executable_path=r'C:/Vatsal/Python/chromedriver.exe')
page = "https://www.nhsinform.scot/illnesses-and-conditions/a-to-z"

driver.get(page)
content = driver.page_source
soup = BeautifulSoup(content, features='html.parser')
names = []

for header in soup.findAll('h2', attrs={'class':'module__title'}):
    if header is not None and header.text is not None:
        names.append((header.text+"").strip())


print("finished")
print(names)
df = pd.DataFrame({'Name':names}) 
df.to_csv('stored.csv', index=False, encoding='utf-8')