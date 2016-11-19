import pandas as pd
import operator
from difflib import SequenceMatcher

xl=pd.ExcelFile('../data/2016/Spreadsheet/Grand_Prix_2016_Post_Marathon.xls')

xl.sheet_names

df=xl.parse('Male')
df.head()

def score(age_results):
    
    dicti={}

    for row in age_results.index:
        #name=new.NameO[row]
        #print row
        #print age_results.iloc[row,2]
        name=age_results.iloc[row,2]

        p=age_results.iloc[row,1]
        if name in dicti.keys():
            points=dicti[name]
            points.append(p)
        else:
            bestmatch=0
            bestkey=None
            for key in dicti.keys():
                testmatch=SequenceMatcher(None, name, key).ratio()
                if (testmatch>bestmatch):
                    bestmatch=testmatch
                    bestkey=key
                       
            if (bestmatch>0.85):
                points=dicti[bestkey]
                points.append(p)
            else:
                dicti[name]=[p]

    totals={}

    for name in dicti:
        points=dicti[name]
        points.sort(reverse=True)
        total=points[0:6]
        totals[name]=sum(total)


    sorted_totals = sorted(totals.items(), key=operator.itemgetter(1), reverse=True)

    i=1
    for item in sorted_totals:
        print str(int(item[1]))+','+item[0]
        i=i+1

for i in range(6):
    
    new=df.ix[:,1+i*2:1+(i+1)*2]
    new=new.dropna()
    new=new.reset_index()
    score(new)
    print
    print


