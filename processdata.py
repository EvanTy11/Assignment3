import pandas as pd
import json
import matplotlib.pyplot as plt


class processdata:
    '''Class used to create a data frame and process that data acording to the users needs'''

    def createDataFrame(self, fieldlist, rowlist, db):
        '''takes column list and rowlist and db connection and creates a dataframe
        then returns the dataframe'''
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

    def getAverage(self, df):
        '''takes the dataframe and prints the average'''
        print(df.mean())

    def getMedian(self, df):
        '''takes the dataframe and prints the median'''
        print(df.median())

    def getMode(self, df):
        '''takes in the dataframe and prints the mode'''
        print(df.mode())

    def gethisto(self, df):
        '''takes in the dataframe and returns a histogram based on the temperature'''
        lst = df['temp'].tolist()
        plt.xlabel("Temperature")
        plt.ylabel("count")
        plt.hist(lst, bins=5)
        plt.show()
