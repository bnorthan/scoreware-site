import pandas as pd

def parse_time_string(time_string):
    split_string=time_string.split(':')
    
    print('hello')
    if len(split_string)==3:
        out_string=split_string[0]+':'+split_string[1]+':'+split_string[2]
    elif len(split_string)==2:
        out_string=split_string[0]+':'+split_string[1]
    else:
        out_string="01:20:14"
        
    return out_string
    

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
                    #newdf['time']=df[c].apply(lambda x: '00:'+x.split(':')[0]+':'+x.split(':')[1])
                    newdf['time']=df[c].apply(lambda x: parse_time_string(x))
                elif (key=='full_name'):
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



