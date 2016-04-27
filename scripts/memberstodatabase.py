import pandas as pd

from datetime import datetime

members=pd.read_excel('data/members.xls')


membersdf=pd.DataFrame()

membersdf['id']=range(members.shape[0])
membersdf['first_name']=members['First name']
membersdf['last_name']=members['Last name']

#membersdf['date_birth']=datetime.strptime(members['Birthdate (e.g., 01 Jun 1954)'])
bd='Birthdate (e.g., 01 Jun 1954)'
   
    
def megadate(datestr):    
    try:
        return datetime.strptime(datestr, '%d %b %Y')
    except:
        pass
    try:
        return datetime.strptime(datestr, '%d %B %Y')
    except:
        return datetime(1900,1,1,1,1)
 
birthdates=[]

for i in range(members.shape[0]):
    birthdates.append(megadate(members[bd].iloc[i]))

membersdf['date_birth']=birthdates
membersdf['gender']=members['Gender']
membersdf['city']=members['City']
membersdf['state']=members['State']

import sqlite3

conn=sqlite3.connect('../site/runnin/db.sqlite3')
cursor=conn.cursor()
membersdf.to_sql('results_member',conn, if_exists='replace',index=False)
    
        
