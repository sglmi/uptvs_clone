from urllib import request
from bs4 import BeautifulSoup

WEBSITE_NAME = "https://www.uptvs.com" 
#url = BASE_URL + filename
#request.urlretrieve(BASE_URL, "imgsource.html")
# Read html content / text:
html_file = open("source.html")
html_text = html_file.read()
html_file.close()

soup = BeautifulSoup(html_text, "html.parser")

all_links = soup.find_all('a')


for link in all_links:
    link_addr = link.get("href")
    url = WEBSITE_NAME + link_addr
    filename = url.split('/')[-1]
    # Path for the filename
    path = "/home/saeid/Documents/Repos/uptvs_clone/img/movies/" + filename
    # download
    request.urlretrieve(url, path)
    print(filename, "successfully downloaded.")
    
    
