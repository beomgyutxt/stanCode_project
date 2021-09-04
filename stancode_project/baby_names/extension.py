"""
File: extension.py
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    """
    The program crawls the baby names websites which record top200 male and female baby names of three decades
    and prints the total number of these babies.
    """
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        ##################
        #                #
        #      TODO:     #
        #                #
        ##################
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)
        items = soup.find_all('table', {'class': 't-stripe'})
        total_male = 0                                      # top200 total male
        total_female = 0                                    # top200 total female
        for item in items:
            data = item.tbody.text
            data = data.split()
            for i in range((len(data)-20)//5):
                # info = [rank, male, male number, female, female number]
                info = data[5*i:5*i+5]
                male_n = string_to_int(info[2])             # get male number
                female_n = string_to_int(info[4])           # get female number
                total_male += male_n
                total_female += female_n
        print(f'Male number: {total_male}')
        print(f'Female number: {total_female}')


def string_to_int(string):
    """
    The function converts data types (string --> int) of data from websites.
    e.g. '182,993' --> 182993
    """
    number = ''
    for ch in string:
        if ch.isdigit():
            number += ch
    return int(number)


if __name__ == '__main__':
    main()
