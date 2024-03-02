import requests as r
class Retriever:


    CITY = "London"
    def __init__(self, URL, KEY):
        self.URL = URL
        self.KEY = KEY

    def send(self):
        sendurl = self.URL + "q=" + self.CITY+ "&appid=" + self.KEY
        print(sendurl)
        response = r.get(sendurl).json()
        print(response)

    def print(self):

        print(self.URL)
     #def getJSON():
