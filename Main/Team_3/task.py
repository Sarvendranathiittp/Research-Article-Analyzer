"""To Check if Index Terms are written in a senctence and follow the following rules :
   1.All articles must contain Index Terms
   2.Index Terms should appear in Alphabetical order
   3.The first term of the Index Terms list must be capitalized and the list should end with full stop.
   4.Acronyms must be capitalized
To list the names of all Scientists used in the research paper 
and to check if they are started with a capital letter since they are proper names
* More Scientist names can be added to the list at line 38"""
import re
class team_3:
    #Constructor
    def __init__(self, latex_code, text_begin):
        self.latex_code = latex_code # The entire LaTex code is in the form of string in the latex_code string
        self.text_begin = text_begin # location of \begin

    def run(self): # will be invoked by wrapper, shouldn't take arguments
        output = []
        text = self.latex_code
        # use self
        str = '='*50
        output.append(str+'\n\tScientist Names Related Comments\n'+str+'\n')
        self.scientistName(text,output)
        self.acron(text,output)
        return output
    
    def scientistName(self,text,output):
        location=dict()
        location2=dict()
        # "set" to avoid repeatition
        scientist_names_used=set()
        scientist_names_used1=set()
        scientist_names_used2=set()
        scientist_names2=[]

        #List is used for ordering       
        scientist_names=[['Isaac Newton','Newton'],['Albert Einstein','Einstein'],'Galileo Galilei',['Niels Bohr','Bohr'],'Marie Curie',
                          ['Max Planck','Planck'],['James Clerk Maxwell','Maxwell'],['Werner Heisenberg','Heisenberg'],['Richard Feynman','Feynman'],
                          ['Erwin Schrodinger','Schrodinger'],'Enrico Fermi','Stephen Hawking','Hawking',['Michael Faraday','Faraday'],'Dmitri Mendeleev','Carl Sagan','Andrei Sakharov','Lise Meitner',
                         'Edwin Hubble','Jocelyn Bell Burnell','Gauss','Chandrasekhar Subrahmanyan','Gaussian','Doppler', ['Leonhard Euler', 'Euler'],['Michael Atiyah', 'Atiyah'],['Ada Lovelace', 'Lovelace'],['Alan Turing', 'Turing'],['Gregor Mendel', 'Mendel'],['Nikola Tesla', 'Tesla'],
                         ['Charles Darwin', 'Darwin'],['Rosalind Franklin', 'Franklin'],['Alexander Fleming', 'Fleming'],['Barbara McClintock', 'McClintock'],['Emmy Noether', 'Noether'],['Stephen Jay Gould', 'Gould'],
                         ['Claude Shannon', 'Shannon'],['Paul Dirac', 'Dirac'],['Henrietta Leavitt', 'Leavitt'],['Jane Goodall', 'Goodall'],"Newton's Laws of Motion", "Einstein's Theory of Relativity", "Bohr Model of the Atom", 
                         "Planck's Constant", "Maxwell's Equations", "Heisenberg Uncertainty Principle", "Feynman Diagrams", "Schrödinger's Cat", "Fermi Paradox", "Hawking Radiation", "Faraday's Law of Induction", "Mendeleev's Periodic Table", 
                         "Sagan's Drake Equation Contributions", "Sakharov Conditions", "Meitner–Hahn Hypothesis", "Hubble's Law", "Bell–Burnell Pulsar Discovery", "Gaussian Distribution", "Chandrasekhar Limit", "Doppler Effect", "Euler's Formula", 
                         "Atiyah–Singer Index Theorem", "Lovelace Algorithm", "Turing Machine", "Mendelian Genetics", "Tesla Coil", "Darwin's Theory of Evolution", "Franklin's X-ray Diffraction Work", "Fleming's Penicillin Discovery", "McClintock's Transposons",
                           "Noether's Theorem", "Gould's Punctuated Equilibrium Theory", "Shannon's Information Theory", "Dirac Equation", "Leavitt's Law", "Goodall’s Chimpanzee Behavior Studies"]
        
        for element in scientist_names:
            if isinstance(element, list):
                scientist_names2.extend(element)
            else:
                scientist_names2.append(element)
        #scientist_names2 expands all the sublists and contains only strings and not sublists
        #scientist_names1 contains all the scientist names in lower case
        scientist_names1 = [string.lower() for string in scientist_names2]

        #text1 contains all the latex code in lower case
        text1 = text.lower()

        """If the scientist names are present in the text it will add 
        its location in the dictionary along with the real word"""
        for word,realword in zip(scientist_names1,scientist_names2):
            pattern = r'\b' + re.escape(word) + r'\b'
            for match in re.finditer(pattern, text1):
                start_index = match.start()
                location[start_index] = realword
                #output.append(str(start_index)+" "+realword)
                scientist_names_used.add(text[start_index:start_index+len(word)])
                scientist_names_used2.add(realword)
            
        #key contains the index number 'character index'
        for key,value in location.items():
            if text[key:key+len(value)]!=value:
                line=self.lineNumber(key)
                scientist_names_used1.add(value)
        
        str1=''
        for word in scientist_names_used2:
            if str1=='':
                str1=word
            else:
                str1=str1+', '+word

        for word in scientist_names_used:
            word_parts=word.split(' ')
            lower_case=False
            for part in word_parts:
                if part[0].islower():
                    lower_case=True
                    break
            if lower_case:
                pattern = r'\b' + re.escape(word) + r'\b'
                for match in re.finditer(pattern,text):
                    line=self.lineNumber(match.start())
                    if len(word_parts)>1:
                        output.append(" Line " + str(line) + " : [Casing] All Words in the name of scientist '" + word + "' should start with a capital letter.\n") 
                    else:
                        output.append(" Line " + str(line) + " : [Casing] Name of scientist '" + word + "' should start with a capital letter.\n") 


                    
        if str1=='':
            output.append('\n No scientist names found.\n')
        else:
            output.append('\n Scientist names : '+str1+'.\n')

            

    def is_string_in_lists(self,search_string, *lists):
        return any(search_string in my_list for my_list in lists)
   
    def acron(self,text,output):
        start_index = text.find(r"\begin{IEEEkeywords}")        
        end_index = text.find(r"\end{IEEEkeywords}") 
        index_text = text[start_index+21:end_index].rstrip() 
        index_text = index_text.strip()
        acronym_word = []
        text1=index_text.replace(","," ")
        text2=text1.replace("."," ")
        for word in text2.split(' '):
            if len(word)>1:
                x=sum(1 for c in word if c.isupper())
                if(x>=2):
                    index = len(acronym_word)
                    acronym_word.insert(index,word)
            else:
                pass
        unique_words = []


    def lineNumber(self,target_index):
        line_count=0
        current_index=0
        while current_index<=target_index:
            if self.latex_code[current_index]=='\n':
                line_count+=1
            current_index+=1
        return line_count+1
    
    # For Finding Mispelled Names
    def levenshtein_distance(self,str1, str2):
        m, n = len(str1), len(str2)
        
        # Initialize a matrix to store distances
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Initialize the first row and column
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        # Fill the matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                cost = 0 if str1[i - 1] == str2[j - 1] else 1
                dp[i][j] = min(
                    dp[i - 1][j] + 1,        # Deletion
                    dp[i][j - 1] + 1,        # Insertion
                    dp[i - 1][j - 1] + cost  # Substitution
                )

        return dp[m][n]

    def is_approximate_match(self,str1, str2, max_difference=1):

        distance = self.levenshtein_distance(str1, str2)
        if distance==0 :
            return 'equal'
        else:
            return (distance <= max_difference) 

