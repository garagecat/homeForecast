#!/usr/bin/python
#-*-coding: utf-8 -*-

# rimkov - homeForecast
# DHT22 polling with Raspberry pi and graph data with Plotly
# launched by crontab every 15 minutes

from plotly.offline import plot
import plotly.graph_objs as go
import csv, time, datetime
import os, gzip, shutil
import Adafruit_DHT, time

datafile = "/home/pi/Documents/homeForecast/homeData.csv"
htmlfile = "/var/www/html/homeForecast.html"

date = time.strftime('%Y-%m-%d %H:%M:%S')

#gpio pi number
pin = 23
#polling sensor type 22 (dht22)
humidity, temp = Adafruit_DHT.read_retry(22, pin)

humidity = '%0.2f' % humidity
temp = '%0.2f' % temp
data = []
data.append(date)
data.append(temp)
data.append(humidity)
#write to data file
with open(datafile, "a") as f_data:
    wr = csv.writer(f_data)
    wr.writerow(data)

#read from data file
graphData = []
with open(datafile, "r") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        graphData.append(row)

#headers = graphData.pop(0)
date = []
temp = []
hum = []
for item in graphData:
    date.append(item[0])
    temp.append(item[1])
    hum.append(item[2])

trace1 = go.Scatter(
         x = date,
         y = temp,
         mode = 'lines',
         name = 'Temperature °',
         line = dict (
              width = 2,
              color = ('rgb(249, 255, 0)')))

trace2 = go.Scatter(
         x = date,
         y = hum,
         mode = 'lines',
         name = 'Humidite %',
         line = dict (
              width = 2,
              color = ('rgb(0, 210, 255)')))

fig = [trace1, trace2]
layout = go.Layout(
paper_bgcolor = 'rgb(0, 0, 0)',
plot_bgcolor = 'rgb(0, 0, 0)',
title = "{2} - Temperature {0}° / Humidite {1}%".format(temp[-1], hum[-1], date[-1]),
xaxis = dict(
        title="date",
        type="date",
        autorange=True,
        linewidth = 2,
    ),
yaxis = dict(
        title="mesure",
        autorange=True,
        linewidth = 2,
    )
)

#offline plot to html file
plot({"data": fig,"layout": layout},filename=htmlfile,auto_open=False)
