import requests
import json
from markov import MarkovChain

class BuzzfeedManager:
    def __init__(self):
        self.titles = []
        
    def get(self, query):
        r = requests.get('http://www.buzzfeed.com/api/v2/feeds/'+query)
        self.buzzfeed_json = r.json()
        
    # def train(self):
    #     for titles in self.buzzfeed_json


if __name__ == '__main__':
    buzzfeed = BuzzfeedManager()
    buzzfeed.get('index')
    print buzzfeed.buzzfeed_json[0]