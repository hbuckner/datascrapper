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
        file = open("output.txt","a")
        #file.write("hello")

        file.write(str(link.get('href'))+"\n")
    print("got here")
#testing
get_links("https://www.linode.com/docs/applications/big-data/how-to-scrape-a-website-with-beautiful-soup/")
