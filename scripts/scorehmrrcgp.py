import pandas as pd
import sys

sys.path.append('../util/match/')
sys.path.append('../util/runner/')

import matchmember
import runnerutils


members=pd.read_csv('../data/2016/Membership/2016-08-16 Members Hudson Mohawk Road Runners Club.csv')

print members.head()

racers=pd.read_csv('../data/2016/Tawasentha/tawasentha2_2016.csv')

print
print racers.head()

matchmember.match(members, racers)

print racers.head()

hmrrc=racers[racers['member']=='yes']
hmrrc=hmrrc[['Place','FIRST_NAME','LAST_NAME','Sex','Age']]

racers.head()

hmrrc["age_cat"]=hmrrc.Age.apply(lambda x:runnerutils.ageToCat(x))


