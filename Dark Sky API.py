import sys
import numpy

sys.path.insert( 1, 'C:/Users/healey/python/modules' )

from forecastiopy import * 

api_key = 'ccba47305cec42476fcbcc3b6892bd24'

loc = [\
       ["Anchorage, Alaska", 61.2181, -149.9003 ],\
       ["Buenos Aires, Argentina", -34.6037, -58.3816 ],\
       ["Sao Jose dos Campos, Brazil", -23.2237, -45.9009 ],\
       ["San Jose, Costa Rica", 9.9281, -84.0807 ],\
       ["Nanaimo, Canada", 49.1659, -123.9401 ],\
       ["Ningbo, China", 29.8683, 121.5440 ],\
       ["Giza, Egypt", 30.0131, 31.2089 ],\
       ["Mannheim, Germany", 49.4875, 8.4660 ],\
       ["Hyderabad, India", 17.3850, 78.4867 ],\
       ["Tehran, Iran", 35.6892, 51.3890 ],\
       ["Bishkek, Kyrgyzstan", 42.8746, 74.5698 ],\
       ["Riga, Latvia", 56.9496, 24.1052 ],\
       ["Quetta, Pakistan", 30.1798, 66.9750 ],\
       ["Warsaw, Poland", 52.2297, 21.0122 ],\
       ["Dhahran, Saudia Arabia", 26.2361, 50.0393 ],\
       ["Madrid, Spain", 40.4168, -3.7038 ],\
       ["Oldham, United Kingdom", 53.5409, -2.1114 ],\
]
import csv

with open('temp.csv', 'w') as csvFile:
    output = csv.writer(csvFile)
    output.writerow( ['City', 'Min 1', 'Max 1', 'Min 2', 'Max 2',
                      'Min 3', 'Max 3', 'Min 4', 'Max 4', 'Min 5',
                      'Max 5', 'Min AVG', 'Max AVG'] )    
    for i in range(len(loc)):
        city=[]
        city.append(loc[i])
        weather = ForecastIO.ForecastIO(api_key, units=ForecastIO.ForecastIO.UNITS_SI,
                                        lang=ForecastIO.ForecastIO.LANG_ENGLISH, 
                                        latitude=loc[i][1], longitude=loc[i][2])
        print('Latitude', weather.latitude, 'Longitude', weather.longitude)
        print('Timezone', weather.timezone, 'Offset', weather.offset)
        current = FIOCurrently.FIOCurrently(weather)
        print(loc[i])
        print('Currently: ' + str(current.get()['temperature']))
        daily = FIODaily.FIODaily(weather)
        print()
        print('Daily')
        print('Summary:', daily.summary)
        print('Icon:', daily.icon)
        for day in range(2, 7):
            print('Day', day -1, end = ': (')
            val = daily.get(day)
            print( str( val[ 'temperatureMin' ] ), end = ',' )
            print( str( val[ 'temperatureMax' ] ) + ')' )
            city.append(val[ 'temperatureMin' ])
            city.append(val[ 'temperatureMax' ])
        min_list=[city[1], city[3], city[5], city[7], city[9]]
        max_list=[city[2], city[4], city[6], city[8], city[10]]
        min_avg=round(numpy.mean(min_list),2)
        max_avg=round(numpy.mean(max_list),2)
        city.append(min_avg)
        city.append(max_avg)
        output.writerow( city )


