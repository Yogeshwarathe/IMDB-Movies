def dictionary_JSON():
	from task_5_get_movies_list_details import get_movies_list_details
	details=get_movies_list_details()
	import json
	for i in details:
		id_1=i['poster_image_url'][27:36]
		y=id_1+"."+"json"
		with open(y,"w+") as file_data:
			json.dump(i,file_data)
		
dictionary_JSON()