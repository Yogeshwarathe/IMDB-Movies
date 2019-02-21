from task_1_find_movice_name import scrape_top_list
import requests
import pprint
from bs4 import BeautifulSoup

link='https://www.imdb.com/title/tt0066763/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=690bec67-3bd7-45a1-9ab4-4f274a72e602&pf_rd_r=798P73ACPDZ4WP9CNEVN&pf_rd_s=center-4&pf_rd_t=60601&pf_rd_i=india.top-rated-indian-movies&ref_=fea_india_ss_toprated_tt_1'
def scrape_movies_details(url):

	data=requests.get(url)
	new_data=BeautifulSoup(data.text,'html.parser')
	name=new_data.find('div',class_='titleBar').h1.text
	a=len(name)-8
	movies_name=name[0:a]

	s=new_data.find('div',class_='subtext')
	r=s.find('time').get_text().strip().split()
	s=len(r)
	if s == 1:
		a=(r[0].split('h'))
		# print(a[0])
		runtime=int(a[0])*60
	else:
		a=(r[0].split('h'))
		b=(r[1].split('min'))
		runtime=int(a[0])*60+int(b[0])
	# print(runtime)
	poster_image=new_data.find('div', class_='poster').a['href'] 
	poster_image_url="https://www.imdb.com"+poster_image

	language=new_data.find('div',attrs={"class":"article","id":"titleDetails"})
	# print(language)
	div=language.find_all('div',class_='txt-block')
	for j in div:
		h4=j.find("h4").text
		if h4 == "Country:":
			a=j.find_all("a")
			for n in a:
				country_name=n.text
			break

	language_list=[]
	for i in div:
		h4=i.find("h4").text
		# print (h4)
		if h4=="Language:":
			a=i.find_all("a")
			# print (a.text)
			for j in a:
				# print (j.text)
				language_list.append(j.text)
			break

	director=new_data.find('div',class_='credit_summary_item')
	div=director.find_all('a')
	director_list=[]
	for i in div:
		# print(i.text)
		director_list.append(i.text)
	# print(director_list)
	p=new_data.find('div',class_='plot_summary')
	bio=p.find('div',class_='summary_text').get_text().strip()

	genre_1=new_data.find('div',attrs={'class':"article",'id':"titleStoryLine"})
	div=genre_1.find_all('div',class_='see-more inline canwrap')
	genre_list=[]
	for y in div:
		h4=y.find('h4').text
		if h4 == "Genres:":
			b=y.find_all('a')
			for l in b:
				# print(l.text)
				genre_list.append(l.text)
	# print(genre_list)
	dict_1={"name":movies_name,"director":director_list,"Country":country_name,'Language':language_list,"poster_image_url":poster_image_url,"bio":bio,"runtime":runtime,"genre":genre_list}
	return (dict_1)
# pprint.pprint(scrape_movies_details(link))