#team 1#
import nltk
from nltk import pos_tag, word_tokenize

import re;

class team_1:
    
    def __init__(self, latex_code, text_begin):
        self.latex_code = latex_code
        self.text_begin = text_begin
        
    def run(self):
        
        output = []
        text=self.latex_code
        self.title_analysis(text,output)
        return output
        
    def title_analysis(self,latex_content,output):
        
        output.append('='*50+"\n\t\t Title Related Comments \n"+'='*50+'\n')
        title_pattern = re.compile(r'\\title{([^}]+)}')
        
        title_match = re.search(title_pattern, latex_content)
        
        if title_match:
        # Extract and return the title text
             title_text = title_match.group(1).strip()
             # Tokenize the text into words
             words = word_tokenize(title_text)
             
             pos_tags = pos_tag(words)
             
             
             for word,pos in pos_tags:
                 output.append(word +"\n")
                 if word == words[0] or word ==words[-1]:
                     if not word.istitle():
                         output.append("Word '"+word +"' need to be capitalized since it is at starting/ending of title\n")
                 
                 elif pos.startswith('N') or pos.startswith('J') or pos.startswith('V') or pos.startswith('R') or pos.startswith('P') :
                    if  not word.istitle() and not word.isupper():
                        output.append(" word'"+word+"' need to be Capitalized since it is a '"+ pos_tag_fullforms(pos)  + "'\n")
                         
                 elif pos=='CC'or pos=='DT' or (pos=='IN' and len(word)<4):
                        if not word.islower():
                            output.append(" word '"+word+"' need to be in lower case since it is a '"+ pos_tag_fullforms(pos) +"'\n")
                 
                 elif pos=='IN' and len(word)>3 :
                        if not word.istitle():
                            output.append(" Word '"+word+"'need to be capitalised since it is a '"+ pos_tag_fullforms(pos)+"'\n")
            
        else:
            output.append("No Title Found in the Latex Code\n")
            
            
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
            
                
        
        
        
        
        
        
    
        
        
        