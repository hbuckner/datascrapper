from urllib3 import *
from bs4 import BeautifulSoup

#get_links: TAKES: string as url  RETURNS: string as links
def get_links(url):
    manager = PoolManager()
    r=manager.request('GET', url)
    file = open("output.txt","w")
    a="done"
    soup = BeautifulSoup(r,'lxml')
    print(soup.find_all('a'))
    for link in soup.find_all('a'):
        print(link.get('href'))
        file = open("output.txt","r+")
        file.write("hello")
        file.write("we made it "+str(link.get("href")))
    print("got here")
#testing
get_links("https://github.com/bulkan/robotframework-requests/issues/135")
