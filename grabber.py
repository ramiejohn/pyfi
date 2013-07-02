import requests
import pandas as pd

def get_tick(tick):
    base_url = "http://ichart.finance.yahoo.com/table.csv?s="
    r = requests.get(base_url+tick)
    splits = r.text.split('\n')
    # dic compin...
    data = { i:[] for i in splits[0].split(',')}
    header = splits[0].split(',')
    for i in splits:
        # gross.
        if 'Date' not in i:
            dlist = map(float,i.split(',')[1:len(i.split(','))])
            dlist.insert(0, i.split(',')[0])
            for i,j in enumerate(dlist):
                data[header[i]].append(j)
    # date gets DJ screwed up... filter it
    data['Date'] = filter(len,data['Date'])
    return pd.DataFrame(data)

    return pd.DataFrame(data)

