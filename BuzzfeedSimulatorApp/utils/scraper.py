from bs4 import BeautifulSoup
import requests
import re
import urllib2
import cookielib
import json

def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

class ImageScraper:
    def __init__(self):
        self.header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
        }

    def get_image(self, query):
        query = query.split()
        query ='+'.join(query)
        self.url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
        soup = get_soup(self.url,self.header)


        ActualImages=[]
        for a in soup.find_all("div",{"class":"rg_meta"}):
            link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
            ActualImages.append((link,Type))

        if ActualImages:
            return ActualImages[0][0]
