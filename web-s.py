from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(executable_path=r'C:/Vatsal/Python/chromedriver.exe')

prices = []
names = []
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
        price = div.find('span', attrs={'class':'price-characteristic'})
        nameHelper = div.find('div', attrs={'class':'search-result-product-title gridview'})
        name = None
        if nameHelper is not None:
            nameHelper = nameHelper.find('a', attrs={'class':'product-title-link line-clamp line-clamp-2 truncate-title'})
            if nameHelper is not None:
                name = nameHelper.find('span')

        if (price is not None) and (name is not None):
            prices.append(price.text)
            names.append(name.text)


    finishedpages.append(currentLink.replace("/",""))   
    
    paginator = soup.find('div',attrs={'class':'paginator'})
    if paginator is not None:
        for page in paginator.findAll('a', href=True):
            link = "https://www.walmart.com"+page["href"]
            pages.append(link)

print("finished")
df = pd.DataFrame({'Name':names,'Price':prices}) 
df.to_csv('products.csv', index=False, encoding='utf-8')