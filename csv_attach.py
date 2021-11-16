
from value_extract import *
import csv
from datetime import date
import pandas as pd

today = date.today()

# dd/mm/YY
date = today.strftime("%d/%m/%Y")
print(date, value)

file = open('oljepriser.csv')


csvreader = csv.reader(file)

c = pd.read_csv('oljepriser.csv')
#print(c)

# Dra sista id:t från csv-filen
# Gör en lista med id+=1, datum och value
#id = #sista id:t
#new_id = id += 1

row_count = sum(1 for row in c)
print ("row count:", row_count)
new_id = (row_count + 1)
print ("new id:", new_id)


#append_list = [new_id, date, value]
#file = open('oljepriser.csv', 'w+', newline='')
#with file:
#    write = csv.writer(file)
#    write.writerows(append_list)



# Value = 705.94 15/11
