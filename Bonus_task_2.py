def analysis_male_female():
	import requests
	from pprint import pprint
	from bs4 import BeautifulSoup
	import json

	url = " https://www.imdb.com/india/top-rated-indian-movies/"
	page = requests.get(url)
	soup = BeautifulSoup(page.text,"html.parser")
	man_div = soup.find('div',class_="lister")
	tbody = man_div.find('tbody',class_="lister-list")
	trs = tbody.find_all('tr')
	big_list=[]
	for tr in trs:
		url_link=tr.find("a").get("href")
		# print(url_link[0:17])
		url="https://www.imdb.com"+url_link[0:17]+"ratings?ref_=tt_ov_rt"
		page=requests.get(url)
		soup=BeautifulSoup(page.text,"html.parser")

		name_1=soup.find('div',class_='aux-content-widget-2 links subnav')
		name=name_1.find('a').get_text()
		# print(name)

		tbody=soup.find('div',class_='title-ratings-sub-page')
		trs=tbody.findAll('div',class_='smallcell')
		list_1=[]
		# print(trs)
		dict_infom={}
		for j in trs:
			a=j.text.split()
			for k in a:
				# print(k)
				list_1.append(k)
		
		dict_new={'male':list_1[5],'female':list_1[10]}
		dict_infom[name]=dict_new
		print(dict_infom)
		big_list.append(dict_infom)
	with open('male_and_female_like_movies.json','w+') as new_file:
		json.dump(big_list,new_file)

analysis_male_female()