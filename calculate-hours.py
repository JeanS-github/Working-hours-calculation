#!/usr/bin/env python3
# coding: utf-8

from datetime import datetime
from datetime import timedelta
import pandas as pd

# read csv file
df = pd.read_csv("check-in.csv", skiprows=[0],sep=';')

#df.info()

cumul_semaine = timedelta(hours=0,minutes =0)
# first day of a week
semaine_prev = df.loc[0,'Début']
# read line in specific format
date_semaine_prev = datetime.strptime(semaine_prev, '%d/%m/%Y %H:%M')
# week number
id_semaine_prev = date_semaine_prev.strftime("%W")
# number of hours I need to do for 35h/week
left1 = left = timedelta(hours=0,minutes=0)

Total = timedelta(hours=0,minutes =0)
for index in df.index:
    time1 = df.loc[index,'Début']
    time2 = df.loc[index,'Fin']
    d1 = datetime.strptime(time1, '%d/%m/%Y %H:%M')
    id_semaine = d1.strftime("%W")
    #print("id semaine =",id_semaine)
    d2 = datetime.strptime(time2, '%d/%m/%Y %H:%M')
    d = d2-d1
    if id_semaine == id_semaine_prev:
        cumul_semaine += d
    else:
        heures=int(cumul_semaine.total_seconds()/3600)
        minutes=((cumul_semaine.total_seconds()/3600)-heures)*60
        print("semaine",id_semaine_prev,"=>",heures,"h",round(minutes),"m")
        if cumul_semaine < timedelta(hours=35):
            left=timedelta(hours=35)-cumul_semaine
            print("il manque :",left,"")
            left1 += left
        print()
        cumul_semaine = d
        id_semaine_prev = id_semaine
    # display the time at each time clocking
    Total = Total + d
    print("nb heure",d)
# display total hours for the last week
heures=int(cumul_semaine.total_seconds()/3600)
minutes=((cumul_semaine.total_seconds()/3600)-heures)*60
print("semaine",id_semaine_prev,"=>",heures,"h",round(minutes),"m")
if cumul_semaine < timedelta(hours=35):
    left=timedelta(hours=35)-cumul_semaine
    print("il manque :",left,"")
    left1 += left

# Global total
heures=int(Total.total_seconds()/3600)
minutes=((Total.total_seconds()/3600)-heures)*60
print("\nDurée totale    :",Total)
#print("Durée en heures2: ",Total.total_seconds()/60/60)
print("Durée en heures :",heures,"h",round(minutes),"m")
heures=int(left1.total_seconds()/3600)
minutes=((left1.total_seconds()/3600)-heures)*60
print("Il me manque    :",heures,"h",round(minutes),"m")

