#div class=	poster-->a['href']-->	div class="class="MediaViewerImagestyles__PortraitContainer-sc-1qk433p-2 gIroZm""
#-->img['src']

from selenium import webdriver

from bs4 import BeautifulSoup
import requests

driver =webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
url='https://www.imdb.com/title/tt0111161/'

driver.get(url)

html_doc=driver.page_source

soup = BeautifulSoup(html_doc,'lxml')
# print(soup)

div=soup.find('div',class_='poster')
# print(div)
pos=div.find('a')
pos_link='https://www.imdb.com'+pos['href']

# print(pos_link)

driver.get(pos_link)
ht_doc=driver.page_source
soup=BeautifulSoup(ht_doc,'lxml')
div =soup.find('div',class_='MediaViewerImagestyles__PortraitContainer-sc-1qk433p-2 gIroZm')
img=div.find('img')
print(img['src'])

f=open('first_image.jpg','wb')
f.write(requests.get(img['src']).content)
f.close()
driver.quit()