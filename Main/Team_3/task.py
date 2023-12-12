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
        self.scientistName(text,output)
        output.append(str+'\n\t\t\t\t\t\tIndex Related Comments\n'+str)
        
        
        
        return output
    
    def scientistName(self,text,output):
        scientist_names_used=set()
        scientist_names={'Isaac Newton','Newton','Albert Einstein','Einstein','Galileo Galilei','Niels Bohr','Bohr','Marie Curie',
                         'Max Planck','Planck','James Clerk Maxwell','Maxwell','Werner Heisenberg','Heisenberg','Richard Feynman',
                         'Feynman','Erwin Schrödinger','Schrödinger','Enrico Fermi','Stephen Hawking','Hawking','Michael Faraday',
                         'Faraday','Dmitri Mendeleev','Carl Sagan','Andrei Sakharov','Lise Meitner',
                         'Edwin Hubble','Jocelyn Bell Burnell','Chandrasekhar Subrahmanyan',
                         'Gaussian','Doppler'}
        for word in text.split(' '):
            if word in scientist_names:
                scientist_names_used.add(word)
        str1=''
        for word in scientist_names_used:
            if str1=='':
                str1=word
            else:
                str1=str1+', '+word
        output.append('Scientist Names Used = '+str1+'\n')
            

        # return output # all output ahould be written in this var
    """
    Make seperate functions for whatever you do and call it in run
    """

    def indexParse(self):
        text = self.latex_code
        start_index = text.find(r"\begin{IEEEkeywords}")
        start_index = text.find(r"\begin{IEEEkeywords}")
