link='https://www.imdb.com/title/tt0066763/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=690bec67-3bd7-45a1-9ab4-4f274a72e602&pf_rd_r=0BSW7KS4V7TVVE8P9572&pf_rd_s=center-4&pf_rd_t=60601&pf_rd_i=india.top-rated-indian-movies&ref_=fea_india_ss_toprated_tt_1'

def similar_movies_ki_list_scrape(url):
	import requests
	import pprint
	from bs4 import BeautifulSoup
	data=requests.get(url)
	soup=BeautifulSoup(data.text,"html.parser")
	# print(soup)
	n=soup.find('div',class_='title_wrapper')
	name_1=n.find('h1').text[0:-8]
	# print(name)
	
	div=soup.find('div',attrs={'class':'article','id':'titleRecs'})
	alldiv=div.findAll('div',class_='rec_item')
	big_dict={}
	list_1=[]
	for i in alldiv:
		for j in (i('a')):
			id_movic=j.get('href')[7:16]
			name=j.find('img').get('alt')
			dict_1={'movies_name':name,'id':id_movic}
			# print(dict_1)
			list_1.append(dict_1)
		# print(list_1)

		big_dict[name_1]=list_1
	pprint.pprint(big_dict)


similar_movies_ki_list_scrape(link)