class team_0:
    def __init__(self, latex_code):
        self.latex_code = latex_code

    def run(self):  # The function which is going to be invoked in the wrapper class should contain no arguments

        acronyms = 0  # number of acronyms
        acronym_word = []  # creating a list to store acronyms found in the file

        output = [] # The output list with the errors to be returned

        for word in text.split(' '):  # for every word in line
            if word.isupper() and word.isalpha():  # if word is all uppercase letters
                acronyms += 1
                if len(word) == 1:  # ignoring the word found in the file of single character as they are not acronyms
                    pass
                else:
                    index = len(acronym_word)
                    acronym_word.insert(index, word)  # storing all the acronyms founded in the file to a list

        uniqWords = sorted(set(acronym_word))  # remove duplicate words and sort the list of acronyms
        '''for word in uniqWords:
            print(word, ":",acronym_word.count(word))  # printing the all the acronyms along with no of times they appear in the file
            with open('LOG.csv', 'w', newline='') as csvfile:  # creating the csv file

                fieldnames = ['Name_of_acronyms', 'Number_of_times_they_occurred']

                thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

                thewriter.writeheader()

                for word in uniqWords:
                    
                    thewriter.writerow({'Name_of_acronyms': word, 'Number_of_times_they_occurred': acronym_word.count(word)})  # Extracting the CSV file
                    full_acronym = []  # creating a list of acronym for which we will search its full form occurrence in the document'''

        for word in uniqWords:
            words = str(
                "(" + word + ")")  # adding brackets to each acronym since full form is present at only condition of giving the acronym at the end of full form within a bracket
            index = len(full_acronym)
            full_acronym.insert(index, words)  # inserting the acronyms with bracket to full_acronym list

        '''# searching the occurrence of each acronym  for the first time in the document
        for word in full_acronym:
            with open(filepath, "r") as file:
                for line_number, line in enumerate(file, start=1):
                    if word in line:
                        print(f"The First occurrence and Full form of the acronym '{word[1:-1]}' is found on line {line_number} of the document.")'''

        # searching the words for which full form is not in the document
        for word in full_acronym:
            with open(filepath) as f:

                if word in f.read():
                    pass
                else:
                    output.append("The first occurrence of acronym " + word[1:-1] + " is not found on the document.")
                    #with open ("LOGII", "a") as logw:
                    #    logw.write("The first occurrence of acronym " + word[1:-1] + " is not found on the document.\n")

        return output