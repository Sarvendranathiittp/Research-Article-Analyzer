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

        # Extract the abstract content
        if begin_abstract_index != -1 and end_abstract_index != -1:
            abstract_content = self.latex_content[begin_abstract_index:end_abstract_index + len(r'\end{abstract}')].strip()
            return abstract_content
        else:
            return None

# Example usage:
latex_file_path = r"C:\Users\Piyush\Github_repo\Research-Article-Analyzer\Resources\Latex_example\AS_in_CR_OC_SPU_cam_ready_v5.tex"
begin_document_index =18804 # Replace with the actual index of \begin{document}

with open(latex_file_path, 'r', encoding='utf-8') as latex_file:
    latex_content = latex_file.read()

# Assuming you have the begin_document_index
obj_team_2 = team_2(latex_content, begin_document_index)
abstract = obj_team_2.extract_abstract()

if abstract:
    print("Abstract:")
    print(abstract)
else:
    print("No abstract found.")








