#div class=	poster-->a['href']-->	div class="class="MediaViewerImagestyles__PortraitContainer-sc-1qk433p-2 gIroZm""
#-->img['src']

from selenium import webdriver

from bs4 import BeautifulSoup
import requests

class Film():
	def __init__(self):
		self.title=""
		self.rank=""
		self.year=""
		self.link=""


def get_film_list():

	driver = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

	url='https://www.imdb.com/chart/top/?ref_=nv_mv_250'

	driver.get(url)

	html_doc=driver.page_source
	# print(html_doc)

	soup = BeautifulSoup(html_doc,'lxml')

	# print(soup)


	table=soup.find('table',class_='chart')
	# print(table)
	film_list=[]

	for td in table.find_all('td',class_='titleColumn'):
		full_title=td.text.strip().replace('\n',' ').replace('      ',' ')
		print(full_title)

		rank=full_title.split('.')[0]
		print(rank)
		title=full_title.split('.')[1].split('(')[0]
		print(title.strip())
		year=full_title.split('(')[1][:-1]
		print(year)

		a=td.find('a')
		print(a['href'])
		print("\n")


		new_film=Film()
		new_film.rank=rank
		new_film.title=title.strip()
		new_film.year=year
		new_film.link=a['href']
		film_list.append(new_film)
	driver.quit()	
	return film_list

def  download_all_poster(film_list):
	
	driver =webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
	
	for f in film_list:

		# url='https://www.imdb.com/title/tt0111161/'
		url = 'https://www.imdb.com'+f.link 
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

		f=open('{0}.jpg'.format(f.title.replace(';'," ")),'wb')
		f.write(requests.get(img['src']).content)
		f.close()

	driver.quit()

download_all_poster(get_film_list())	