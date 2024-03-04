import requests as r


class WeatherRetriever:

    def __init__(self, URL, KEY, CITY):
        self.response = None
        self.URL = URL
        self.KEY = KEY
        self.CITY = CITY

    def Request(self):
        '''takes URL, KEY and city and
        sends request to weather API and returns url'''
        sendurl = self.URL + self.CITY + "&appid=" + self.KEY
        return sendurl

    def getResponse(self, sendurl):
        '''takes sendurl and
        returns the response in JSON'''
        self.response = r.get(sendurl).json()
        return self.response
