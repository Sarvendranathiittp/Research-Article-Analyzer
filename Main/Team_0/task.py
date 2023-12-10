# To check for incorrect annotations
# Code abridged from IIT G Summer Internship Project of Simanta Sarkar

class team_0:

    def __init__(self, latex_code):
        self.latex_code = latex_code

    def run(self):  # The function which is going to be invoked in the wrapper class should contain no arguments

        acronyms = 0  # number of acronyms
        acronym_word = []  # creating a list to store acronyms found in the file

        output = [] # The output list with the errors to be returned

        text = self.latex_code
        for word in text.split(' '):  # for every word in line
            if word.isupper() and word.isalpha():  # if word is all uppercase letters
                acronyms += 1
                if len(word) == 1:  # ignoring the word found in the file of single character as they are not acronyms
                    pass
                else:
                    index = len(acronym_word)
                    acronym_word.insert(index, word)  # storing all the acronyms founded in the file to a list

        uniqWords = sorted(set(acronym_word))  # remove duplicate words and sort the list of acronyms
        
        full_acronym = []
        for word in uniqWords:
            words = str(
                "(" + word + ")")  # adding brackets to each acronym since full form is present at only condition of giving the acronym at the end of full form within a bracket
            index = len(full_acronym)
            full_acronym.insert(index, words)  # inserting the acronyms with bracket to full_acronym list

        # searching the words for which full form is not in the document
        for word in full_acronym:
                if word in text:
                    pass
                else:
                    output.append("The first occurrence of acronym " + word[1:-1] + " is not found on the document.\n")

        return output