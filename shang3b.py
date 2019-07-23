import csv

with open ('Data/data2.csv', 'r') as f:
	rows = csv.reader(f)
	headers = next(rows)
	for row in rows:
		row[1] = float(row[1])
		row[2] = float(row[2])
		if row[2] == 0.00:
			row[3] = 0.00
		else:
			row[3] = row[2]/row[1]
		print(row)
# with open('data2.csv', 'wb') as f:
#     writer = csv.writer(f)
#     writer.writerows(row)