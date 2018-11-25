import pandas as pd
import operator
from difflib import SequenceMatcher

xl=pd.ExcelFile('../data/2018/SpreadSheet/Grand_Prix_2018_Post_Stockade.xls')

xl.sheet_names


who='Male'

out_name='../data/2018/SpreadSheet/Totals__'+who+'.csv'


df=xl.parse(who)
df.head()

def score(age_results):
    
    dicti={}

    for row in age_results.index:
        #name=new.NameO[row]
        #print row
        #print age_results.iloc[row,2]
        name=age_results.iloc[row,2]

        p=age_results.iloc[row,1]
        if name in list(dicti.keys()):
            points=dicti[name]
            points.append(p)
        else:
            bestmatch=0
            bestkey=None
            for key in list(dicti.keys()):
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


    sorted_totals = sorted(list(totals.items()), key=operator.itemgetter(1), reverse=True)

    print(type(sorted_totals))
    i=1

    temp=[]
    for item in sorted_totals:
        print(str(int(item[1]))+','+item[0])
        i=i+1
        temp.append([int(item[1]),item[0]])

    sorted_totals=temp

   # return pd.DataFrame(sorted_totals, columns=['name', 'points'])
    return pd.DataFrame(sorted_totals)
scored_df=pd.DataFrame()

categories=['open', '30_39', '40_49', '50_59', '60_69', '70+']

for i in range(6):
    
    new=df.ix[:,1+i*2:1+(i+1)*2]
    new=new.dropna()
    new=new.reset_index()
    temp=score(new)
    temp
    scored_df=scored_df.join(score(new), how='outer', lsuffix='l', rsuffix='r')
    print()
    print()


print(scored_df.head())

scored_df.to_csv(out_name,index=False)
