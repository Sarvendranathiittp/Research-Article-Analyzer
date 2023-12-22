import re    
class team_2:
    def __init__(self, latex_content, begin_document_index):
        self.latex_content = latex_content
        
        title_index = latex_content.find(r'\title{')
        begin_document_index = latex_content.find(r'\begin{document}')

        # Check if both indices were found
        if title_index != -1 and begin_document_index != -1:
            # Choose the minimum index (earlier occurrence)
            begin_index = min(title_index, begin_document_index)
        else:
            # If one index is -1, choose the other (whichever is not -1)
            begin_index = max(title_index, begin_document_index)

        self.begin_document_index = begin_index
    
    def extract_abstract(self):
        # Find the index of \begin{abstract} using the given begin_document_index
        begin_abstract_index = self.latex_content.find(r'\begin{abstract}', self.begin_document_index)

        # Find the index of \end{abstract}
        end_abstract_index = self.latex_content.find(r'\end{abstract}', begin_abstract_index)

        # Extract the abstract content without \begin{abstract} and \end{abstract}
        if begin_abstract_index != -1 and end_abstract_index != -1:
            abstract_content = self.latex_content[begin_abstract_index + len(r'\\begin{abstract}'):end_abstract_index].strip()
            return abstract_content
        else:
            return None
        
    def remove_latex_commands(self,text):

        # Function to remove LaTeX commands
        text_withoutcommands = re.sub(r'\\[a-zA-Z]+', '', text)
        # Define a regular expression pattern to match the unwanted patterns
        pattern = r'\{[\d.]+(cm|mm)?\}'

        # Use re.sub to replace the matched patterns with an empty string
        cleaned_text = re.sub(pattern, '', text_withoutcommands)
    
        return cleaned_text

    def run(self):
        
        abstract = self.remove_latex_commands(self.extract_abstract()) 
        output = [] # The output would be updated with the extracted title and abstract along with the word counts respectively.
        
        output.append('\n'+'='*50+"\n\t\t Abstract Related Comments \n"+'='*50)
    
   
        
        return output
   
