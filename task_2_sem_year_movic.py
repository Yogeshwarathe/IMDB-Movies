from task_1_find_movice_name import scrape_top_list
import pprint

def group_by_year(all_movice):
	year_list=[]
	for i in all_movice:
		a=(i["year"])
		if a not in year_list:
			year_list.append(a)
	# print(year_list)

	big_dict={}
	for i in year_list:
		smal_list=[]
		for j in all_movice:
			y=j["year"]
			if y == i:
				smal_list.append(j)

		big_dict[i]=smal_list
	return (big_dict)

m=group_by_year(scrape_top_list())
pprint.pprint(m)