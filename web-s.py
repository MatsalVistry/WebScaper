from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(executable_path=r'C:/Vatsal/Python/chromedriver.exe')

prices = []
pages = []
pages.append("https://www.walmart.com/search/?grid=true&query=laptops")
finishedpages = []

while len(pages) != 0:
    currentLink = pages.pop(0)
    if(currentLink.replace("/","") in finishedpages):
        continue

    print(currentLink)
    print(finishedpages)
    driver.get(currentLink)
    content = driver.page_source
    soup = BeautifulSoup(content, features='html.parser')

    for div in soup.findAll('div', attrs={'class':'search-result-gridview-item-wrapper'}):
        price=div.find('span', attrs={'class':'price-characteristic'})
        if price is not None:
            prices.append(price.text)

    finishedpages.append(currentLink.replace("/",""))   
    
    paginator = soup.find('div',attrs={'class':'paginator'})
    if paginator is not None:
        for page in paginator.findAll('a', href=True):
            link = "https://www.walmart.com"+page["href"]
            pages.append(link)

df = pd.DataFrame({'Price':prices}) 
df.to_csv('products.csv', index=False, encoding='utf-8')