#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 15:54:35 2019

@author: ec2-user
"""
import sys
import imp
from races.models import Race
from races.models import Result

sys.path.append('../util/runner/')
sys.path.append('../util/race/')
import header
imp.reload(header)
from header import RaceHeader

import pandas as pd
import readers
imp.reload(readers)

from localflavor.us.models import USStateField

# open hangover hald
hh=pd.read_csv('../data/2019/1_HH/HH.csv')
stockade=pd.read_csv('../data/2018/11_Stockade/stockade.csv')

hh=readers.parse_general(hh, header.RaceHeader.headers, 1)
stockade=readers.parse_general(stockade, header.RaceHeader.headers, 1)

# open stockadeathon
print(stockade.head())
print(hh.head())

print('ok')

Race.objects.all().delete()
Result.objects.all().delete()

race1=Race(race_name='Hangover Half', race_date='2019-01-01', city='Albany', state=USStateField('NY'))
race1.save()
race2=Race(race_name='Stockadeathon', race_date='2018-11-11', city='Schenectady', state=USStateField('NY'))
race2.save()

#Race.objects.bulk_create([race1,race2])


for index, r in hh.iterrows():
    runner=Result(first_name=r.first_name, last_name=r.last_name, gender=r.gender, age=r.age, city=r.city, race=race1, time=r.time)
    runner.save()
    


#Result.objects.bulk_create([runner1, runner2]);





