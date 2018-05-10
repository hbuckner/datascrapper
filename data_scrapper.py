from urllib3 import *
import bs4

#get_links: TAKES: string as url  RETURNS: string as links
def get_links(url):
    manager = PoolManager()
    r=manager.request( 'GET',url)
    print(r)
    file = open("output.txt","w")
    a="done"
    #print(str(r.data))
    soup = bs4.BeautifulSoup(r.data,'lxml')
    for link in soup.find_all('a'):
        print(link)
        file = open("output.txt","a+")
        #file.write("LINKS")
        if (str(link.get('href'))[0:4] =="http"):
            file.write(str(link.get('href'))+"\n")
    print("got here")

def get_text(url):
    manager = PoolManager()
    r=manager.request( 'GET',url)
    print(r)
    #file = open("output2.txt","w")
    soup = bs4.BeautifulSoup(r.data,'lxml')
    for link in soup.find_all('p'):
        print(link)
        file = open("output.txt","a+")
        #file.write("TEXT")
        file.write(link.text+"\n")
    print("got here")
#testing
get_links("https://www.linode.com/docs/applications/big-data/how-to-scrape-a-website-with-beautiful-soup/")
get_text("https://www.linode.com/docs/applications/big-data/how-to-scrape-a-website-with-beautiful-soup/")
