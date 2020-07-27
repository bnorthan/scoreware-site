#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 09:15:23 2020

@author: bnorthan
"""
import sys

sys.path.append('../util/runner/')
sys.path.append('../util/race/')

import pandas as pd
import header
import readers
import utils



race_name='../data/2020/4_Virtual_Colonie_Mile/2020-07-25 2020 VIRTUAL COLONIE MILE Hudson Mohawk Road Runners Club.csv'

data=pd.read_csv(race_name)
racers=readers.parse_general(pd.read_csv(race_name), header.RaceHeader.headers, 1)

data['seconds']=data['Time'].apply(lambda x: utils.timeToSeconds(x))

import sqlite3
sys.path.append('../util/runner/')
conn=sqlite3.connect('../site/db.sqlite3')
cursor=conn.cursor()

data.to_sql('results_result',conn, if_exists='replace',index=False)

