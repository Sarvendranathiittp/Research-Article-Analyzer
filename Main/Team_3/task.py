#To Check if Index Terms are written in a senctence and follow the following rules :
#   1.All articles must contain Index Terms
#   2.Index Terms should appear in Alphabetical order
#   3.The first term of the Index Terms list must be capitalized and the list should end with full stop.
#   4.Acronyms must be capitalized
#To list the names of all Scientists used in the research paper 
#and to check if they are started with a capital letter since they are proper names

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
        output.append(str+'\n\tIndex Related Comments\n'+str+'\n')
        output.extend(self.indexCheck())
        #output.append('\n'+str+'\n\tAcronym Related Comments\n'+str)
        self.acron(text,output)
        
        return output
    
    def scientistName(self,text,output):
        location=dict()
        # "set" to avoid repeatition
        scientist_names_used=set()
        scientist_names_used1=set()
        scientist_names_used2=set()
        scientist_names2=[]
        #List is used for ordering       
        scientist_names=[['Isaac Newton','Newton'],['Albert Einstein','Einstein'],'Galileo Galilei',['Niels Bohr','Bohr'],'Marie Curie',
                          ['Max Planck','Planck'],['James Clerk Maxwell','Maxwell'],['Werner Heisenberg','Heisenberg'],['Richard Feynman','Feynman'],
                          ['Erwin Schrödinger','Schrödinger'],'Enrico Fermi','Stephen Hawking','Hawking',['Michael Faraday',
                         'Faraday'],'Dmitri Mendeleev','Carl Sagan','Andrei Sakharov','Lise Meitner',
                         'Edwin Hubble','Jocelyn Bell Burnell','Chandrasekhar Subrahmanyan',
                         'Gaussian','Doppler']
        
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
            if text1.find(word)!=-1:
                location[text1.find(word)]=realword
                #output.append(str(text1.find(word))+" "+realword)
                scientist_names_used.add(text[text1.find(word):text1.find(word)+len(word)])
                scientist_names_used2.add(realword)
            
        #key contains the index number 'character index'
        for key,value in location.items():
            if text[key:key+len(value)]!=value:
                
                line=self.lineNumber(key)
                output.append("At Line "+str(line)+' : '+text[key:key+len(value)]+" is not in proper format ")
        #"At line "+self.line_number(text,key)+":"+
        for element in scientist_names:
                # Check if the element is a list
            if isinstance(element, list):
                # Check if any element in the sublist is present in S1
                if any(sub_element in scientist_names_used2 for sub_element in element):
                    # Add the first element of the sublist to the set
                    scientist_names_used1.add(element[0])
            else:
                # Check if the standalone element is present in S1
                if element in scientist_names_used2:
                    # Add the standalone element to the set
                    scientist_names_used1.add(element)
        str1=''
        for word in scientist_names_used1:
            if str1=='':
                str1=word
            else:
                str1=str1+', '+word
        for word in scientist_names_used:
            if word[0].islower() is True: # can directly check True/False is True not required
                output.append(word+" should start with a capital letter as it is a proper name ")
        if str1=='':
            output.append('No Scientist Names Used\n')        
        else:
            output.append('\nScientist Names Used = '+str1+'\n')        
    
    
    """
    Make seperate functions for whatever you do and call it in run
    """
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
        """
        for word in acronym_word:
            if word not in unique_words:
                output.append("\n"+word)
        """

    def indexCheck(self):
        text = self.latex_code
        output = []
        
        start_index = text.find(r"\begin{IEEEkeywords}")
        if start_index == -1:
            output.append("Index Terms not present in document")
            return output
        
        end_index = text.find(r"\end{IEEEkeywords}") 
        
        index_text = text[start_index+21:end_index].rstrip() # 21 is to offset \begin{IEEEkeywords}
        index_text = index_text.strip()
        
        """
        Checking alphabetical order 
        """
        
        comma_list = [i.strip()[0].lower() for i in index_text.split(",") if len(i)>=1 and i.strip()[0].isalpha()]
        if comma_list != sorted(comma_list):
            output.append("Index terms are not in alphabetical order")
        
        index_text_list = index_text.replace(","," ").split(" ")
        full_stop_check_list = [i.strip() for i in index_text_list if len(i)>=1]
        index_text_list = [i.strip(" .") for i in index_text_list if len(i)>=1]
        reference_text = index_text.capitalize()
        reference_text_list = reference_text.replace(","," ").split(" ")
        reference_text_list = [i.strip(" .") for i in reference_text_list if len(i)>=1]
        
        """
        Checking if index terms are in Sentence case
        Considering any word with >=2 upper case characters as Acronyms
        """
        for i,j in zip(index_text_list,reference_text_list):
            if not sum([1 for _ in i if _.isupper()])>=2:
                if i != j:
                    if j[0].isupper():
                        output.append("First letter of first word must be in Capital Case")
                    else:
                        output.append(f"Word {i.strip()} is in the middle of the sentence, so should be in lower case ")
        """
        Checking for full stop at the end of index terms
        """
        
        if full_stop_check_list[-1][-1] !=".":  # last character should be .
            output.append(f"Full stop not present at the end of index")
        return output if len(output)>=1 else ["No errors in Index"] 

    def lineNumber(self,target_index):
        line_count=0
        current_index=0
        while current_index<=target_index:
            if self.latex_code[current_index]=='\n':
                line_count+=1
            current_index+=1
        return line_count+1
