def time_to_hh_mm_ss_str(time):
    ts=time.split(':')
    if int(ts[0])>10:
        strtime='00:'+ts[0]+':'+ts[1]
    else:
        strtime=ts[0]+':'+ts[1]+':'+ts[2]
    return strtime
