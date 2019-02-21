import pprint
from task_5_get_movies_list_details import get_movies_list_details
def analyse_movies_directors():
    movies_details=get_movies_list_details()
    all_directors=[]
    director=[]
    for i in movies_details:
        yo=(i['director'])
        for j in yo:
            all_directors.append(j)
            if j not in director:
                director.append(j)
    
    dict_director={}
    for a in director:
        count=0
        for b in all_directors:
            if a == b:
                count+=1
        dict_director[a]=count
    return (dict_director)
pprint.pprint(analyse_movies_directors())