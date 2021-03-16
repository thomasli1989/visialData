import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sub1\source\sitka_weather_07-2014.csv'
try:
    with open(filename) as f:
        reader =csv.reader(f)
        header_row = next(reader)

        # for index,colum_header in enumerate(header_row):
        #    print(index,colum_header)
        dates,highs,lows = [],[],[]
        for row in reader:
            try:
                current_date = datetime.strptime(row[0],"%Y-%m-%d")
                high = int(row[1])
                low = int(row[2])
            except ValueError:
                print(current_date,'missing data')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

        #create figure
        fig = plt.figure(dpi = 128,figsize = (10,6))
        plt.plot(dates,highs,c='red',alpha = 0.5)
        plt.plot(dates,lows,c='blue',alpha = 0.5)
        plt.fill_between(dates,highs,lows,facecolor = 'blue',alpha = 0.1)

        #set figure format
        plt.title("Daily high temperature,July 2014",fontsize = 24)
        plt.xlabel('datetime',fontsize = 16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)",fontsize =16)
        plt.tick_params(axis='both',which='major',labelsize=16)
        plt.show()




except FileNotFoundError:
        print('file not found,pleae check the filename and filepath') 
