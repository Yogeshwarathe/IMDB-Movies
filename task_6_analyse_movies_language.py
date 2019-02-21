from task_5_get_movies_list_details import get_movies_list_details
import pprint

def analyse_movies_language():
	movies_10_list=get_movies_list_details()
	list_language=[]
	all_language=[]
	for i in movies_10_list:
		y=(i['Language'])
		for i in y:
			all_language.append(i)
			if i not in list_language:
				list_language.append(i)
	dict_1={}
	for i in list_language:
		count=0
		for j in all_language:
			if i == j:
				count+=1
		# print(i,count)
		dict_1[i]=count

	return (dict_1) 


# pprint.pprint(analyse_movies_language())
