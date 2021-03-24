import csv


# this class initiates a import CSV object (which is basically a blank array) which can then have the getcvs method applied to it where the
# argument is the name of the csv file to be put into an array.
# the getcvs method reads the csv line by line adds each line as an element in the array, and removes the empty lines that are
# apparently unavoidable when writing a csv with python. Some more methods could be added later if needed

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


