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
        scientist_names_used=self.scientistName(text,scientist_names_used)
        print(scientist_names_used)
        
        
        return output
    
    def scientistName(self,text,scientist_names_used):
        scientist_names_used=[]
        scientist_names={'Isaac Newton','Albert Einstein','Galileo Galilei','Niels Bohr','Marie Curie',
                         'Max Planck','James Clerk Maxwell','Werner Heisenberg','Richard Feynman',
                         'Erwin Schrödinger','Enrico Fermi','Stephen Hawking','Michael Faraday',
                         'Dmitri Mendeleev','Carl Sagan','Andrei Sakharov','Lise Meitner',
                         'Edwin Hubble','Jocelyn Bell Burnell','Chandrasekhar Subrahmanyan',
                         'Gaussian','Doppler'}
        for word in text.split(' '):
            if word in scientist_names:
                scientist_names_used.append(word)
        return scientist_names_used
            

        # return output # all output ahould be written in this var
    """
    Make seperate functions for whatever you do and call it in run
    """

    def indexParse(self):
        text = self.latex_code
        start_index = text.find(r"\begin{IEEEkeywords}")
        start_index = text.find(r"\begin{IEEEkeywords}")
