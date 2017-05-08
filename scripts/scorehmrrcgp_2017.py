import pandas as pd
import sys

sys.path.append('../util/match/')
sys.path.append('../util/runner/')
sys.path.append('../util/race/')

import matchmember
reload(matchmember)
import runnerutils
import readers
reload(readers)
import header
reload(header)
import utils
reload(utils)

members_name='../data/2017/Membership/2017-05-07 Members Hudson Mohawk Road Runners Club.csv'
race_name='../data/2017/4_Masters/17masters.csv'

race_out_base='../data/2017/4_Masters/gp'

race_out_name=race_out_base+'.csv'
race_out_males=race_out_base+'_males.csv'
race_out_females=race_out_base+'_females.csv'

members=pd.read_csv(members_name)
members["age"]=members['Birthdate (e.g., 01 Jun 1954)'].apply(lambda x:utils.datestring_to_age(x))
members["gender"]=members['Gender'].apply(lambda x:utils.parse_gender(x))

print members.head()

racers=readers.parse_general(pd.read_csv(race_name), header.RaceHeader.headers, 1)
#racers=pd.read_csv(race_name)
print racers.head()

matchmember.match(members, racers, 4.5, 5.5)

print racers.head()

hmrrc=racers[racers['member']=='yes']
hmrrc=hmrrc[['place', 'first_name','last_name','gender','age']]

racers.head()

hmrrc["age_cat"]=hmrrc.age.apply(lambda x:runnerutils.ageToCat(x))

hmrrc=hmrrc.sort_values(['gender','age_cat','place'])
hmrrc['name']=hmrrc.first_name+" "+hmrrc.last_name

hmrrc.to_csv(race_out_name)

females=hmrrc[hmrrc.gender=='F']

males=hmrrc[hmrrc.gender=='M']

def getCategoryNames(hmrrc, gender, category):
    temp=hmrrc[hmrrc.gender==gender]
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

females.to_csv(race_out_females)

a_open_M=getCategoryNames(hmrrc, 'M', 'a_open')
a_30_39_M=getCategoryNames(hmrrc, 'M', 'b_30_39')
a_40_49_M=getCategoryNames(hmrrc, 'M', 'c_40_49')
a_50_59_M=getCategoryNames(hmrrc, 'M', 'd_50_59')
a_60_69_M=getCategoryNames(hmrrc, 'M', 'e_60_69')
a_70_99_M=getCategoryNames(hmrrc, 'M', 'f_70+')

males=pd.concat([a_open_M, a_30_39_M, a_40_49_M, a_50_59_M, a_60_69_M, a_70_99_M], axis=1)

males.to_csv(race_out_males)

#a_open_F=females[females.age_cat=='a_open']
#a_30_39_F=females[females.age_cat=='a_30_39']
#a_40_49_F=females[females.age_cat=='a_40_49']
#a_50_59_F=females[females.age_cat=='a_50_59']
#a_60_69_F=females[females.age_cat=='a_60_69']
#a_70_99_F=females[females.age_cat=='a_70_99']




