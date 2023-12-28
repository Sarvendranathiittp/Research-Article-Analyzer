# Team 1 #
"""
To run this file 
        First we need to install the nltk module using the command "pip install nltk"
        Then import it ...because we can easily detect the parts of speech of each word easily.
"""

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
        self.author_analysis(text,output)
        output.append('='*50+"\n")
        return output
        
    #function to analyse title text. 
    def title_analysis(self,latex_content,output):
        
        output.append('='*50+"\n\t\t Title Related Comments \n"+'='*50+'\n')
        
         # Define a regular expression to match LaTeX Title
        title_pattern = re.compile(r'\\title{([^}]+)}')
        
         # Finding title pattern in latex content
        title_match = re.search(title_pattern, latex_content)
        
        if title_match:
            # Extract and return the title text
             title_text = title_match.group(1).strip()
             
             # Tokenize the title_text into words
             words = word_tokenize(title_text)
             
             # Use part-of-speech tagging to get the POS (part-of-speech) for each word
             pos_tags = pos_tag(words)
             
             # Filter words that are tagged (NN, NNS, etc.)
             for word,pos in pos_tags:
                 output.append(word +" \n")
                 if word == words[0] or word ==words[-1]:   # intial & final word shld be capital ina title
                     if not word.istitle() and not word.isupper():
                         output.append(" Word '"+word +"' need to be capitalized since it is at starting/ending of title\n")
                 
                 #Finding Nouns, Adjectives, Verbs, Adverbs & Prnouns and checking the condition
                 elif pos.startswith('N') or pos.startswith('J') or pos.startswith('V') or pos.startswith('R') or pos.startswith('P') :
                    if  not word.istitle() and not word.isupper():
                        output.append(" Word '"+word+"' need to be Capitalized since it is a '"+ pos_tag_fullforms(pos)  + "'\n")
                 
                 #Finding Coordinate Conjuctions , Articles, pripostions         
                 elif pos=='CC'or pos=='DT' or (pos=='IN' and len(word)<4):
                        if not word.islower():
                            output.append(" Word '"+word+"' need to be in lower case since it is a '"+ pos_tag_fullforms(pos) +"'\n")
                 
                 #finding prepostions of length greater than 3
                 elif pos=='IN' and len(word)>3 :
                        if not word.istitle():
                            output.append(" Word '"+word+"'need to be capitalised since it is a '"+ pos_tag_fullforms(pos)+"'\n")
                 else:
                     if not word.isupper():
                        output.append("Warning : This word '"+word+"' is not recognised !!!!\n")
             #Checking Whether extra spaces are added in title text.
             spaces_count(title_text,output)    
            
        else:
            output.append("Error : No Title Found in the Latex Code\n")
         
            
    # Function to analyse author text       
    def author_analysis(self,latex_content,output):
        
        output.append('='*50+"\n\t\t Author Related Comments \n"+'='*50+'\n')
        
        # Define a regular expression to match latex author 
        author_pattern = r"\\author\{(.*)\}"
        
        # finding author pattern in latex content
        matches = re.findall(author_pattern, latex_content)
        
        #extracted author text in latext content
        author_text=matches[0]
        author_text=author_text+"}"
        print(author_text)
        # making author text into token of words 
        words = word_tokenize(author_text)
        
        # variable to count the no of names or authors 
        name_count=0
        
        author_indices=[]
        author_indices.append(0)
        
        author_flag=0
        #Verifying the author text with IEEE rules 
        for i in range(len(words)):
           
            if re.match(r'^[a-zA-Z]+$', words[i]) and not words[i]=='and':
                name_count=name_count+1
                
                #verifying all authors, other names is capitalized or not 
                if not words[i].istitle()and not words[i].isupper():
                    output.append("word '"+words[i]+"' need to be capitalized\n")
                
                #verifying a comma is missing or not
                if name_count>3:
                    output.append("Warning : Comma is not present in first three words of the author list. Check for any missing comma\n")
                    name_count=0
                    
            if words[i]=='{':
                author_flag =1
                if not words[i-1]==',':
                    output.append("Comma is missing after the Author Name '"+words[i-2]+"' and Before Author Affiliation\n")
                    name_count=0
                    
                #making sure that author affiliation is writen in italic style.
                if not words[i+1]=='\\it':
                    output.append("Warning : it's better to use Italyic Style in writing Author Affiliation \n")
            
            if words[i]==',':
                name_count=0   
                if not words[i+1]=='{' and author_flag==0:
                    author_indices.append(i+1)
            
            #verifiying whether comma is missing after the author affiliation and before author name
            if words[i]=='}'and not i==len(words)-1 and not words[i+1]=='}':
                author_flag=0
                if not words[i+1]==',' and not words[i+1]=='and' :
                       output.append("Comma is missing before author '"+words[i+1]+"'.\n")
                       author_indices.append(i+1)   
            if words[i]=='and' and not words[i-1]==',':
                author_indices.append(i)    
                name_count=0
                       
        checking_and_word(words,author_indices,output)    
        
        # Finding whether unncessary spaces are assigned in author content    
        spaces_count(author_text,output)
        
# Function to verify whether unnecessary spaces are given or not    
def spaces_count(text,output):
        spaces_count=0
        for i in range(len(text)):
            if(text[i]==" "):
                spaces_count=spaces_count+1
            else:   
                spaces_count=0
            
            #if there are more than 2 spaces we will through a warning
            if(spaces_count>2):
                output.append("Warning : Found Unnecessary Spaces, Try to remove them\n")
                break
                    
def checking_and_word(words,author_indices,output):
    
    if len(author_indices)==2: 
        if not words[author_indices[1]]=='and':
            output.append("If only two authors are present then the format should be \\author{author1 and author2}\n"+"\t\tHere Remove comma between authors & add 'and'\n")
        elif words[author_indices[1]-1]==',':
            output.append("If only two authors are present then the format should be \\author{author1 and author2}\n"+"\t\tHere comma should be removed\n")
    else:
        for i in author_indices:
            if words[i]=='and' and not i==author_indices[-1]:
                output.append("if number of authors are more than 2 then format is : \n \t\t\\author{author1, author2, and author3} \n\t\tso remove 'and' between  all authors except last author\n")
                break
            
        if not words[author_indices[-1]]=='and' or not words[author_indices[-1]-1]==',':
                output.append("if number of authors are more than 2 then format is : \n \t\t\\author{author1, author2, and author3} \n\t\tso make sure there is ', and' before last author \n") 
           
                
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
            
                
