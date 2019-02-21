import json
import pprint
with open('scrape_movie_cast_details.json','r') as new_data:
	data=json.load(new_data)
# pprint.pprint(data)

def analyse_actors(movies_list):
	all_id_list=[]
	cast_list=[]
	for i in movies_list:
		id_a=i['cast']
		for j in id_a:
			cast_list.append(j)
			all_id_list.append(j['imdb_id'])
	# print(id_list)
	# pprint.pprint(cast_list)
	id_not_ripited=[]
	for j in all_id_list:
		if j not in id_not_ripited:
			id_not_ripited.append(j)
	# print(id_not_ripited)
	big_dict={}
	for k_id in id_not_ripited:
		# print(k)
		for m_dict in cast_list:
			if k_id == m_dict['imdb_id']:
				name=m_dict['name']
				# print(name)
		num_movies=0
		for all_id in all_id_list:
			if k_id == all_id:
				num_movies+=1
		smal_dict={'name':name,'num_movies':num_movies}
		big_dict[k_id]=smal_dict
	pprint.pprint(big_dict)


analyse_actors(data)