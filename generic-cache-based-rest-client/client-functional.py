

import requests
import threading


def createSymbolLiteral(symbols):

    symbolsLiteral = ''
    for i in range(len(symbols)-1):
        symbolsLiteral = symbolsLiteral + symbols[i] + ','

    symbolsLiteral = symbolsLiteral + symbols[-1]
    print("symbolsLiteral ", symbolsLiteral)
    return symbolsLiteral

lcache = {}

def client(baseUrl, date, base, symbols):
    global lcache
    symbolsLiteral = createSymbolLiteral(symbols)
    actualUrl = baseUrl + date + '?' + 'base=' + base + '&symbols=' + symbolsLiteral
    print("actualUrl", actualUrl)

    lock = threading.Lock()

    try :
        key = baseUrl+'-'+date+'-'+base+'-'+symbolsLiteral
        if key in lcache:
            return lcache[key]

        lock.acquire()
        if key in lcache:
            return lcache[key]
        reponse = requests.get(actualUrl)
        lcache[key] = reponse.json()

        lock.release()

        return reponse.json()


    except Exception as e:
        print("Exception ", e)





# symbols = ['USD1', 'USD2', 'USD3']


baseUrl = 'https://api.frankfurter.app/'
date = '2017-01-02'
base = 'USD'
symbols = ['INR']
#client(baseUrl, date, base, symbols)




clients = []
for i in range(100):
    t = threading.Thread(target=client, args=(baseUrl, date, base, symbols))
    clients.append(t)

for t in clients:
    t.start()

for t in clients:
    t.join()










