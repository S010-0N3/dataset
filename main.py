#import module csv
import csv

f = open("nfl_data.csv")
csvreader = csv.reader(f)

nfl = list(csvreader)

print(nfl)