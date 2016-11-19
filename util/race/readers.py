import pandas as pd

def parse_general(df, headers, id):

    newdf=pd.DataFrame()

    print type(headers)
    for key in headers:
        print headers[key]
        for c in df.columns:
            if c.lower() in headers[key]:
                print c.lower()+' matches'

                if (key=='time'):
                    newdf['time']=df.Time.apply(lambda x: '00:'+x.split(':')[0]+':'+x.split(':')[1])
                elif (key=='full_name'):
                    df[c]=df[c].astype(str)
                    newdf['first_name']=df[c].apply(lambda x: x.split(' ',1)[0])
                    newdf['last_name']=df[c].apply(lambda x: x.split(' ',1)[-1])
                else:
                    newdf[key]=df[c]

    newdf['race_id']=id

    return newdf



