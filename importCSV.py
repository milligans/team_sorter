import csv

class importCSV():

    def __init__(self, file):
        self.file='results.csv'
        self.answers_dict={}
        self.result_array=[]


    def getcsvs(self, file):
        with open (file) as csvfile:
          result_array=list(csv.reader(csvfile))
        for result in result_array:
            if not result:
                result_array.remove(result)

        return result_array