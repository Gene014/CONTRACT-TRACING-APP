import csv

class DataStorage:
    def save_data(filename, questions, data):
        with open (filename, 'a', newline='') as file:
            writer = csv.writer(file)

            #Checking file if empty
            if file.tell() == 0:
                writer.writerow(questions)

    def load_data(filename):
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            data = list(reader)

        return data