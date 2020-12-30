
#s-include-content-margin s-border-bottom s-latency-cf-section

from selenium import webdriver
from bs4 import BeautifulSoup

class book():
	def __init__(self):
		self.title=""
		self.link=""

def get_book_list():

	driver = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

	url ='https://www.amazon.in/s?k=python+programming+books&crid=2Z09JRX057ZH8&sprefix=python+programming'
	driver.get(url)

	html_doc=driver.page_source
	# print(html_doc)
	soup = BeautifulSoup(html_doc,'lxml')
	# print(soup)
	div1 = soup.find('div',class_='s-main-slot s-result-list s-search-results sg-row')
	
	book_list=[]
	# print(div1)
	for div2 in div1.findAll('div',class_='s-include-content-margin s-border-bottom s-latency-cf-section'):
		# print(div2.encode('utf-8'))
		for all_a in div2.findAll('a',class_='a-link-normal a-text-normal'):
			# print(all_a.text)
			# print(all_a['href'])
			# print("\n")
			new_book=book()
			new_book.title=all_a.text
			new_book.link='https://www.amazon.in'+all_a['href']
			book_list.append(new_book)


	driver.quit()
	
	return book_list		

b1=get_book_list()	

for book in  b1 :
	print (book.title)
	print(book.link)
	print("\n")
