# Essentially I want this program to take in a csv file in the current OHS
# format, and then alert me if any therapists' License expire within a month.
# Can be extended to alert for birthdays (1 week), Liability insurance (1 month)

import pandas as pd

from datetime import datetime


class OptimumDates:

    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.data = pd.read_csv(self.csv_file)

    def get_lic_dates(self):
        lic_dates = self.data.iloc[:, [1, 2, 7]].dropna(thresh=3)
        return lic_dates.iloc[:, [2]]

    def get_liab_dates(self):
        liab_dates = self.data.iloc[:, [1, 2, 6]].dropna(thresh=3)
        return liab_dates.iloc[:, [2]]

    def get_bcheck_dates(self):
        bcheck_dates = self.data.iloc[:, [1, 2, 8]]
        return bcheck_dates.iloc[:, [2]]

# df = OptimumDates(file)
# print(df.get_liab_dates())


def main():
    file = 'Optimum.csv'
    lic = OptimumDates(file)
    options = ['List Current Exp. License Dates', 'List Current Liability Insurance Exp. Dates',
               'List Last Background Check Dates']
    x = input('What will you like to do?\n 1.){}\n 2.){}\n 3.){}\n'.format(options[0], options[1], options[2]))
    if x == '1':
        print(lic.get_lic_dates())
    elif x == '2':
        print(lic.get_liab_dates())
    elif x == '3':
        print(lic.get_bcheck_dates())
    else:
        print('Oops! Invalid input')


main()