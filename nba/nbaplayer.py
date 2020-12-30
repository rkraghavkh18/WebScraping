
#class="nba-stat-table__overlay"

from selenium import webdriver
from bs4 import BeautifulSoup

#create driver
driver = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
url='https://in.global.nba.com/playerindex/'

#download html page

driver.get(url)
html_doc=driver.page_source.encode("utf-8")
#create soup
soup=BeautifulSoup(html_doc,'lxml')
# #print(soup.encode("utf-8"))
# a= soup.find_all('a',{"class":"player-name ng-isolate-scope"})
div=soup.find('div' ,class_='nba-stat-table__overlay')
for a in div.find_all('a', class_='player-name ng-isolate-scope'):
	for span in a.find_all('span'):
		print(span.text)
# for span in soup.find('a', class_='player-name ng-isolate-scope').find_all('span'):
#     print(span.text)

# div=soup.find('div' ,class_='nba-stat-table__overlay')
# print(div)
# table=div.find_all('table')
# print(table.find_all('a')[0])
driver.quit()