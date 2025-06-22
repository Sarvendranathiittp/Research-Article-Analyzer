# Team 1 #
"""
To run this file 
        First we need to install the nltk module using the command "pip install nltk"
        Then import it ...because we can easily detect the parts of speech of each word easily.
"""

import nltk     #importing module nltk containing parts of speech
from nltk import pos_tag, word_tokenize


import re;      #importing module regular expression
try:
    nltk.data.find('taggers/averaged_perceptron_tagger_eng/averaged_perceptron_tagger_eng.pickle')
except LookupError:
    nltk.download('averaged_perceptron_tagger_eng')

INs={ 'for', 'in', 'on', 'at', 'to', 'by', 'with', 'about', 'between','into',
'through', 'during', 'before', 'after', 'from', 'of'} #prepositions
PRPs={'I', 'you', 'he', 'she', 'it', 'we', 'they' "me", "him", "her", "us", "them","mine", "yours", "his", "hers", "ours","myself", "yourself", "himself", "herself", "itself","who", "whom", "which", "someone", "everyone"} # Pronouns
DTs= {"the", "a", "an", "this", "that","each", "every", "some", "any", "no","many", "few", "several", "more", "most", "all","both", "either", "neither","much", "less", "least","such", "what", "which", "whose","my", "your", "his", "her", "its", "our", "their",  "one", "another", "the other", "some other", "any other"} 
CCs={"and", "or", "but", "nor", "for", "yet", "so", "after", "although", "as", "because", "before", "even if","even though", "if", "once", "since", "so that", "than","that", "though", "unless", "until", "when", "whenever","where", "whereas", "wherever", "whether", "while"} # Conjunctions


