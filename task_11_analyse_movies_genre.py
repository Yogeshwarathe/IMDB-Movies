import pprint 
def analyse_movies_genre():
	import json
	with open('all_movices_details.json',"r") as file_data:
		movies_data=json.load(file_data)

	all_genre_list=[]
	a_genre_list=[]
	for i in movies_data:
		y=i['genre']
		for j in y:
			all_genre_list.append(j)
			if j not in a_genre_list:
				a_genre_list.append(j)
	

	dict_genre={}
	for k in a_genre_list:
		count=0
		for l in all_genre_list:
			if k == l:
				count+=1
		dict_genre[k]=count
	return(dict_genre)

pprint.pprint(analyse_movies_genre())