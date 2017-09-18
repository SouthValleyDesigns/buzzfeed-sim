import requests
import json
from markov import MarkovChain

class BuzzfeedManager:
    def __init__(self):
        self.titles = []
        
    def get(self, query, page):
        r = requests.get('http://www.buzzfeed.com/api/v2/feeds/'+query'?p='+page)
        self.buzzfeed_json = r.json()
        
        
    def train(self, pages=10):
        for page in range(pages):
            for buzz in self.buzzfeed_json['buzzes']:
                print buzz['title'].replace('&quot;', '\'')


    buzzfeed.get('lol')
    buzzfeed = BuzzfeedManager()
    buzzfeed.get('lol')
    buzzfeed.train()
    # print buzzfeed.buzzfeed_json['buzzes'][7]['title']