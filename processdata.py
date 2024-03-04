import pandas as pd
import json
import matplotlib.pyplot as plt


class processdata:

    # Method that creates and returns are dataframe
    def createDataFrame(self, fieldlist, rowlist, db):
        i = 0
        humidity = []
        df = pd.DataFrame(columns=fieldlist, index=rowlist)
        while (i < len(rowlist)):
            humidity.clear()
            json_data = db.get(rowlist[i])
            j = 0
            data = json.loads(json_data)
            while (j < len(fieldlist)):
                redisdata = data['main'][fieldlist[j]]
                humidity.append(redisdata)
                j += 1
            df.loc[rowlist[i]] = humidity
            i += 1
        print(df)
        return df

    # Gets and prints the average
    def getAverage(self, df):
        print(df.mean())

    def getMedian(self, df):
        print(df.median())

    def getMode(self, df):
        print(df.mode())

    def gethisto(self, df):
        lst = df['temp'].tolist()
        plt.xlabel("Temperature")
        plt.ylabel("count")
        plt.hist(lst, bins=5)
        plt.show()
