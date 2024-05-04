
import requests

class Client(object):

    def __init__(self, baseUrl, date, base, symbols) -> None:
        self.baseUrl = baseUrl
        self.date = date
        self.base = base
        self.symbols = symbols
        symbolsLiteral = self.createSymbolLiteral(symbols)
        self.actualURL = baseUrl + date + '?' + 'base=' + base + '&symbols=' + symbolsLiteral

    
    def createSymbolLiteral(self, symbols):
        symbolsLiteral = ''
        for i in range(len(symbols)-1):
            symbolsLiteral = symbolsLiteral + symbols[i] + ','

        symbolsLiteral = symbolsLiteral + symbols[-1]
        print("symbolsLiteral ", symbolsLiteral)
        return symbolsLiteral

    def get(self):
        try :
            response = requests.get(self.actualURL)
            print("response ", response.json())
            return response.status_code, response.json()

        except Exception as e:
            print("Exception ", e)
            return e

    # def post(self):
    #     try :
    #         response = requests.post(self.actualURL)
    #         print("response ", response)
    #         return response.status_code, response.json()

    #     except Exception as e:
    #         print("Exception ", e)
    #         return e
