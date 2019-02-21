import pprint
def analyse_language_and_directors():
	import json

	with open('all_movices_details.json','r') as file_data:
		movices=json.load(file_data)

	movices_details=movices
	director_list=[]
	for i in movices_details:
		y=i['director']
		for j in y:
			if j not in director_list:
				director_list.append(j)
	# print(director_list)
	dict_1={}
	for y in director_list:
		all_list=[]
		list_1=[]
		for a in movices_details:
			j=a['director']
			for b in j:
				if y == b:
					z=a['Language']
					for i in z:
						all_list.append(i)
						if i not in list_1:
							list_1.append(i)
		dict_use={}
		for k in list_1:
			add=0
			for m in all_list:
				if k == m:
					add+=1
			dict_use[k]=add
		dict_1[y]=dict_use

	return(dict_1)

pprint.pprint(analyse_language_and_directors())