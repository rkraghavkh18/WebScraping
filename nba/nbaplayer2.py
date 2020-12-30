# weight/heigh
# born 
# drafted

from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
url='https://in.global.nba.com/players/#!/precious_achiuwa'

driver.get(url)

html_doc=driver.page_source.encode("utf-8")
# print(driver.page_source.encode("utf-8"))
player_bio=[]
soup=BeautifulSoup(html_doc,'lxml')
# print(soup.encode("utf-8"))
# hw=soup.find_all('span',class_="player-info-right--bio ng-binding")
# print(hw.text)
for span in soup.find_all('span',class_='player-info-right--bio ng-binding'):
	player_bio.append(span.text)

Born=player_bio[1]
Drafted=player_bio[2]
Experience=player_bio[3]
PtoNBA=player_bio[4]
# for span in b_span.findNextSiblings():
# 	born=born+span.text


# exp=""

# exp_span=soup.find('span',string='Experience')

# for span in exp_span.findNextSiblings():
# 	exp=exp+span.text	
# print(born)
# print(exp)
