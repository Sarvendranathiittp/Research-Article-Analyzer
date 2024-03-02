#team 6
import re
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import words
from nltk import word_tokenize , pos_tag



class team_6:

    def __init__(self, latex_code, text_begin):
        self.latex_code = latex_code 
        self.text_begin = text_begin
    

    def run(self):
        
        output=[] #creating a list to store the output errors.

        output.append('='*50+"\n\t Sections and Subsections related Comments \n"+'='*50+'\n')
        #the words we are looking for.
        word_1="\subsection" 
        word_2="\subsubsection"

        lines = self.latex_code.splitlines()  # splitting the code into lines.
        indices = []

        # Finding the index of each line containing either word_1 or word_2
        for index, line in enumerate(lines):
            if word_1 in line or word_2 in line:
                indices.append(index)  # storing the indices of word_1 and word_2 in the list.

        for index in indices:
            line1 = lines[index]
            
            char1 = '}'
            char2 = '~'

            # Finding the substring between '}' or '~' and the end of the line
            a = 12 if word_1 in line1 else 15 if word_2 in line1 else 0
            b = line1.find(char2, a) if char2 in line1[a:] else line1.find(char1, a)
            
            if b != -1:
                  line = line1[a:b]
            #output.append(line)
           # output.append(line+'\n')
            tokens= word_tokenize(line) #tokenising parts of speech.
            postag = pos_tag(tokens) #tagging parts of speech.
            #output.append(postag)
            #Conditions on list of Nouns, pronouns, adjectives ,verbs and adverbs
            pos_list1={'NN', 'NNS', 'NNP', 'PRP', 'PRP$', 'RBR', 'RBS', 'JJ', 'JJR', 'JJS', 'VB', 'RB'}
            #Articles and Co-ordinating conjuctions
            pos_list2={'CC','DT'}
            #Prepositions of more than three words
         #   list3={'before','from','through','with','versus','among','under','between','without'}
            index+=1
            x=0 
            for word, pos in postag:
                if pos in pos_list1 and word[0].islower():
                    output.append(('ERROR in line:'+str(index)+"   "+"Word {"+word+'}'+" need to be Capitalized since it is a "+ get_pos_full_form(pos)+"\n"))
                    x=1
            # for word,pos in postag:
                elif pos in pos_list2 :
                    if word[0].islower() and word!=tokens[0] and word!=tokens[-1]:
                        pass
                    else:
                        output.append(('ERROR in line:'+str(index)+"   "+"Word {"+word+'}'+" need to be in lower case since it is a "+ get_pos_full_form(pos)+"\n"))
                        x = 2
            # for word in tokens:
                 #finding prepostions of length greater than 3
                elif pos=='IN' and len(word)>3 :
                        if not word[0].isUpper():
                            output.append(('ERROR in line:'+str(index)+"   "+"Word {"+word+'}'+" need to be capitalised since it is a "+ get_pos_full_form(pos)+"\n"))
                            x=3
        if x == 0:
         output.append("No errors found in Subsections and Subsubsections")
                           
        output.append('='*50+"\n")
        return output


def get_pos_full_form(pos_tag):
     pos_full_forms = {
        'NN': 'Noun, Singular or Mass',
        'NNS': 'Noun, Plural',
        'NNP': 'Proper Noun, Singular',
        'PRP': 'Personal Pronoun',
        'PRP$': 'Possessive Pronoun',
        'IN': 'Preposition or Subordinating Conjunction',
        'RBR': 'Adverb, Comparative',
        'RBS': 'Adverb, Superlative',
        'JJ': 'Adjective',
        'JJR': 'Adjective, Comparative',
        'JJS': 'Adjective, Superlative',
        'VB': 'Verb, Base Form',
        'RB': 'Adverb'
        # Add more POS tags as needed
    }

     return pos_full_forms.get(pos_tag, 'Unknown POS Tag')


    # def lineNumber(self,target_index):
    #     line_count=1
    #     current_index=0
    #     while current_index<=target_index:
    #         if self.latex_code[current_index]=='\n':
    #             line_count+=1
    #         current_index+=1
    #     return line_count
             

