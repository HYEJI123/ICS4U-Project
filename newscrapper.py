#This is a webscraper

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests

root = "https://www.google.ca/"
link = "https://www.google.com/search?q=health&safe=strict&rlz=1C1RXQR_koCA940CA940&sxsrf=ALeKk02GvKeIkO3ng1RJOk5x7VLdYfZPYw:1617967767469&source=lnms&tbm=nws&sa=X&ved=2ahUKEwiYtabQh_HvAhV8FlkFHcqsBGwQ_AUoA3oECAIQBQ&biw=669&bih=937"

req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
with requests.Session() as c:
    soup = BeautifulSoup(webpage, 'html5lib')
    #print(soup)
    for item in soup.find_all('div', attrs={'class': 'ZINbbc xpd O9g5cc uUPGi'}):
        raw_link = (item.find('a', href=True)['href'])
        link = raw_link.split("/url?q=")[1].split('&sa=U&')[0]
        #print(item)
        title = (item.find('div', attrs={'class': 'BNeawe vvjwJb AP7Wnd'}).get_text())
        description = (item.find('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'}).get_text())

        title = title.replace(",", "")
        description = description.replace(",", "")

        time = description.split(" · ")[0]
        script = description.split(" · ")[1]
        #print(title)
        #print(link)
        #print(time)
        #print(script)
        document = open("newsdata.csv", "a")
        document.write("{}, {}, {}, {} \n".format(title, time, script, link))
        document.close()
