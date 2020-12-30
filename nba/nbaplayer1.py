
#class="nba-stat-table__overlay"

from selenium import webdriver
from bs4 import BeautifulSoup


class player():
	def __init__(self):
		self.names=""
		self.link=""


def get_player_list():
			
	#create driver
	driver = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
	url='https://in.global.nba.com/playerindex/'

	#download html page

	driver.get(url)
	html_doc=driver.page_source.encode("utf-8")
	#create soup
	soup=BeautifulSoup(html_doc,'lxml')

	player_list=[]

	div=soup.find('div' ,class_='nba-stat-table__overlay')
	for a in div.find_all('a', class_='player-name ng-isolate-scope'):
		name=""
		for span in a.find_all('span'):
			name=name+span.text
		# print(name)	
		# print(a['data-ng-href'])	
		new_play=player()
		new_play.names=name
		new_play.link='https://in.global.nba.com'+a['data-ng-href']
		player_list.append(new_play)

	for one_player in player_list:
		print(one_player.names)
		print(one_player.link)

	driver.quit()


	return player_list

get_player_list()	