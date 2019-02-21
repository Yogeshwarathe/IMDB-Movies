from task_1_find_movice_name import scrape_top_list
from task_12_actors_aur_actresses_details import scrape_movie_cast
def cast_scrape_movie_details():
	import json
	with open('all_movices_details.json','r') as file_data:
		all_movices_details=json.load(file_data)
	# print(all_movices_details)
	all_list=[]
	all_movic_find_url=scrape_top_list()
	for j in range(len(all_movic_find_url)):
		one_dict=all_movices_details[j]
		# print(one_dict)
		url_one=all_movic_find_url[j]['url']
		cast=scrape_movie_cast(url_one)

		new_dict={}
		list_1=[]
		for i in one_dict:
			list_1.append(i)
		for j in list_1:
			new_dict[j]=one_dict[j]

		new_dict['cast']=cast
		all_list.append(new_dict)

	with open('scrape_movie_cast_details.json','w+') as new_file:
		json.dump(all_list,new_file)

	return(all_list)

cast_scrape_movie_details()