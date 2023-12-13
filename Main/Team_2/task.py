#sample space#2003
#example12
#python
#TO CALCULATE THE CHARACTER LENGTH
#class team_2:

   # def __init__(self, latex_code, text_begin):
    #    self.latex_code = latex_code
     #   self.text_begin = text_begin


	#def run(self):
	 #   count_words()

       


class team_2:
    def __init__(self, latex_content, begin_document_index):
        self.latex_content = latex_content
        self.begin_document_index = begin_document_index

    def extract_abstract(self):
        # Find the index of \begin{abstract} using the given begin_document_index
        begin_abstract_index = self.latex_content.find(r'\begin{abstract}', self.begin_document_index)

        # Find the index of \end{abstract}
        end_abstract_index = self.latex_content.find(r'\end{abstract}', begin_abstract_index)

        # Extract the abstract content without \begin{abstract} and \end{abstract}
        if begin_abstract_index != -1 and end_abstract_index != -1:
            abstract_content = self.latex_content[begin_abstract_index + len(r'\begin{abstract}'):end_abstract_index].strip()
            return abstract_content
        else:
            return None
   
    def count_words(self, text):
        # Split the text into words and return the count
        words = text.split()
        return len(words)
    
    def run(self):
        abstract = self.extract_abstract()
        output = [] # The output would be updated with the extracted title and abstract along with the word counts respectively.

        if abstract:

            output.append(f"Abstract: \n{abstract}")
        
            # Call the count_words method using the obj_team_2 instance
            word_count = self.count_words(abstract)
            print(f"Abstract is found,data is updated in LOGII file")

            output.append(f"\n Number of words in the abstract: {word_count}")
       
        else:
            output.append("No abstract found.")

            print("No abstract found.")
        return output