class team_1:
    def __init__(self, latex_code, text_begin):
        self.latex_code = latex_code    # The entire LaTex code is in the form of string in the latex_code string
        self.text_begin = text_begin    # location of \begin
        
    def run(self):      # will be invoked by wrapper, shouldn't take arguments
        output = []     # The output list with the errors to be returned
        text=self.latex_code
        self.author_analysis(text,output)
        #self.title_analysis(text,output)
        return output
    
    #function to analyse title text. 
    def title_analysis(self,latex_content,output):
        
        output.append('='*50+"\n\t\t Title Related Comments \n"+'='*50+'\n')
        
         # Define a regular expression to match LaTeX Title
        title_pattern = re.compile(r'\\title{([^}]+)}')
        
         # Finding title pattern in latex content
        title_match = re.search(title_pattern, latex_content)

        title_index = latex_content.find(r'\title')

        self.line_number=0

        
        self.line_number = self.latex_code.count('\n', 0, title_index) + 1
        print(self.line_number)
        
        if title_match:
             
              # Extract and return the title text
            title_text = title_match.group(1).strip()

             # Tokenize the title_text into words
            wordss = word_tokenize(title_text)
            # spliting hyphenated words
            words=[]
            hyphenated_words_map=[]
            for word in wordss:
                if '-' in word:
                    splits=word.split('-')
                    words.extend(splits)
                    hyphenated_words_map.append((True,list(splits)))
                else:
                    words.append(word)
                    hyphenated_words_map.append((False,[word]))

             
             # Use part-of-speech tagging to get the POS (part-of-speech) for each word
            
            # For POS tagging, lowercase 'A' if not at start/end
            tag_words = []
            for i, w in enumerate(words):
                if w == 'A' and i != 0 and i != len(words)-1:
                    tag_words.append('a')
                else:
                    tag_words.append(w)
            pos_tags = pos_tag(tag_words)

            corrected_pos_tags=[]
            for word,pos in pos_tags:
                if word.lower() in INs:
                    corrected_pos_tags.append((word, 'IN'))
                elif word.lower() in PRPs:
                    corrected_pos_tags.append((word, 'P'))
                elif word.lower() in DTs:
                    corrected_pos_tags.append((word, 'DT'))
                elif word.lower() in CCs:
                    corrected_pos_tags.append((word, 'CC'))
                else:
                    corrected_pos_tags.append((word, pos))
                
            pos_tags=corrected_pos_tags

            count=0
            error=''
            error_triggered=False
             
             # Filter words that are tagged (NN, NNS, etc.)
            
            corrected_words = []

            pos_i = 0
            for is_hyphenated, subwords in hyphenated_words_map:
                corrected_subwords = []
                for i, subword in enumerate(subwords):
                    word, pos = pos_tags[pos_i]
                    # Initial and final word: capitalize
                    if pos_i == 0 or pos_i == len(words) - 1:
                        corrected_word = word.capitalize() if not word.isupper() else word
                    # Nouns, Adjectives, Verbs, Adverbs, Pronouns: capitalize
                    elif pos.startswith('N') or pos.startswith('J') or pos.startswith('V') or pos.startswith('R') or pos.startswith('P'):
                        corrected_word = word.capitalize() if not word.isupper() else word
                    # Coordinating Conjunctions, Articles, short prepositions: lowercase
                    elif pos == 'CC' or pos == 'DT' or (pos == 'IN' and len(word) < 4):
                        corrected_word = word.lower()
                    # Prepositions of length > 3: capitalize
                    elif pos == 'IN' and len(word) > 3:
                        corrected_word = word.capitalize()
                    else:
                        corrected_word = word
                    corrected_subwords.append(corrected_word)
                    pos_i += 1
                if is_hyphenated:
                    corrected_words.append('-'.join(corrected_subwords))
                else:
                    corrected_words.append(corrected_subwords[0])

            corrected_title = ' '.join(corrected_words)


            for i, (word, pos) in enumerate(pos_tags):
                error_triggered=False
                if word == words[0] or word == words[-1]:   # initial & final word should be capital in a title
                    if not word.istitle() and (not word.isupper() and not word.istitle()):
                        error += f" Line {self.line_number}: In Word {word} first letter need to be capitalized.\n"
                        error_triggered = True
                        # checking if it's a plural acronym
                        if (word[:len(word)-1].isupper() and not word[len(word)-1].islower()) or (not word[:len(word)-1].isupper() and not word[len(word)-1].islower()):
                            error += f" Line {self.line_number}: In Word {word} last letter should be in lowercase if it's an acro.\n"
                # Finding Nouns, Adjectives, Verbs, Adverbs & Pronouns and checking the condition
                elif pos.startswith('N') or pos.startswith('J') or pos.startswith('V') or pos.startswith('R') or pos.startswith('P'):
                    if not word[0].isupper():
                        error += f" Line {self.line_number}: In Word {word} first letter need to be capitalized.\n"
                        error_triggered = True
                # Finding Coordinate Conjunctions, Articles, prepositions         
                elif pos == 'CC' or pos == 'DT' or (pos == 'IN' and len(word) < 4):
                    if not word.islower() and not (i > 0 and words[i-1] == ':'):
                        error += f" Line {self.line_number}: Word {word} need to be in lower case.\n"
                        error_triggered = True
                # finding prepositions of length greater than 3
                elif pos == 'IN' and len(word) > 3:
                    if not word[0].isupper():
                        error += f" Line {self.line_number}: In Word {word} first letter need to be capitalized.\n"
                        error_triggered = True
                count = 0
                for i in range(1, len(word)):
                    if 65 <= ord(word[i]) <= 90:
                        count += 1
                if count>0 and not word.isupper():
                    count_word=num_to_words(count)
                    plural="letter is" if count==1 else "letters are"
                    if error_triggered:
                        error+=f"In the word {word}, {count_word} {plural} unnecessarily capitalized.\n"
                    else:
                        error+=f" Line {self.line_number}: In the word {word}, {count_word} {plural} unnecessarily capitalized.\n"

             #Checking Whether extra spaces are added in title text.
            self.spaces_count(title_text,output) 
 
        else:
            error+="Error : No Title Found in the Latex Code\n"
        output.append(error)
        output.append("\nCorrected Title:\n" + corrected_title + "\n")

           
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
        
        # making author text into token of words 
        words = word_tokenize(author_text)
        
        # variable to count the no of names or authors 
        name_count=0
        
        #using a list to save the author indices in given text
        author_indices=[]
        author_indices.append(0)
        author_flag=0   #it is used to check whether we are inside author affiliation or outside it
        

        author_index = latex_content.find(r'\author')
        
        if author_index != -1:
            self.line_number =latex_content.count('\n', 0, author_index) + 1
        else:
            self.line_number = -1

        #Verifying the author text with IEEE rules 
        for i in range(len(words)):
            #Extracting the full name of author
            j=i-1
            name_parts=[]
            while j>=0 and words[j].lower() not in [',','and','}','{']:
                name_parts.insert(0,words[j])
                j-=1
            full_name=' '.join(name_parts)

            if re.match(r'^[a-zA-Z]+$', words[i]) and not words[i]=='and':
                #verifying all authors, other names is capitalized or not 
                if not words[i][0].isupper():
                    output.append(f" Line {self.line_number}: In Word '"+words[i]+"' first letter need to be capitalized.\n")
                    
            #verifying a comma is between author and author affiliation
            if words[i]=='{':
                author_flag =1
                if not words[i-1]==',':
                    output.append(f" Line {self.line_number}: A comma is missing after the author name '{full_name}', and before the author affiliation.\n")
                #making sure that author affiliation is writen in italic style.
                if not words[i+1]=='\\it':
                    output.append(f" Line {self.line_number}: Warning: Use \it for italic style when writing the author affiliation.\n")
            
            if words[i]==',':
                if not words[i+1]=='{' and author_flag==0:
                    author_indices.append(i+1)  #appending the authors
            
            #verifiying whether comma is missing after the author affiliation and before author name
            if words[i]=='}'and not i==len(words)-1 and not words[i+1]=='}':
                author_flag=0
                if not words[i+1]==',' and not words[i+1]=='and' :
                       output.append(f" Line {self.line_number}: Insert a comma between author names.\n")
                       author_indices.append(i+1) #appending the authors   
                       
            if words[i]=='and' and not words[i-1]==',':
                author_indices.append(i)    #appending the authors
                
         
        # finding whether 'and' is present at correct place or not in author text              
        self.checking_and_word(words,author_indices,output)    
        
        # Finding whether unncessary spaces are assigned in author content    
        self.spaces_count(author_text,output)
 
        
