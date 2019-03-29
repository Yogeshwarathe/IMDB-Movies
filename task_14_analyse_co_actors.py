import json
from pprint import pprint
with open('scrape_movie_cast_details.json','r') as new_file:
	data=json.load(new_file)
# pprint(data)
coman_id = []
all_actor_dict = []
for i in data:
	a = i["cast"][0:5]
	all_actor_dict.append(a)
	for j in a:
		if j["imdb_id"] not in coman_id:
			coman_id.append(j["imdb_id"])

big_dict = {}
for y in coman_id:
	niche_wala_actor = []
	for o in coman_id:
		if y != o:
			list_2_actors = []
			list_2_actors.append(y)
			list_2_actors.append(o)
			# print(list_2_actors)
			add_2 = 0
			for g in all_actor_dict:
				add = 0
				for e in g:
					if e["imdb_id"] == y:
						first_name = e["name"]

					if e["imdb_id"] == o:
						second_a_name = e["name"]

					if e["imdb_id"] in list_2_actors:
						add+=1
				if add == 2:
					add_2+=1
					add = 0
				else:
					add = 0
			if add_2 >= 1:
				dict_1 = {'imdb_id':o,"name":second_a_name,"num_movies":add_2}
				niche_wala_actor.append(dict_1)
				add_2 = 0
			else:
				add_2 = 0
	
	big_dict[y] = {"name":first_name,"frequent_co_actors":niche_wala_actor}
pprint(big_dict)
