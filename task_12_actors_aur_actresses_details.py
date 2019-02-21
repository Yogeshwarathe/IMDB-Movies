import requests
import pprint
import json
from bs4 import BeautifulSoup
url='https://www.imdb.com/title/tt0066763/fullcredits?ref_=tt_cl_sm#cast'
def scrape_movie_cast(movie_caste_url):
	page=requests.get(movie_caste_url)
	# print(page)
	soup=BeautifulSoup(page.text,"html.parser")
	# listo=soup.find('div',class_="article listo")
	table=soup.find('table',class_='cast_list')
	tr=table.findAll('td',class_='')
	man_list=[]
	for i in tr:
		actor_name=(i.find('a').get_text().strip())
		imdb_id=(i.find('a').get('href')[6:15])
		# print(actor_name)
		# print(id_actor)
		dict_1={'imdb_id':imdb_id,'name':actor_name}
		man_list.append(dict_1)

		# y_name=imdb_id+'_cast.json'
		# with open(y_name,'w+') as file_name:
		# 	json.dump(dict_1,file_name)

	with open('movic_anand_actors_details.json','w+') as new_file:
		json.dump(man_list,new_file)

	return (man_list)


# pprint.pprint(scrape_movie_cast(url))
