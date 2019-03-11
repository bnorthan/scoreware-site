import pandas as pd
import sys

sys.path.append('../util/match/')
sys.path.append('../util/runner/')

import matchmember
import runnerutils


members=pd.read_csv('../data/2017/Membership/2017-01-03 Members Hudson Mohawk Road Runners Club.csv')

print(members.head())

racers_base='../data/2017/1_HH/17Hangover_half'
racers=pd.read_csv(racers_base+'.csv')

print()
print(racers.head())

matchmember.match(members, racers)

print(racers.head())

hmrrc=racers[racers['member']=='yes']
hmrrc=hmrrc[['Place','FIRST_NAME','LAST_NAME','Sex','Age']]

racers.head()

hmrrc["age_cat"]=hmrrc.Age.apply(lambda x:runnerutils.ageToCat(x))

hmrrc=hmrrc.sort_values(['Sex','age_cat','Place'])
hmrrc['name']=hmrrc.FIRST_NAME+" "+hmrrc.LAST_NAME

hmrrc.to_csv(racers_base+'_hmrrc.csv')

sdlkfj
females=hmrrc[hmrrc.Sex=='F']

males=hmrrc[hmrrc.Sex=='M']

def getCategoryNames(hmrrc, gender, category):
    temp=hmrrc[hmrrc.Sex==gender]
    temp=temp[temp.age_cat==category]
    temp=temp.reset_index(drop=True)
    temp=temp.name
    scored=pd.DataFrame()
    scored['score']=[12,10,8,7,6,5,4,3,2,1]
    scored['name']=temp
    return scored

a_open_F=getCategoryNames(hmrrc, 'F', 'a_open')
a_30_39_F=getCategoryNames(hmrrc, 'F', 'b_30_39')
a_40_49_F=getCategoryNames(hmrrc, 'F', 'c_40_49')
a_50_59_F=getCategoryNames(hmrrc, 'F', 'd_50_59')
a_60_69_F=getCategoryNames(hmrrc, 'F', 'e_60_69')
a_70_99_F=getCategoryNames(hmrrc, 'F', 'f_70+')

females=pd.concat([a_open_F, a_30_39_F, a_40_49_F, a_50_59_F, a_60_69_F, a_70_99_F], axis=1)

females.to_csv('../data/2016/Tawasentha/females_scored.csv')

a_open_M=getCategoryNames(hmrrc, 'M', 'a_open')
a_30_39_M=getCategoryNames(hmrrc, 'M', 'b_30_39')
a_40_49_M=getCategoryNames(hmrrc, 'M', 'c_40_49')
a_50_59_M=getCategoryNames(hmrrc, 'M', 'd_50_59')
a_60_69_M=getCategoryNames(hmrrc, 'M', 'e_60_69')
a_70_99_M=getCategoryNames(hmrrc, 'M', 'f_70+')

males=pd.concat([a_open_M, a_30_39_M, a_40_49_M, a_50_59_M, a_60_69_M, a_70_99_M], axis=1)

males.to_csv('../data/2016/Tawasentha/males_scored.csv')

#a_open_F=females[females.age_cat=='a_open']
#a_30_39_F=females[females.age_cat=='a_30_39']
#a_40_49_F=females[females.age_cat=='a_40_49']
#a_50_59_F=females[females.age_cat=='a_50_59']
#a_60_69_F=females[females.age_cat=='a_60_69']
#a_70_99_F=females[females.age_cat=='a_70_99']




