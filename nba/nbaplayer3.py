
#class="nba-stat-table__overlay"

from selenium import webdriver
from bs4 import BeautifulSoup


class player():
	def __init__(self):
		self.names=""
		self.link=""
		self.Born=""
		self.Drafted=""
		self.Experience=""
		self.PtoNBA=""



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

	return(player_list)
def get_detail_for_all_players(player_list):

	driver = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
	for p in player_list[0:2]:

		# url='https://in.global.nba.com/players/#!/precious_achiuwa'

		url=p.link

		driver.get(url)

		html_doc=driver.page_source.encode("utf-8")
		# print(driver.page_source.encode("utf-8"))
		player_bio=[]
		soup=BeautifulSoup(html_doc,'lxml')
		

		for span in soup.find_all('span',class_='player-info-right--bio ng-binding'):
			player_bio.append(span.text)

		Born=player_bio[1]
		Drafted=player_bio[2]
		Experience=player_bio[3]
		PtoNBA=player_bio[4]	

		p.Born=Born
		p.Drafted=Drafted
		p.Experience=Experience
		p.PtoNBA=PtoNBA

	driver.quit()
	return player_list


player_list=get_detail_for_all_players(get_player_list())

for p in player_list[0:2]:
	print("\n")
	print(p.names)
	print(p.link)
	print(p.Born)
	print(p.Drafted)
	print(p.Experience)
	print(p.PtoNBA)
	print("\n")