from requests import Request, Session
from pandas import json_normalize 
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import config

#Change this based on the get request type - see https://coinmarketcap.com/api/documentation/v1
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start':'1',
    'limit':'5000'
}
    # Add any parameters in your search 
    # 'cryptocurrency_type':'coins'
    # 'market_cap_max':'1500000431.14'
    # 'slug' : ['ethereum']


headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': config.API_key,
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url)
    response = session.get(url, params=parameters)
    
    data = json.loads(response.text)
    body = data['data']
    df = json_normalize(body)
    df.to_csv('.\Outputs\mydata.csv')

    # Load data to dataframe and then save to csv
    # data = json.loads(response.text)
    # df = json_normalize(data)
    # df.to_csv('.\Outputs\mydata.csv', index=False)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)