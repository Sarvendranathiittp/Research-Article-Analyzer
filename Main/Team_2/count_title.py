class team2:
    def __init__(self, latex_content, begin_document_index):
        self.latex_content = latex_content
        self.begin_document_index = begin_document_index
    
    def extract_title(self, title_command=r'\title', opening_brace='{', closing_brace='}'):
        # Find the index of the title command using the given begin_document_index
        begin_title_index = self.latex_content.find(title_command, self.begin_document_index)

        # Find the index of the opening curly brace after the title command
        opening_brace_index = self.latex_content.find(opening_brace, begin_title_index)

        # Initialize variables to track the depth of nested curly braces
        depth = 0
        current_index = opening_brace_index

        # Iterate through characters starting from the opening brace
        while current_index < len(self.latex_content):
            current_char = self.latex_content[current_index]

        if current_char == opening_brace:
            depth += 1
        elif current_char == closing_brace:
            depth -= 1

        # Check if the closing brace is found and the depth becomes zero
        if depth == 0 and current_char == closing_brace:
            title_content = self.latex_content[opening_brace_index + 1:current_index].strip()
            return title_content

        current_index += 1

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
