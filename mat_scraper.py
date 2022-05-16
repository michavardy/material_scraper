# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 13:27:36 2019

@author: Micha.Vardy
"""


from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome('chromedriver.exe')

url_list = [
        'http://asm.matweb.com/search/SpecificMaterial.asp?bassnum=MA7075T6',
        
        ]

url = 'http://www.matweb.com/search/DataSheet.aspx?MatGUID=4f19a42be94546b686bbf43f79c51b7d&ckck=1'
driver.get(url)
#table = 
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

table_list = soup.find_all('table')
#try:
#    df = pd.read_html(str(table_list[8]),header=0)
#except:
#    pass

for i in range(len(table_list)):
    table = table_list[i]
    try:
        df = pd.read_html(str(table),header=0)
        print(f'\n\n table: {i} \n\n {df} ')
    except:
        print(f'\n\ntable {i} didnt work \n\n')
    

#with open('scrape_test.txt', "w", encoding="utf-8") as f:
#    f.write(soup.prettify())
#file.close() 
