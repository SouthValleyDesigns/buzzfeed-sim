import requests


class BuzzfeedManager:
    def __init__(self, query):
        self.query = query

    def get(self, page):
        r = requests.get('http://www.buzzfeed.com/api/v2/feeds/' + self.query + '?p=' + str(page))
        self.buzzfeed_json = r.json()

        return self.buzzfeed_json

    def read_titles(self, pages=50):
        seen = set()
        unique = []

        for page in range(pages):
            for buzz in self.get(page)['buzzes']:
                title = buzz['title']
                title = title.replace('&quot;', '\'')
                if title not in seen:
                    unique.append(title)
                    seen.add(title)
        return unique


# if __name__ == '__main__':
#     buzzfeed = BuzzfeedManager('lol')
#     buzzfeed.read_titles()
    # print buzzfeed.buzzfeed_json['buzzes'][7]['title']
