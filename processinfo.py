from requests import get
import pycountry
import time


def check(ccur) :
    rr = pycountry.countries.search_fuzzy(ccur)
    while(len(rr) == 0):
        ccur = input('invalid response, please enter another country: ')
        rr = pycountry.countries.search_fuzzy(ccur)
    return pycountry.countries.search_fuzzy(ccur)[0].name

def process():
    uctys = ['United States', 'China', 'India', 'Spain', 'Mexico']
    print('You can pick 5 countries by yourself')
    for i in range(5):
        cur = input('input a country: ')
        uctys[i] = check(cur)
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
        if country == uctys[0]:
            rows = elem['data']['rows']
            for row in rows:
                confirm = row[8]
                dead = row[3]
                unix = row[0]
                if unix >= tmbase:
                    ctys[0][0].append(confirm)
                    ctys[1][0].append(dead)
        elif country == uctys[1]:
            rows = elem['data']['rows']
            for row in rows:
                confirm = row[8]
                dead = row[3]
                unix = row[0]
                if unix >= tmbase:
                    ctys[0][1].append(confirm)
                    ctys[1][1].append(dead)
        elif country == uctys[2]:
            rows = elem['data']['rows']
            for row in rows:
                confirm = row[8]
                dead = row[3]
                unix = row[0]
                if unix >= tmbase:
                    ctys[0][2].append(confirm)
                    ctys[1][2].append(dead)
        elif country == uctys[3]:
            rows = elem['data']['rows']
            for row in rows:
                confirm = row[8]
                dead = row[3]
                unix = row[0]
                if unix >= tmbase:
                    ctys[0][3].append(confirm)
                    ctys[1][3].append(dead)
        elif country == uctys[4]:
            rows = elem['data']['rows']
            for row in rows:
                confirm = row[8]
                dead = row[3]
                unix = row[0]
                if unix >= tmbase:
                    ctys[0][4].append(confirm)
                    ctys[1][4].append(dead)
    return [ctys, uctys]