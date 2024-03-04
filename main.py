import WeatherRetriever
import dbconfig
import json
import processdata


class main:
    ''''Main app class'''

    def main():
        '''Main Application function'''
        d = dbconfig.dbconfig("config.yaml")
        connection = d.get_redis_connection()
        defaultcitylist = ['London', 'New York', 'Miami', 'Tokyo', 'Paris', 'Singapore', 'Montreal', 'Seattle']
        citylist = []
        connection.flushdb()
        while True:

            i = 0
            menuinput = input(
                "###MainMenu###: Welcome! to add cities to retrieve weather info from type:add, to process data on cities type:process, to quit type:quit")
            fieldlist = []
            while (menuinput.__eq__("process")):

                processinput = input(
                    "###ProcessMenu###: please enter fields you want to add (Ex: humidity, temp, pressure) enter quit when you want to quit")

                if processinput.__eq__("done"):
                    df = processdata.processdata.createDataFrame(processdata, fieldlist, citylist, connection)
                    while (processinput.__eq__("done")):
                        typeofprocess = input(
                            "###SelectProcessMenu###: please enter processes you can apply to the fields you added you want to do EX: mean, median, temphistogram mode or enter:quit to quit")

                        if typeofprocess.__eq__("quit"):
                            processinput = "typeofprocessquit"
                        if typeofprocess.__eq__("mean"):
                            processdata.processdata.getAverage(processdata, df)
                        if typeofprocess.__eq__("median"):
                            processdata.processdata.getMedian(processdata, df)
                        if typeofprocess.__eq__("mode"):
                            processdata.processdata.getMode(processdata, df)
                        if typeofprocess.__eq__("histogram"):
                            processdata.processdata.gethisto(processdata, df)
                elif processinput.__eq__("quit"):
                    menuinput = "processquit"
                fieldlist.append(processinput)

            while (menuinput.__eq__("add")):
                city = input("##AddMenu## Please add a cityname(s) or enter default for a default list then enter:done")
                if city.__eq__("done"):

                    while i < len(citylist):
                        menuinput = "main"
                        r1 = WeatherRetriever.WeatherRetriever("https://api.openweathermap.org/data/2.5/weather?q=",
                                                               "d252374e5abf5d1d0c777e96c85263c1", citylist[i])
                        connection.set(citylist[i], json.dumps(r1.getResponse(r1.Request())))
                        i += 1

                elif city.__eq__("default"):
                    citylist.clear()
                    citylist = defaultcitylist
                    print(citylist)


                else:
                    citylist.append(city)
            if menuinput.__eq__("quit"):
                break

    if __name__ == '__main__':
        main()
