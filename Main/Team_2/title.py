# Assuming you have the latex_content
latex_content = r"""
{\title{
\vspace*{1cm}
\Large{ Article title in ENGLISH (12pt, capitalized the first letter of each word [except connectors])\\
\large{\textcolor{carnelian}{\emph{Título del Artículo en ESPAÑOL (12pt, con mayúsculas la primera letra de cada palabra (excepto conectores)}}}
\\[0.2cm]}}}
"""

import re

# Function to remove LaTeX commands
def remove_latex_commands(text):
    return re.sub(r'\\[a-zA-Z]+', '', text)

class team2:
    def __init__(self, latex_content, begin_document_index):
        self.latex_content = latex_content
        self.begin_document_index = begin_document_index

    def extract_title(self, title_command=r'\title', opening_brace='{', closing_brace='}'):
        begin_title_index = self.latex_content.find(title_command, self.begin_document_index)

        # Find the index of the opening curly brace after the title command
        # Find the index of the title command using the given begin_document_index
        opening_brace_index = self.latex_content.find(opening_brace, begin_title_index)

        # Initialize variables to track the depth of nested curly braces
        depth = 0
        current_index = opening_brace_index + 1  # Start from the character after the opening brace

        # Iterate through characters starting from the opening brace
        while current_index < len(self.latex_content):
            current_char = self.latex_content[current_index]

            if current_char == opening_brace:
                depth += 1
            elif current_char == closing_brace:
                depth -= 1

            # Include any text until the next closing brace is found
        if depth == -1:
            title_content = self.latex_content[opening_brace_index + 1:current_index].strip()
            return title_content

        current_index += 1

        return None
     

# Example usage:
#latex_file_path = r"C:\Users\Piyush\Github_repo\Research-Article-Analyzer\Resources\Latex_example\AS_in_CR_OC_SPU_cam_ready_v5.tex"
#begin_document_index = 18804  # Replace with the actual index of \begin{document}

#with open(latex_file_path, 'r', encoding='utf-8') as latex_file:
 #   latex_content = latex_file.read()

# Assuming you have the begin_document_index
obj_team2 = team2(latex_content, 0)#begin_document_index
title = obj_team2.extract_title()

if title:
    print("Title (Original):")
    print(title)

    # Process the title by removing LaTeX commands
    processed_title = remove_latex_commands(title)
    print("Title (Processed):")
    print(processed_title)

    # Count words in the processed title
    word_count = len(processed_title.split())
    print(f"Number of words in the processed title: {word_count}")
else:
    print("No title found.")
