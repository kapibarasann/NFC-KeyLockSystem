import csv

with open('data.csv', 'r') as f:
	reader = csv.reader(f)
	card = ''.join(next(reader))
f.close()

print card
