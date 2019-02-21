def scrape_top_list():
	import requests
	import pprint
	from bs4 import BeautifulSoup
	url = " https://www.imdb.com/india/top-rated-indian-movies/"
	page = requests.get(url)
	# print(data)
	soup = BeautifulSoup(page.text,"html.parser")
	# print(soup)
	man_div = soup.find('div',class_="lister")
	# print(man_div)
	tbody = man_div.find('tbody',class_="lister-list")
	# print(tbody)
	trs = tbody.find_all('tr')
	# print(trs)

	big_list_all_movic=[]
	for tr in trs:
		movi_data = tr.find('td',class_='titleColumn').get_text().strip().split()
		# print(movi_data)
		po=movi_data[0].strip('.')
		position=int(po)
		# print(position)
		y=(movi_data[-1].strip('()'))
		year=int(y)
		# print(year)
		name1 = tr.find('td',class_='titleColumn')
		name2=name1.find('a')
		name=(name2.text)
		# print(name)
		url_link=tr.find("a").get("href")
		link="https://www.imdb.com"+url_link
		# print(link)
		rating_movi = tr.find('td',class_='ratingColumn imdbRating').get_text().split()
		R=float(rating_movi[0])
		# print(R)

		fist_dict = {"position":position,"name":name,"year":year,"rating":R,"url":link}
		big_list_all_movic.append(fist_dict)

	return (big_list_all_movic)
# all_movic=(scrape_top_list())
# print(all_movic)
# pprint.pprint(all_movic)

