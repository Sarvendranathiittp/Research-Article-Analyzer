#team 6
import re
import nltk
from nltk.corpus import words
from nltk import word_tokenize , pos_tag
# nltk.download('words')

class team_6:

    def __init__(self, latex_code, text_begin):
        self.latex_code = latex_code 
        self.text_begin = text_begin

    def run(self):

        output=[] #creating a list to store the output errors.
        i=0

        #the words we are looking for.
        word_1="\subsection" 
        word_2="\subsubsection"

        lines=self.latex_code.split('\n') #splitting the code into lines.
        indices=[]

        #finding the index of each line containing either word_1 or word_2
        for index in range(self.text_begin,len(lines)): 
            if word_1 in lines[index] or word_2 in lines[index]:
                indices.append(index) #storing the indices of word_1 and word_2 in the list.
        for index in indices:
            line = lines[index]
            tokens= word_tokenize(line) #tokenising parts of speech.
            postag = pos_tag(tokens) #tagging parts of speech.
            pos_list1={'NN', 'NNS', 'NNP', 'PRP', 'PRP$', 'IN', 'RBR', 'RBS', 'JJ', 'JJR', 'JJS', 'VB', 'RB'}
            pos_list2={'CC','DT'}
            list3={'before','from','through','with','versus','among','under','between','without'}
            for word, pos in postag:
                if pos in pos_list1 and word[0].islower():
                    output[i]={'ERROR in line:', [index]}
                    i=i+1
            for word,pos in postag:
                if pos in pos_list2 and word[0].islower() and word!=tokens[0] and word!=tokens[-1]:
                    pass
                else:
                    output[i]={'ERROR in line:', [index]}
                    i=i+1
            for word in tokens:
                if word in list3:
                    output[i]={'ERROR in line:', [index]}
                    i=i+1

        return output



             

