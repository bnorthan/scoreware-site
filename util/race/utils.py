from dateutil.parser import parse
import datetime


def time_to_hh_mm_ss_str(time):
    ts=time.split(':')
    if int(ts[0])>10:
        strtime='00:'+ts[0]+':'+ts[1]
    else:
        strtime=ts[0]+':'+ts[1]+':'+ts[2]
    return strtime

def parse_gender(gender_string):
    if str(gender_string).lower()[0]=='f':
        return 'F'
    else:
        return 'M'

def datestring_to_age(datestring):
    today=datetime.datetime.today()
    
    try: 
        dob=parse(datestring)
    except:
        dob=today

    return today.year-dob.year

def date_to_age(dates):
    num_total=0
    num_errors=0
    
    for dateString in dates:
        print dateString
        num_total=num_total+1
        try: 
            date=parse(dateString)
        except:
            date=datetime.datetime.today
            num_errors=num_errors+1

    print "Num Total: "+str(num_total)
    print "Num Erros: "+str(num_errors)
            


