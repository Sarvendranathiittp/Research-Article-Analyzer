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
        
        #the words we are looking for.
        word_1="\subsection" 
        word_2="\subsubsection"

        lines=self.latex_code.splitlines() #splitting the code into lines.
        indices=[]
        #finding the index of each line containing either word_1 or word_2
        #output.append(lines)
        output.append(lines[1769])
        for index in range(0,len(lines)): 
            if word_1 in lines[index] or word_2 in lines[index]:
                indices.append(index) #storing the indices of word_1 and word_2 in the list.
        for index in indices:
            line1 = lines[index]
            #   output.append(str(index)+" "+line1)
            a=12
            # if word_1 in line1:
            #     a=12
            if word_2 in line1:
                a=15
            char1='}'
            char2='~'
            b = 0
            for c in range(a,len(line1)):
                if line1[c] == char1 or line1[c] == char2:
                    b = c
                    break
            line=line1[a:b]
            #output.append(line)
           # output.append(line+'\n')
            tokens= word_tokenize(line) #tokenising parts of speech.
            postag = pos_tag(tokens) #tagging parts of speech.
            #output.append(postag)
            #Conditions on list of Nouns, pronouns, adjectives ,verbs and adverbs
            pos_list1={'NN', 'NNS', 'NNP', 'PRP', 'PRP$', 'IN', 'RBR', 'RBS', 'JJ', 'JJR', 'JJS', 'VB', 'RB'}
            #Articles and Co-ordinating conjuctions
            pos_list2={'CC','DT'}
            #Prepositions of more than three words
            list3={'before','from','through','with','versus','among','under','between','without'}
            index+=1
            for word, pos in postag:
                if pos in pos_list1 and word[0].islower():
                    output.append(('ERROR in line:'+str(index)+" "+word+' '+pos))
            # for word,pos in postag:
                elif pos in pos_list2 :
                    if word[0].islower() and word!=tokens[0] and word!=tokens[-1]:
                        pass
                    else:
                        output.append(('ERROR in line:'+str(index)+" "+word+' '+pos))
            # for word in tokens:
                elif word in list3:
                    output.append(('ERROR in line:'+str(index)+" "+word+' '+pos))
        return output


    # def lineNumber(self,target_index):
    #     line_count=1
    #     current_index=0
    #     while current_index<=target_index:
    #         if self.latex_code[current_index]=='\n':
    #             line_count+=1
    #         current_index+=1
    #     return line_count
             

