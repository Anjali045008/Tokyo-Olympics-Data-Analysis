# -*- coding: utf-8 -*-
"""Tokyo Olympics_Scraper.ipynb


"""

from sqlalchemy.sql.expression import false
from requests.api import request
import requests
from bs4 import BeautifulSoup
import pandas as pd


# Define the URL of the website to scrape
url = "https://www.bbc.com/sport/olympics/57836709"

r= requests.get(url)
print(r)

soup= BeautifulSoup(r.text,"lxml")
table = soup.find("table",class_="gs-o-table story-body__table")
#print(table)
title = table.find_all("th")
#print(headers)
header=[]
for i in title:
  name=i.text
  header.append(name)
print(header)

df = pd.DataFrame(columns=header)
#df

rows = table.find_all("tr")
#print(rows)

for i in rows[1:]:
  data=i.find_all("td")
  row=[tr.text for tr in data]
  l=len(df)
  df.loc[l]=row
print(df)
