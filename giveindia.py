import requests,json
import pprint
from bs4 import BeautifulSoup
page=requests.get("https://www.giveindia.org/certified-indian-ngos")
soup=BeautifulSoup(page.text,"html.parser")

all_names=soup.findAll("div",class_="nonprofit-card-container d-flex py-2 container")
partner_list=[]
country_state_list=[]
count=0
for i in all_names:
	first=i.find("div",class_="d-flex f-d-col col-10 col-sm-10")
	first_nm=first.find("h5").text
	country=i.find("span").text
	partner_list.append(first_nm)
	country_state_list.append(country)
pprint.pprint(partner_list)
pprint.pprint(country_state_list)












# all_links=[]
# with open("task1.json",'r') as p:
# 	data=json.load(p)
# 	for i in data:
# 		all_links.append(i["url"]+''+"fullcredits?ref_=tt_cl_sm#cast")
# # pprint.pprint(all_links)
# user =int(input("enter how many movies you want"))
# for link in range(user):
# 	page=requests.get(all_links[link])
# 	soup= BeautifulSoup(page.text,"html.parser")

# 	main_div=soup.find("div",class_="redesign")
# 	table_text=main_div.find("table",class_="cast_list")
# 	trs_list=table_text.find_all("tr",class_="even")
# 	odd_list=table_text.find_all("tr",class_="odd")
# 	all_data=trs_list
# 	count_for_tr=0
# 	all_name_list=[]
# 	all_i_d_list=[]

# 	for i in trs_list:
# 		a_tag = i.find("td",class_="primary_photo")
# 		aies=a_tag.find("a")["href"][6:15]
# 		all_i_d_list.append(aies)
# 		names=a_tag.find("img")["alt"]
# 		all_name_list.append(names)


# 	for j in odd_list:
# 		a_ = j.find("td",class_="primary_photo")
# 		aie=a_.find("a")["href"][6:15]
# 		all_i_d_list.append(aie)
# 		name=a_.find("img")["alt"]
# 		all_name_list.append(name)
# 	all_list=[]
# 	for i in range(len(all_name_list)):
# 		all_dict={}
# 		all_dict["name"] = all_name_list[i]
# 		all_dict["id"] = all_i_d_list[i]
# 		all_list.append(all_dict)
# 	pprint.pprint(all_list)








