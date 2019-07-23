#Import csv module for reader and writer functions
import csv

with open ('Data/data2.csv', 'r') as csvinput:
    with open('Data/output.csv', 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)
    
        all = []
        headers = next(reader)
        all.append(headers)

        for row in reader:
            row[1] = float(row[1])
            row[2] = float(row[2])
            if row[2] == 0.00:
                row[3] = 0.00
            else:
                row[3] = row[2]/row[1]
            all.append(row)

        writer.writerows(all)
