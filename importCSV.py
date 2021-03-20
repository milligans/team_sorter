import csv


class importCSV():
    with open ('results.csv') as csvfile:
        answers_dict={}
        reader=csv.DictReader(csvfile)
        for row in reader:
            answers_dict.update(row)
            print(answers_dict)


