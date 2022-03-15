import pandas as pd
import sys
import time
from bs4 import BeautifulSoup
import requests


def get_crypto_prices(cryptocurrencies):
    priceValues = []
    for currency in cryptocurrencies:
        try:
            page = requests.get(f'https://coinmarketcap.com/currencies/{currency}/')
            soup = BeautifulSoup(page.content, 'html.parser')
            price = soup.find('div', class_='priceValue').text
            priceValues.append(price)
        except AttributeError:
            continue   
    prices = {crypto:value for crypto,value in zip(cryptocurrencies, priceValues)}
    print(prices)
    data = pd.DataFrame(prices, index=[1])
    data.set_index('bitcoin', inplace=True)
    return data
    
get_crypto_prices(['bitcoin', 'ethereum', 'tether', 'solana', 'cardona', 'binance coin', 'bnb', 'avalanche', 'xrp'])
