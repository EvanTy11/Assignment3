import WeatherRetriever
import dbconfig
import json
import processdata


class main:
    ''''Main app class for weather update app'''

    def main():
        '''Main Application function for app menu'''
        d = dbconfig.dbconfig("config.yaml")
        #Redis connection
        connection = d.get_redis_connection()
        defaultcitylist = ['London', 'New York', 'Miami', 'Tokyo', 'Paris', 'Singapore', 'Montreal', 'Seattle']
        citylist = []
        connection.flushdb()
        #Main loop
        while True:

            i = 0
            menuinput = input(
                "###MainMenu###: Welcome! to add cities to retrieve weather info from type:add, to process data on cities type:process, to quit type:quit")
            fieldlist = []
            #Process loop where a user can input fields they want to call agg funcs on
            while (menuinput.__eq__("process")):

                processinput = input(
                    "###ProcessMenu###: please enter fields you want to add (Ex: humidity, temp, pressure) enter quit when you want to quit")
                #User is done adding fields to dataframe
                if processinput.__eq__("done"):
                    df = processdata.processdata.createDataFrame(processdata, fieldlist, citylist, connection)
                    #Processing func call loop
                    while (processinput.__eq__("done")):
                        typeofprocess = input(
                            "###SelectProcessMenu###: please enter processes you can apply to the fields you added you want to do EX: mean, median, temphistogram mode or enter:quit to quit")
                        #Processing checks from user input calling processing func depending on what we get from user
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
            # add loop where users can input cities they want to retrieve weather info from Ex London, Paris, Mumbai, Tokyo, all in real time
            while (menuinput.__eq__("add")):
                city = input("##AddMenu## Please add a cityname(s) or enter default for a default list then enter:done")
                #User is done and checks occur
                if city.__eq__("done"):

                    while i < len(citylist):
                        menuinput = "main"
                        #Passing api key & url to Retriever class
                        r1 = WeatherRetriever.WeatherRetriever("https://api.openweathermap.org/data/2.5/weather?q=",
                                                               "d252374e5abf5d1d0c777e96c85263c1", citylist[i])
                        #storing key,JSON in Redis
                        connection.set(citylist[i], json.dumps(r1.getResponse(r1.Request())))
                        i += 1
                # if user selects default option
                elif city.__eq__("default"):
                    citylist.clear()
                    citylist = defaultcitylist
                    print(citylist)

                #adding cities onto list
                else:
                    citylist.append(city)
            #App Exits
            if menuinput.__eq__("quit"):
                break

    if __name__ == '__main__':
        main()