# Function to verify whether unnecessary spaces are given or not    
    def spaces_count(self,text,output):
            spaces_count=0
            for i in range(len(text)):
                if(text[i]==" "):
                    spaces_count=spaces_count+1
                else:   
                    spaces_count=0
                
                #if there are more than 2 spaces we will through a warning
                if(spaces_count>2):
                    output.append(f" Line {self.line_number}: Warning: Unnecessary spaces found between words\n")
                    break
                    
# Function to verify 'and' word is at right place
    def checking_and_word(self,words,author_indices,output):
        
        #verifying conditions if only two authors are present 
        if len(author_indices)==2: 
            if not words[author_indices[1]]=='and':
                output.append(f" Line {self.line_number}: If only two authors are present, the format should be \\author(author1 and author2).\n\t\tRemove the comma between the authors and add 'and'.\n")
            
            elif words[author_indices[1]-1]==',':
                output.append(f" Line {self.line_number}: If only two authors are present then the format should be \\author(author1 and author2)\n"+"\t\tHere comma should be removed.\n")
    
    #verifying conditions if more than two authors are present 
        else:
            for i in author_indices:
                if words[i]=='and' and not i==author_indices[-1]:
                    output.append(f" Line {self.line_number}: If number of authors are more than 2 then format is : \n \t\t\\author(author1, author2, and author3) \n\t\tTry to remove 'and' between  all authors except last author.\n")
                    break
            
            #checking whether there is ", and " before last author   
            if not words[author_indices[-1]]=='and' or not words[author_indices[-1]-1]==',':
                    output.append(f" Line {self.line_number}: If number of authors are more than 2 then format is : \n \t\t\\author(author1, author2, and author3) \n\t\tso make sure there is ', and' before last author. \n") 
        
def num_to_words(n):
    num_words={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten"}
    return num_words.get(n, str(n))
    

            


                
