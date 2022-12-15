
import csv


dayda = open('census_2009b.csv','r')

reader = csv.reader(dayda, delimiter='\t')

for row in reader:
    # print(row)
    if len(row) != 6:
        print(len(row))