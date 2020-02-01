from bs4 import BeautifulSoup
import requests,time
from pprint import pprint
finale_dic={}
for i in range(1,3):
    solo_dic={}
    link=requests.get('https://www.flipkart.com/search?q=nikon+cameras&sid=jek%2Cp31%2Ctrv&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_0_6_na_na_na&as-pos=0&as-type=RECENT&suggestionId=nikon+cameras%7CDSLR+Camera&requestId=93c92076-347d-4092-9e3d-7fe7edd7a249&as-backfill=on&page='+str(i))
    time.sleep(2)
    soup=BeautifulSoup(link.text,'lxml')
    name=soup.find_all('div',class_="_3wU53n")
    rating=soup.find_all('div',class_="hGSR34")
    price=soup.find_all('div',class_="_1vC4OE _2rQ-NK")
    image_url=soup.find_all('div',class_="_3BTv9X")
    for j in range(len(price)):
        print(j+1)
        solo_dic[name[j].text]={}
        solo_dic[name[j].text]['Rating']=rating[j].text
        solo_dic[name[j].text]['Price']=price[j].text
        solo_dic[name[j].text]['Image Url']=image_url[j].find('img')['src']
    pprint(solo_dic)
