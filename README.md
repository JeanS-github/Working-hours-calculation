# Working-hours-calculation
From a CSV file, calculates the hours made at each check-in. 

Displays the number of hours and missing hours per week, then the total since the 1st check in.

I use [this](https://play.google.com/store/apps/details?id=com.picca.pointage&hl=fr&gl=US) app on android to save my hours.
This is not the best app, but it's easy to use, and it save my hours is a csv file.

## Installation

Tested with python3

Packages you need :

* dateutil
* pandas

```bash
sudo pip3 install python-dateutil pandas
```

## Run

Change in the python script the filename of your CSV file (line 9, "check-in.csv").
You can also change the delimiter (I used ";").

```python
# read csv file
df = pd.read_csv("check-in.csv", skiprows=[0],sep=';')
```
And then:
```bash
./calculate-hours.py
```
## Example

The CSV file, need to be like that:

```txt
"Liste des pointages du 27/06/2021 11:05";
"Numéro";"Début";"Fin";"Commentaire"
"1";"08/06/2021 11:15";"08/06/2021 15:15";""
"2";"08/06/2021 18:30";"08/06/2021 21:30";""
"3";"09/06/2021 11:30";"09/06/2021 15:00";""
"4";"09/06/2021 20:00";"09/06/2021 23:00";""
"5";"10/06/2021 11:30";"10/06/2021 14:30";""
"6";"10/06/2021 20:00";"10/06/2021 23:00";""
"7";"11/06/2021 11:30";"11/06/2021 14:45";""
"8";"11/06/2021 20:00";"11/06/2021 23:00";""
"9";"12/06/2021 11:25";"12/06/2021 15:00";""
"10";"12/06/2021 20:00";"13/06/2021 00:00";""
"11";"15/06/2021 11:30";"15/06/2021 14:30";""
"12";"16/06/2021 20:00";"16/06/2021 22:30";""
"13";"17/06/2021 11:30";"17/06/2021 14:45";""
"14";"17/06/2021 20:00";"18/06/2021 22:45";""
"15";"18/06/2021 11:30";"18/06/2021 14:56";""
"16";"18/06/2021 20:00";"18/06/2021 23:00";""
"17";"19/06/2021 11:30";"19/06/2021 14:35";""
"18";"19/06/2021 20:00";"20/06/2021 00:00";""
"19";"22/06/2021 11:35";"22/06/2021 14:45";""
"20";"22/06/2021 20:00";"22/06/2021 22:45";""
"21";"23/06/2021 11:30";"23/06/2021 14:30";""
"22";"23/06/2021 20:00";"23/06/2021 22:45";""
"23";"24/06/2021 11:30";"24/06/2021 14:45";""
"24";"24/06/2021 20:00";"24/06/2021 22:45";""
"25";"25/06/2021 11:30";"25/06/2021 14:45";""
"26";"25/06/2021 20:00";"25/06/2021 23:45";""
"27";"26/06/2021 10:30";"26/06/2021 14:45";""
"28";"26/06/2021 19:30";"27/06/2021 00:45";""
```

## Result

You'll finally get this:

* display total hours for each check-in
* total hours per week, with the week's number
* and if you're in France, the missing hours if you work less than 35h per week
* and finally the total of working hours and the missing hours

```txt
22/06 nb heure 3:15:00
22/06 nb heure 2:45:00
23/06 nb heure 3:00:00
23/06 nb heure 2:45:00
24/06 nb heure 3:15:00
24/06 nb heure 2:45:00
25/06 nb heure 4:15:00
25/06 nb heure 3:45:00
26/06 nb heure 4:15:00
26/06 nb heure 5:15:00
semaine 25 => 35h 15m

29/06 nb heure 4:35:00
29/06 nb heure 3:05:00
30/06 nb heure 3:00:00
30/06 nb heure 2:35:00
01/07 nb heure 3:40:00
01/07 nb heure 3:05:00
02/07 nb heure 3:10:00
02/07 nb heure 3:50:00
03/07 nb heure 3:10:00
03/07 nb heure 4:30:00
semaine 26 => 34h 40m
il manque : 0:20:00

[...]

Durée totale    : 5 days, 15:55:00
Durée en heures : 135 h 55 m
Nombre de semaines de travail : 11
Il me manque    : 4 h 15 m
J'ai fait 15h 30m supp

```


