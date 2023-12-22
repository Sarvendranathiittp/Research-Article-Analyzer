class team_2:
    def team_2(self, latex_content, begin_document_index):
        self.latex_content = latex_content
        self.begin_document_index = begin_document_index

    def extract_title(self):
        # Find the index of \title using the given begin_document_index
        begin_title_index = self.latex_content.find(r'\title', self.begin_document_index)

        # Find the index of \end{abstract}
        end_title_index = self.latex_content.find(r'\author', begin_title_index)

        # Extract the abstract content
        if begin_title_index != -1 and end_title_index != -1:
            title_content = self.latex_content[begin_title_index:end_title_index + len(r'\author')].strip()
            return title_content
        else:
            return None
# Example usage:
latex_file_path = r:
begin_document_index =18804 # Replace with the actual index of \begin{document}

with open(latex_file_path, 'r', encoding='utf-8') as latex_file:
    latex_content = latex_file.read()

# Assuming you have the begin_document_index
obj_team_2 = team_2(latex_content, begin_document_index)
title = obj_team_2.extract_title()

if title:
    print("Title:")
    print(title)
else:
    print("No title found.")


def remove_braces(title):
    # Find the index of the first '{' and the last '}'
    start_index = title.find('{')
    end_index = title.rfind('}')

    # Check if both '{' and '}' are found
    if start_index != -1 and end_index != -1:
        # Extract the substring between '{' and '}'
        result = title[start_index + 1:end_index]
        return result
    else:
        # Return the original string if '{' or '}' is not found
        return title
 
newtit=title.Remove('}','')
newtitle=title.Remove('{','')



def get_word_list(iyn):
    return iyn.split()
word_list = get_word_list(newtitle)

# Print the list of words
print("List of words:", word_list)

def count_words(iyn):
    words = iyn.split()
    return (len(words))


word_count = count_words(newtitle)
print(f"Number of words: {word_count}")