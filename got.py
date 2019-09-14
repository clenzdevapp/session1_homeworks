# coding=utf8
# IMPORTS

import urllib3
from bs4 import BeautifulSoup

# URLS
url = "https://en.wikipedia.org/wiki/Game_of_Thrones"
url_wiki = "https://en.wikipedia.org"

# INITIALISIERUNG 1 WEBSITE
http = urllib3.PoolManager()
response = http.request('GET',url)#"https://en.wikipedia.org/wiki/Game_of_Thrones"
# Objekt soup von der Klasse BeautifulSoup
soup = BeautifulSoup(response.data,features='html.parser')#"https://en.wikipedia.org/wiki/Game_of_Thrones"

# MAIN
def main():
    viewers_got = 0

    # PARSING 1
    for tag in soup.findAll("th", attrs={"class":None}):
        link = tag.next#Season 1, Season 2 ...
        if str(link.string).startswith("Season") and str(link).find("title=")>0:
            url_site = url_wiki + link["href"]#url_wiki = "https://en.wikipedia.org"+/Season1-GOT.html
            # INITIALISIERUNG 2 WEBSITE
            response_site = http.request('GET',url_site)#Subpage = https://en.wikipedia.org/Season1-GOT.html
            soup_site = BeautifulSoup(response_site.data,features='html.parser')#Parsing der Subpage wird geladen
            # PARSING 2
            for tag_site in soup_site.findAll("tr", attrs={"class":"vevent"}):
                if tag_site.find("sup"):
                    viewers_got += float(tag_site.find("sup").previous.string)#Making of a sum of all GOT Watchers
                    print("...")
                    #print viewers_got

    print("\nDie Serie Game of Thrones wird auf dem aktuellen Stand von " + str(viewers_got) + " Millionen Zuschauern geschaut. Wie awesome ist das denn :-O ;-)")

    return viewers_got

if __name__ == '__main__':
    viewers_result = main()