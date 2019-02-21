from task_1_find_movice_name import scrape_top_list
import pprint
def group_by_decade(all_movic):
	list_1=[]
	list_2=[]
	for y in range(1950,2018,10):
		list_1.append(y)
		list_2.append(y+9)

	dict_decade={}
	for j in range(len(list_1)):
		fist=list_1[j]
		last=list_2[j]
		de_list=[]
		for i in all_movic:
			y=(i['year'])
			if fist <= y and last >= y:
				de_list.append(i)
		dict_decade[fist]=de_list
	return (dict_decade)
decode=group_by_decade(scrape_top_list())
pprint.pprint(decode)


