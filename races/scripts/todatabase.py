import pandas as pd

import sys
import imp
sys.path.append('../util/race/')
import header
imp.reload(header)
from header import RaceHeader

def timetostr(time): 
    ts=time.split(':') 
    if int(ts[0])>10:
        strtime='00:'+ts[0]+':'+ts[1] 
    else:    
        strtime=ts[0]+':'+ts[1]+':'+ts[2]
    return strtime 

def parse_delmar():
    delmar=pd.read_csv('../data/2016/20160403_DelmarDash5Miler.csv')

    delmardf=pd.DataFrame()
    #delmardf['PLACE']=results.Place
    #delmardf['id']=rotg.index
    delmardf['time']=delmar.Time.apply(lambda x: timetostr(x))
    delmardf['race_id']=2
    delmardf['member_id']=0
    delmardf['first_name']=delmar.First_Name
    delmardf['last_name']=delmar.Last_Name
    delmardf['gender']=delmar.Sex
    delmardf['city']=delmar.City
    delmardf['state']=delmar.State
    delmardf['age']=delmar.Age
    delmardf['bib']=delmar.Bib
    delmardf['pace']=delmar['NET Pace']
    delmardf['splits']=delmar['1M']+','+delmar['2M']+','+delmar['3M']+','+delmar['4M']+','+delmar['5M']
    #delmardf['YEAR']=2016i

    return delmardf


def parse_rotg():
        
    rotg=pd.read_csv('../data/2016/20160312_RunninoftheGreen4m.csv')

    rotgdf=pd.DataFrame()
    #rotgdf['PLACE']=results.Place
    rotgdf['id']=rotg.index
    rotgdf['time']=rotg.Time.apply(lambda x: '00:'+x.split(':')[0]+':'+x.split(':')[1])
    rotgdf['race_id']=1
    rotgdf['member_id']=0
    rotgdf['first_name']=rotg.Name.apply(lambda x: x.split(' ',1)[0])
    rotgdf['last_name']=rotg.Name.apply(lambda x: x.split(' ',1)[1])
    rotgdf['gender']=rotg.Sex
    rotgdf['city']=rotg.City
    rotgdf['state']=rotg.State
    rotgdf['age']=rotg.Age
    rotgdf['bib']=rotg.Bib
    rotgdf['pace']=rotg.Pace
    rotgdf['splits']='00:00'

    return rotgdf

def parse_general(df, headers, id):

    newdf=pd.DataFrame()

    print(type(headers))
    for key in headers:
        print(headers[key])
        for c in df.columns:
            if c.lower() in headers[key]:
                print(c.lower()+' matches')

                if (key=='time'):
                    df.Time=df.Time.astype(str)
                    newdf['time']=df.Time.apply(lambda x: '00:'+x.split(':')[0]+':'+x.split(':')[1])
                else:
                    newdf[key]=df[c]
    newdf['race_id']=id

    return newdf


#delmar=parse_delmar()
#rotg=parse_rotg()

#masters=parse_general(pd.read_csv('../data/2016/masters10k.csv'),RaceHeader.headers,3)
#ds=parse_general(pd.read_csv('../data/2016/DistinguishedService.csv'), RaceHeader.headers,4)

hh=parse_general(pd.read_csv('../data/2019/1_HH/HH.csv'), RaceHeader.headers,4)
stockade=parse_general(pd.read_csv('../data/2018/11_Stockade/stockade.csv'), RaceHeader.headers,5)
#hh=pd.read_csv('../data/2019/1_HH/HH.csv');

print(hh.head())
'''
import sqlite3
#sys.pyath.append('../util/runner/')
conn=sqlite3.connect('../../mysite/db.sqlite3')
cursor=conn.cursor()
hh['id']=hh.index;
hh['state']='NY'
hh['bib']=100;
hh['pace']='00:00'
hh['splits']='00:00'
hh['member_id']=0
hh.to_sql('races_result',conn, if_exists='replace')
'''

#rotg.to_sql('results_result',conn, if_exists='replace',index=False)
#delmar.to_sql('results_result',conn, if_exists='append',index=False)
#masters.to_sql('results_result', conn, if_exists='append', index=False)
#ds.to_sql('results_result', conn, if_exists='append', index=False)
