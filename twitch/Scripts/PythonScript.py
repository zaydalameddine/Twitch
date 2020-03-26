# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 16:48:44 2020

@author: Zayd Alameddine
"""

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

LolViewers = pd.read_csv('LolViewersByCountry.csv')
ViewersPerHour_US = pd.read_csv('NumOfViewersPerHour_US.csv')

# Bar Graph: Featured Games

# This data is taken from the Twitch features games section
# where there is a list of the top 10 featured games with
# the number of users
games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]

viewers =  [1070, 472, 302, 239, 210, 171, 170, 90, 86, 71]

# building and displaying the bar graph
plt.bar(range(len(games)), viewers, color = 'blue')
plt.title('Featured Games Viewers')
plt.legend(['Twitch'])
plt.xlabel('Games')
plt.ylabel('Viewers')

# making ax equal to the subplot as an object to get access
# to certain functions 
ax = plt.subplot()
ax.set_xticks([0,1,2,3,4,5,6,7,8,9,10])
ax.set_xticklabels(games, rotation = 30)

plt.show()

# comment the line below to see the previous plot
plt.clf()

# Pie Chart: League of Legends Viewers' Whereabouts

# taken from an SQLite Query results read in above called
# LolViewersByCountry.csv
# only going to plot 10 ten and all the countries lower
# than that are added together as Other

colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue', 'lightpink', 'darkseagreen', 'sienna', 'khaki', 'gold', 'violet', 'yellowgreen']

plt.pie(LolViewers['total'], colors=colors, shadow=True, startangle=345, autopct='%1.0f%%', pctdistance=1.15)
plt.title('League of Legends Viewers Whereabouts')
plt.legend(LolViewers['country'], loc = 'right')

plt.show()

# comment the line below to see the previous plot
#plt.clf()


# Line Graph: Time Series Analysis

plt.plot(ViewersPerHour_US['hour'], ViewersPerHour_US['viewers'])
plt.figure(figsize=(12,8))

plt.title("Time Series")

plt.xlabel("Hour")
plt.ylabel("Viewers")

ax = plt.subplot()

ax.set_xticks(ViewersPerHour_US['hour'])
ax.set_yticks([0, 3000, 6000, 9000, 12000, 15000, 18000, 21000, 24000, 27000, 30000])

y_upper = [i + (i*0.15) for i in ViewersPerHour_US['viewers']]
y_lower = [i - (i*0.15) for i in ViewersPerHour_US['viewers']]

plt.fill_between(ViewersPerHour_US['hour'], y_lower, y_upper, alpha=0.2)

plt.show()




















