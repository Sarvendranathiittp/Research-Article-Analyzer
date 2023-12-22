#team 1#
import nltk     #importing module nltk containing parts of speech
from nltk import pos_tag, word_tokenize

import re;      #importing module regular expression


class team_1:
    #constructor
    def __init__(self, latex_code, text_begin):
        self.latex_code = latex_code    # The entire LaTex code is in the form of string in the latex_code string
        self.text_begin = text_begin    # location of \begin
        
    def run(self):      # will be invoked by wrapper, shouldn't take arguments
        output = []     # The output list with the errors to be returned
        text=self.latex_code
        self.title_analysis(text,output)
        output.append('='*50+"\n")
        return output
        
    def title_analysis(self,latex_content,output):
        
        output.append('='*50+"\n\t\t Title Related Comments \n"+'='*50+'\n')
         # Define a regular expression to match LaTeX Title
        title_pattern = re.compile(r'\\title{([^}]+)}')
        
        title_match = re.search(title_pattern, latex_content)
        
        if title_match:
            # Extract and return the title text
             title_text = title_match.group(1).strip()
             
             # Tokenize the title_text into words
             words = word_tokenize(title_text)
             
             # Use part-of-speech tagging to get the POS (part-of-speech) for each word
             pos_tags = pos_tag(words)
             
             # Filter words that are tagged as nouns (NN, NNS, etc.)
             for word,pos in pos_tags:
                 if word == words[0] or word ==words[-1]:   # intial & final word shld be capital ina title
                     if not word.istitle() and not word.isupper():
                         output.append("Word '"+word +"' need to be capitalized since it is at starting/ending of title\n")
                 
                 #Finding Nouns, Adjectives, Verbs, Adverbs & Prnouns and checking the condition
                 elif pos.startswith('N') or pos.startswith('J') or pos.startswith('V') or pos.startswith('R') or pos.startswith('P') :
                    if  not word.istitle() and not word.isupper():
                        output.append(" word'"+word+"' need to be Capitalized since it is a '"+ pos_tag_fullforms(pos)  + "'\n")
                 
                 #Finding Coordinate Conjuctions , Articles, pripostions         
                 elif pos=='CC'or pos=='DT' or (pos=='IN' and len(word)<4):
                        if not word.islower():
                            output.append(" word '"+word+"' need to be in lower case since it is a '"+ pos_tag_fullforms(pos) +"'\n")
                 
                 #finding prepostions of length greater than 3
                 elif pos=='IN' and len(word)>3 :
                        if not word.istitle():
                            output.append(" Word '"+word+"'need to be capitalised since it is a '"+ pos_tag_fullforms(pos)+"'\n")
            
        else:
            output.append("No Title Found in the Latex Code\n")
            
    
    # full forms of each of the parts of speech tag (POS_tag)
def pos_tag_fullforms(pos):
    
    if(pos.startswith('N')):
        return "Noun" 
    elif(pos.startswith('J')):
        return "Adjective"
    elif(pos.startswith('V')):
        return "Verb"
    elif(pos.startswith('R')):
        return "AdVerb"
    elif(pos=='CC'):
        return "Coordinating Conjuction"
    elif(pos=='IN'):
        return "preposition/subordinating conjunction"
    elif(pos.startswith('P')):
        return "Pronoun"
    elif(pos.startswith('DT')):
        return "Articles"
    else:
        return "Null"
            
                
