from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

url = "https://idbop.mylicense.com/verification/SearchResults.aspx" #specify url
page = requests.get(url)
pagetext = page.text



soup = BeautifulSoup(pagetext, 'html.parser')

file = open("test.csv", 'w')

for row in soup.find_all('tr'): #html tags
    for col in row.find_all('td'):
        print(col.text)
        
  #Nested loop where I am stuck      
 import csv
from bs4 import BeautifulSoup #create csv for output

outfile = open("test.csv","w",newline='')
writer = csv.writer(outfile)

tree = BeautifulSoup(html,"lxml")
body_tag = tree.select("body")[0]
tab_data = [[item.text for item in row_data.select("tr,tbody")]
                for row_data in body_tag.select("table")]

for data in tab_data:
    writer.writerow(data)
    print(' '.join(data)) #nested join where I'm stuck
