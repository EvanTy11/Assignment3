import WeatherRetriever
import dbconfig
import json
class main:


    def main():
        d = dbconfig.dbconfig("config.yaml")
        connection = d.get_redis_connection()
        #Main App Loop
        citylist = []
        while True:
            i = 0
            city = input("Enter cities you would like to get weather data and enter quit when done")

            print(len(citylist))
            if city.__eq__("quit"):

                while i < len(citylist):
                    r1 = WeatherRetriever.WeatherRetriever("https://api.openweathermap.org/data/2.5/weather?q=","d252374e5abf5d1d0c777e96c85263c1", citylist[i])
                    print(r1.getResponse(r1.Request()))
                    connection.set('city:'+citylist[i], json.dumps(r1.getResponse(r1.Request())))
                    json_data = connection.get('city:'+citylist[i])
                    data = json.loads(json_data)
                    temp = data['main']['temp']
                    print(temp)
                    i += 1
            else:
                citylist.append(city)
                print(citylist)

    if __name__ == '__main__':
        main()