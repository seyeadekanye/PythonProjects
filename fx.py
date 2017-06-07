#  use namedtuple for return in both functions.

import requests

from bs4 import BeautifulSoup
from collections import namedtuple


url1 = 'https://abokifx.com/'
url2 = 'https://abokifx.com/ratetypes/?rates=cbn'
rates = namedtuple('rate', {'bank_rate', 'black_market_rate'})


def get_rates_buy():
    r1 = requests.get(url1)
    r2 = requests.get(url2)
    if r1.status_code == 200 and r2.status_code == 200:
        soup1 = BeautifulSoup(r1.text, "lxml")
        soup2 = BeautifulSoup(r2.text, "lxml")
        black_market_table = soup1.find('table', {'class': 'grid-table'})
        bank_rate_table = soup2.find('table', {'class': 'grid-table'})
        bmr = black_market_table.findAll('td')[1].text
        cbn = float(bank_rate_table.findAll('td')[1].text.strip())
        aboki = float(bmr[:3])
        print(type(cbn))
        return rates(cbn, aboki)
    else:
        pass


def get_rates_sell():
    r1 = requests.get(url1)
    r2 = requests.get(url2)
    if r1.status_code == 200 and r2.status_code == 200:
        soup1 = BeautifulSoup(r1.text, "lxml")
        soup2 = BeautifulSoup(r2.text, "lxml")
        black_market_table = soup1.find('table', {'class': 'grid-table'})
        bank_rate_table = soup2.find('table', {'class': 'grid-table'})
        bmr = black_market_table.findAll('td')[1].text
        cbn = float(bank_rate_table.findAll('td')[1].text.strip())
        aboki = float(bmr[6:9])
        print(type(cbn))
        return rates(cbn, aboki)
    else:
        pass


if __name__ == '__main__':
    print(get_rates_sell())