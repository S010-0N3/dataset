#import module csv
import csv

f = open("nfl_data.csv")
nfl = csv.reader(f)

sf_wins = 0
for row in nfl:
  if row[2] == "San Francisco 49ers":
    sf_wins += 1

print(sf_wins)


#creer une fonction qui prendra en entre le nom d'une equipe et retournera ces victoires.sf_wins
f = open("nfl_data.csv")
nfl = csv.reader(f)

def nfl_wins(team):
  count = 0
  for row in nfl:
    if row[2] == team:
      count += 1
  return(count)


victoire = nfl_wins(input())
print(victoire,"victoire")