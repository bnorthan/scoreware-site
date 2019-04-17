import pandas as pd

def parse_general(df, headers, id):
    

    newdf=pd.DataFrame()

    print((type(headers)))
    for key in headers:
        print((headers[key]))
        for c in df.columns:
            if c.lower() in headers[key]:
                print((c.lower()+' matches'))
                print(key)
                print(key=='name')

                if (key=='time'):
                    df[c]=df[c].replace('nan', method='bfill')
                    df[c]=df[c].fillna(method='bfill')
                    print((df[c].ix[230:240]))
                    df[c]=df[c].astype(str)
                    print((df[c].ix[230:240]))
                    newdf['time']=df[c].apply(lambda x: '00:'+x.split(':')[0]+':'+x.split(':')[1])
                elif (key=='full_name'):
                    df[c]=df[c].fillna(value='none none')
                    df[c]=df[c].replace('nan', value='none none')
                    df[c]=df[c].astype(str)
                    newdf['first_name']=df[c].apply(lambda x: x.split()[0])
                    
                    #newdf['last_name']=df[c].apply(lambda x: x.split()[-1])
                    newdf['last_name']=df[c].apply(lambda x: getLastName(x))
                    print(newdf['last_name'])
                    
                else:
                    if (key=='age'):
                        df[c]=df[c].fillna(value=40)
                    else:
                        df[c]=df[c].fillna(value='none')
                    newdf[key]=df[c]

    newdf['race_id']=id

    return newdf

def getLastName(full_name):
    split=full_name.split()
    last_name=split[1];
    for i in range(2,len(split)):
        last_name=last_name+' '+split[i]
        
    return last_name



