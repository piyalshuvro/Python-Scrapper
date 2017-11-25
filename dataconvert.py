import pandas as pd
from bs4 import BeautifulSoup
import csv



for i, df in enumerate(pd.read_html("GpResult (12).xls")):
    df.to_csv('myfile_%s.csv' % i)









# soup = BeautifulSoup("GpResult (12).xls")
# tables = soup.findChildren('table')
# print(tables)

# my_table = tables[0]
# rows = my_table.findChildren(['th', 'tr'])
# for row in rows:
# 	cells = row.findChildren('td')
# 	for cell in cells:
# 		value = cell.string
# 		print(value)


# results = pd.read_html("GpResult (12).xls")
# with open('filename.csv', 'wb') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     wr.writerow(results)
	


