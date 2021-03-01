# Numerated Code Assessment: MBTA Predictor

 MBTA Predictor is a script that allows you to predict the next three stops at any given MBTA Heavy or Light Rail stop.
  

This script is written in python3 and utilizes the python modules, "datetime" and "requests". 

The user will first be given a set of route options and asked to enter which route they will be traveling on, for example:
```
 Route Options:
Red Line
Mattapan Trolley
Orange Line
Green Line B
Green Line C
Green Line D
Green Line E
Blue Line

 Which route are you travelling on today?

```

Next, the user will be given direction options and asked in which direction they will be travelling, for example:
```
 Direction Options:
South
North

 Which direction are you travelling in today?
```

Finally, the user is given a set of stops and asked which stop they will be departing from, for example:
```
 Stop Options:
Alewife
Davis
Porter
Harvard
Central
Kendall/MIT
Charles/MGH
Park Street
Downtown Crossing
South Station
Broadway
Andrew
JFK/UMass
Savin Hill
Fields Corner
Shawmut
Ashmont
North Quincy
Wollaston
Quincy Center
Quincy Adams
Braintree

 Which stop are you departing from?
```

The output results of this script are then printed to the user like so:
```
 The next departures from that stop are:

12:10

12:17

12:23

```

If any of the information is typed incorrectly, the user will be prompted to try again until their input matches one of the given options.

## Prerequisites

Before you begin, ensure you have met the following requirements listed in the requirements.txt file:
```
certifi==2020.12.5
chardet==4.0.0
idna==2.10
requests==2.25.1
urllib3==1.26.3

```


## Using MBTA Predictor

To use MBTA Predictor, follow these steps:

```
pip install -r requirements.txt
python3 MBTApredictor.py
```
