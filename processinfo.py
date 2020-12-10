from requests import get
import pycountry
import time
def process():
    tmbase = 1583020800000
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4241.0 Safari/537.36'
    }
    res = get('https://covid19.who.int/page-data/table/page-data.json', headers = headers)
    dic = res.json()['result']['pageContext']['countryGroups']
    ctys = [[[], [], [], [], []], [[], [], [], [], []]]
    for elem in dic:
        code = elem['value']
        ctyres = pycountry.countries.get(alpha_2 = code)
        if ctyres is None:
            continue
        else:
            pass
        country = ctyres.name
        if country == 'United States':
            rows = elem['data']['rows']
            for row in rows:
                confirm = row[8]
                dead = row[3]
                unix = row[0]
                if unix >= tmbase:
                    ctys[0][0].append(confirm)
                    ctys[1][0].append(dead)
        elif country == 'China':
            rows = elem['data']['rows']
            for row in rows:
                confirm = row[8]
                dead = row[3]
                unix = row[0]
                if unix >= tmbase:
                    ctys[0][1].append(confirm)
                    ctys[1][1].append(dead)
        elif country == 'India':
            rows = elem['data']['rows']
            for row in rows:
                confirm = row[8]
                dead = row[3]
                unix = row[0]
                if unix >= tmbase:
                    ctys[0][2].append(confirm)
                    ctys[1][2].append(dead)
        elif country == 'Spain':
            rows = elem['data']['rows']
            for row in rows:
                confirm = row[8]
                dead = row[3]
                unix = row[0]
                if unix >= tmbase:
                    ctys[0][3].append(confirm)
                    ctys[1][3].append(dead)
        elif country == 'Mexico':
            rows = elem['data']['rows']
            for row in rows:
                confirm = row[8]
                dead = row[3]
                unix = row[0]
                if unix >= tmbase:
                    ctys[0][4].append(confirm)
                    ctys[1][4].append(dead)
    return ctys