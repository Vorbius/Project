import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from twilio.rest import Client

api_key =  'ACe2c82e77cde53b864010d70b6e84dfa0'
api_key_secret = '888afcb462e323fb8add6b8a952d6144'

accountSID='ACe2c82e77cde53b864010d70b6e84dfa0'
authToken='888afcb462e323fb8add6b8a952d6144'

client=Client(accountSID, authToken)

TwilioNumber='+18556740751'

myCellPhone='+12108502236'

message='You should sell now, buddy'


url = 'https://markets.businessinsider.com/cryptocurrencies'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)

webpage= urlopen(req).read()

soup=BeautifulSoup(webpage,'html.parser')

print(soup.title.text)
table_rows=soup.find_all('tr')

#print(soup.title.text)
for row in table_rows[1:6]:
    td=row.findAll('td')
    crypto_name=td[0].text
    crypto_price=td[1].text
    crypto_change=td[3].text
    crypto_ammount=td[2].text
    crypto_price=float(crypto_price.replace(',',''))
    crypto_ammount=float(crypto_ammount.replace(',',''))
    crypto_oldammount=crypto_price-crypto_ammount
    print(f'Name: {crypto_name}')
    print(f'Cost 24H ago: {crypto_oldammount}')
    print(f'Price: {crypto_price}')
    print(f'% Change in 24h: {crypto_change}')
    if crypto_name.lower() == 'ethereum':
        if crypto_price > 2000:
            textmessage=client.messages.create(to=myCellPhone, from_=TwilioNumber, body=message)
            print('Status: '+textmessage.status)
    print(input())


'''
for row in table_rows [:5]:
    crypto_name=soup.find('span',class_="Table_tableCellName__hYTfr")
    crypto_price=soup.find('div', class_="CryptoPricesTable_priceColumn__smBT5")
    crypto_change=soup.find('span', class_="TableCellChange_tableCellChangePositive__N5OmP")
    crypto_icon=soup.find('span', class_="Table_tableCellInfoSymbol__FvKrh" )
    crypto_work=soup.find('td', class_="Table_tableCell__Ejvon" )
#crypto_oldprice=float(crypto_price.text)*(1+crypto_change)
    print(crypto_name)
    print(crypto_price)
    print(crypto_change)
    print(crypto_icon)
    print(crypto_work.text)

'''