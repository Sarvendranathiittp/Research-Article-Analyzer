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
             
             word_checking = [word for word, pos in pos_tags if pos.startswith('N') or pos.startswith('J') or pos.startswith('V') or pos.startswith('R')]
             
             for word in word_checking:
                 output.append(word+"\n")
                 if  not word.istitle():
                     output.append(" This word'"+word+"' need to be Capital since it is a"  +"\n")
             
        else:
            output.append("No Title Found in the Latex Code\n")
        
        
        
        
        
        
    
        
        
        