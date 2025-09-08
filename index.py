
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest     

jop_title=[]
companies1=[]
locations1=[]
skills1=[]
post_dates1=[]

result = requests.get("https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=Network%20Administrator")

stc=result.content

soup=BeautifulSoup(stc,"lxml")
# print(soup) 
job_titles=soup.find_all("h2",{"class":"css-193uk2c"})
companies=soup.find_all("a",{"class":"css-ipsyv7"})
locations=soup.find_all("span",{"class":"css-16x61xq"})  
skills=soup.find_all("div",{"class":"css-1rhj4yg"})
post_dates = soup.find_all("div", class_=["css-1jldrig", "css-eg55jf"])



for i in range(len(job_titles)):
    jop_title.append(job_titles[i].text)
    companies1.append(companies[i].text)
    locations1.append(locations[i].text)
    skills1.append(skills[i].text)
    post_dates1.append(post_dates[i].text)
# print(jop_title,companies1,locations1,skills1,post_dates1)


# print(len(job_titles), len(companies), len(locations), len(skills), len(post_dates))
file_list=[jop_title,companies1,locations1,skills1,post_dates1]
exported=zip_longest(*file_list)


with open("jop1.csv","w") as myfile:
    
    wr=csv.writer(myfile)
    wr.writerow(["Job Title","Company","Location","Skills","Post Date"])
    wr.writerows(exported)
