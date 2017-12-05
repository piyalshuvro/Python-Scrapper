import pandas as pd
from bs4 import BeautifulSoup
import csv
import html5lib

for number in range(1,208):
	for i, df in enumerate(pd.read_html("GpResult(%s).xls" % number,header = 0)):
		df.drop(df.index[0])
		df.to_csv('myfile_%s.csv' % number)



# for i, df in enumerate(pd.read_html("GpResult (12).xls",header = 0)):
# 	df.drop(df.index[0])
# 	df.to_csv('myfile_%s.csv' % 2)

for number in range(1,208):
	with open("myfile_%s.csv" %number, "rb") as fp_in, open("newfile_%s.csv" %number, "wb") as fp_out:
		reader = csv.reader(fp_in, delimiter=",")
		writer = csv.writer(fp_out, delimiter=",")
		for row in reader:
			del row[0]
			writer.writerow(row)


		# reader = csv.reader(fp_in, delimiter=",")
  #   	writer = csv.writer(fp_out, delimiter=",")
  #   	for row in reader:
  #   		del row[0]
  #   		writer.writerow(row)
    	

    	


# with open("myfile_2.csv", "rb") as fp_in, open("newfile.csv", "wb") as fp_out:
    # reader = csv.reader(fp_in, delimiter=",")
    # writer = csv.writer(fp_out, delimiter=",")
    # for row in reader:
    #     del row[0]
    #     writer.writerow(row)



