#!/usr/bin/env python3
# coding: utf-8

from datetime import datetime
from datetime import timedelta
import pandas as pd

# read csv file
my_file="check-in.csv"
df = pd.read_csv(my_file, skiprows=[0],sep=';')

#df.info()

cumul_semaine = timedelta(hours=0,minutes =0)
# first day of a week
semaine_prev = df.loc[0,'Début']
# read line in specific format
date_semaine_prev = datetime.strptime(semaine_prev, '%d/%m/%Y %H:%M')
# week number
id_semaine_prev = date_semaine_prev.strftime("%W")
# number of hours I need to do for 35h/week
left1 = left = plus1 = plus = timedelta(hours=0,minutes=0)

# display time in sepcific format
def format_time(self):
    heures=int(self.total_seconds()/3600)
    minutes=((self.total_seconds()/3600)-heures)*60
    my_format=f"{heures}h {round(minutes)}m"
    return my_format

nb_weeks=0
Total = timedelta(hours=0,minutes =0)
for index in df.index:
    time1 = df.loc[index,'Début']
    time2 = df.loc[index,'Fin']
    d1 = datetime.strptime(time1, '%d/%m/%Y %H:%M')
    id_semaine = d1.strftime("%W")
    d2 = datetime.strptime(time2, '%d/%m/%Y %H:%M')
    # difference between the 2 times clocking
    d = d2-d1
    if id_semaine == id_semaine_prev:
        cumul_semaine += d
    else:
        nb_weeks+=1
        print(f"semaine {id_semaine_prev} => {format_time(cumul_semaine)}")
        if cumul_semaine < timedelta(hours=35):
            left=timedelta(hours=35)-cumul_semaine
            print("il manque :",left,"")
            left1 += left
        else: # heures supp
            plus=cumul_semaine-timedelta(hours=35)
            plus1+=plus
        print()
        cumul_semaine = d
        id_semaine_prev = id_semaine
    # display the time at each time clocking
    Total = Total + d
    print(d1.strftime("%d/%m"),"nb heure",d)

# display total hours for the last week
print(f"semaine {id_semaine_prev} => {format_time(cumul_semaine)}")
if cumul_semaine < timedelta(hours=35):
    left=timedelta(hours=35)-cumul_semaine
    print("il manque :",left,"")
    left1 += left
else: # heures supp
    plus=cumul_semaine-timedelta(hours=35)
    plus1+=plus

# Global total
print("Durée totale    :",Total)
print("Durée en heures :",format_time(Total))
print("Nombre de semaines de travail :",nb_weeks+1)

# Total heures qu'il me manque
# Calcul avec les heures supplementaires et manquantes
if left1 > plus1:
    left2=left1-plus1
    format_time(left2)
    texte=f"Il me manque {format_time(left2)}."
else:
    plus2=plus1-left1
    texte=f"J'ai fait {format_time(plus2)} supp"

# Vrai total heures manquantes ou supp
print(f'{texte}')
