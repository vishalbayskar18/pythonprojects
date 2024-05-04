

from Client import Client 


baseUrl = 'https://api.frankfurter.app/'
date = '2017-01-02'
base = 'USD'
symbols = ['INR']


client = Client(baseUrl, date, base, symbols)

status_code, response = client.get()

print("status_code ", status_code)

print("response ", response)