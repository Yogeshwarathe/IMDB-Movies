def get_movie_list_details():
	from task_1_find_movice_name import scrape_top_list
	from task_4_all_details import scrape_movies_details
	import random
	import time
	import json

	all_data=scrape_top_list()
	list_details=[]
	for i in all_data:
		url=(i['url'])
		details=scrape_movies_details(url)
		list_details.append(details)
		random_number=random.randint(1,3)
		time.sleep(random_number)
		id_1=i['url'][27:36]
		y=id_1+'.'+'json'
		with open(y,"w+") as new_file:
			json.dump(details,new_file)

	with open('all_movices_details.json',"w+") as new_file:
		json.dump(list_details,new_file)


get_movie_list_details()

