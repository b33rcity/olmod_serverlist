#!/usr/bin/env python3

import sys
import urllib.request
from collections import namedtuple
from bs4 import BeautifulSoup

list_page = urllib.request.urlopen('https://olproxy.otl.gg/').read().decode('utf-8')

soup = BeautifulSoup(list_page, features='html.parser')

browser = soup.body.find(id='browser')
headers = browser.find_all(attrs={'class': 'header'})
col_width = len(headers)

tup_headers = [x.string.replace(' ', '_') for x in headers]
Listing = namedtuple('Listing', tup_headers)

records = [x for x in browser.find_all(attrs={'class': 'old'})]

r = 0
listings = []
while not r + col_width > len(records):
    fields = []
    for x in records[r:r+col_width]:
        if len(x.contents) > 1:
            if x.a:
                fields.append(f"{x.a.string}({x.a.attrs['href']})")
            elif x.time:
                fields.append(x.time.string)
        else:
            fields.append(x.string)
    listings.append(Listing._make(fields))
    r += col_width

for listing in listings:
    print(f"{listing.Name}")
    print(f"\tIP: {listing.IP_Address}")
    print(f"\tPlayers: {listing.Players}")
    print(f"\tMap: {listing.Map}, Mode: {listing.Mode}")
    print(f"\tLast Update: {listing.Last_Updated}")
    print(f"\tLast Game Started: "
          f"{listing.Last_Game_Started}")
    print("")
    print(f"Notes: {listing.Notes}")
    print("\n************\n")
