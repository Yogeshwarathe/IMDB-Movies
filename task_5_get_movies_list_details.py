from task_1_find_movice_name import scrape_top_list
from task_4_all_details import scrape_movies_details
import requests
import pprint
from bs4 import BeautifulSoup

# print(scrape_top_list())
def get_movies_list_details():
	all_movies=scrape_top_list()
	movies_list=[]
	stop=0
	for i in all_movies:
		if stop == 10:
			break
		else:
			stop+=1
			url_link=(i["url"])
			a=scrape_movies_details(url_link)
			movies_list.append(a)
	return (movies_list)
# pprint.pprint(get_movies_list_details())
