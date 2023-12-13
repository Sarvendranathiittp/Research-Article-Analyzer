class team2:
    def __init__(self, latex_content, begin_document_index):
        self.latex_content = latex_content
        self.begin_document_index = begin_document_index

    def extract_title(self):
        # Find the index of \title using the given begin_document_index
        begin_title_index = self.latex_content.find(r'\title', self.begin_document_index)

        # Find the index of \author
        end_title_index = self.latex_content.find(r'\author', begin_title_index)

        # Extract the title content
        if begin_title_index != -1 and end_title_index != -1:
            title_content = self.latex_content[begin_title_index:end_title_index + len(r'\author')].strip()

        # Remove "\title{" and "}\author"
            title_content = title_content.replace(r'\title{', '').replace('}\author', '').strip()
            return title_content
        else:
            return None
    def extract_title(self):
        # Find the index of \title using the given begin_document_index
        begin_title_index = self.latex_content.find(r'\title', self.begin_document_index)

        # Find the index of \author 
        end_title_index = self.latex_content.find(r'\author', begin_title_index)

        # Extract the title content
        if begin_title_index != -1 and end_title_index != -1:
            title_content = self.latex_content[begin_title_index+ len(r'\title'):end_title_index].strip()
            # Remove "\title{" and "}\author"
            title_content = title_content.replace(r'\title{', '').replace('}\author', '').strip()
            return title_content
        else:
            return None
# Example usage:
latex_file_path = r"C:\Users\Piyush\Github_repo\Research-Article-Analyzer\Resources\Latex_example\AS_in_CR_OC_SPU_cam_ready_v5.tex"
begin_document_index = 18804  # Replace with the actual index of \begin{document}

with open(latex_file_path, 'r', encoding='utf-8') as latex_file:
    latex_content = latex_file.read()

# Assuming you have the begin_document_index
obj_team2 = team2(latex_content, begin_document_index)
title = obj_team2.extract_title()

if title:
    print("Title:")
    print(title)
else:
    print("No title found.")

def get_word_list(iyn):
    return iyn.split()

word_list = get_word_list(title)

# Print the list of words
print("List of words:", word_list)

def count_words(iyn):
    words = iyn.split()
    return len(words)

word_count = count_words(title)
print(f"Number of words: {word_count}")
