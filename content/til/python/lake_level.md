---
title: Clear Lake level, with pandas
date: 2024-02-08
draft: false
categories:
  - TIL
tags:
  - python
  - til
---

I live on Clear Lake, and watching the level rise and fall is one of my 
minor obsessions. 

Clear Lake has a special way of measuring the height of the Lake. It uses
the 'Rumsey Scale.' There are some nuances, but pretty much a guy named 
Rumsey put a stick in the mud, and set zero Rumsey to be at the natural
low water level of 1318.257 feet above mean sea level.

The low water mark being when water stops flowing over the 'Grigsby Riffle'
(I think).

The USGS [has a page with the Rumsey level](https://waterdata.usgs.gov/monitoring-location/11450000/#parameterCode=00065&period=P7D&showMedian=false), and you can download the data in a tab 
delimited file.

A further bit of trivia is that a full lake is defined as 7.56 feet on 
the Rumsey scale.

In fall of 2022, after two years of drought, the lake hit a record low 
of -2.74 feet, and then multiple atmospheric rivers hit California, and the lake
rose over six feet, from -2.3ft to +4 ft, in just over three weeks, and rose
another four feet in the next two months. 

When the lake hits 8 feet they release water from the Cache Creek dam, and usually
that is enough to avoid flooding. But if there is a lot of rain the inflow is 
greater than their ability to regulate the water. 

So exciting.

It felt like this year we are on track to get a full lake earlier than in the past.

Last year we hit full lake on 3/14/2023. And the earliest appears to be in 2017 on Jan 20th. 


Here is some code

    Also see /todo/clearlake/lake/lake.py

````
import pandas as pd
import pdb

FULL_LAKE = 7.56
df = pd.read_table('lake_level.txt', comment='#')
df['datetime']=pd.to_datetime(df['datetime'])
df_full_lake=df[df['15867_00065']>=FULL_LAKE]
print( df_full_lake[['datetime','15867_00065']].groupby(df_full_lake['datetime'].dt.year).agg(['min', 'max']))
print( df[['datetime','15867_00065']].groupby(df['datetime'].dt.year).agg(['min', 'max']))
print( df[['datetime','15867_00065']].groupby(df['datetime'].dt.date).agg(['min', 'max']))
````
