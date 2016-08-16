import pandas as pd

import sys
sys.path.append('../util/runner/')

import matcher
reload(matcher)

def match(members, runners):

    i=0
    max_score=[]
    match_info=[]
    
    for index, row_runners in runners.iterrows():
        max_score.append(0)
        match_info.append([])
        
        for index, row_members in members.iterrows():
                                
            score = matcher.matchRunner(row_runners.FIRST_NAME, row_runners.LAST_NAME, 20, "none", row_members['First name'], row_members['Last name'], 20, "none")
                                        
            if (score>max_score[i]):
                max_score[i]=score
                match_info[i]=[row_runners.FIRST_NAME, row_runners.LAST_NAME, row_members['First name'], row_members['Last name']]
        i=i+1

    for i in range(len(max_score)):
        #print max_score[i]," ",match_info[i]
        if (max_score[i]>3.4):
            print 'yes'
            runners.ix[i,'member']='yes'
