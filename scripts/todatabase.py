import pandas as pd

def timetostr(time): 
    ts=time.split(':') 
    if int(ts[0])>10:
        strtime='00:'+ts[0]+':'+ts[1] 
    else:    
        strtime=ts[0]+':'+ts[1]+':'+ts[2]
    return strtime 

def parse_delmar():
    delmar=pd.read_csv('data/20160403_DelmarDash5Miler.csv')

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
        
    rotg=pd.read_csv('data/20160312_RunninoftheGreen4m.csv')

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

delmar=parse_delmar()
rotg=parse_rotg()

import sqlite3
conn=sqlite3.connect('../site/runnin/db.sqlite3')
cursor=conn.cursor()

rotg.to_sql('results_result',conn, if_exists='replace',index=False)
delmar.to_sql('results_result',conn, if_exists='append',index=False)
