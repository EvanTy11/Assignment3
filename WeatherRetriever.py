import requests as r


class WeatherRetriever:

    def __init__(self, URL, KEY, CITY):
        self.response = None
        self.URL = URL
        self.KEY = KEY
        self.CITY = CITY

    # Sends request to weather API and returns url
    def Request(self):
        sendurl = self.URL + self.CITY + "&appid=" + self.KEY
        return sendurl

    # Gets the repsonce in JSON
    def getResponse(self, sendurl):
        self.response = r.get(sendurl).json()
        return self.response
