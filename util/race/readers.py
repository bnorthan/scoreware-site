import pandas as pd

def parse_general(df, headers, id):
    
    print('fuck YOU')

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
                    print('fuck fucking fuck you name')
                    df[c]=df[c].fillna(value='none none')
                    df[c]=df[c].replace('nan', value='none none')
                    df[c]=df[c].astype(str)
                    newdf['first_name']=df[c].apply(lambda x: x.split()[0])
                    newdf['last_name']=df[c].apply(lambda x: x.split()[-1])
                else:
                    if (key=='age'):
                        df[c]=df[c].fillna(value=40)
                    else:
                        df[c]=df[c].fillna(value='none')
                    newdf[key]=df[c]

    newdf['race_id']=id

    return newdf



