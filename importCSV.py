import csv


class importCSV():
    with open ('results.csv') as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            print(row)
