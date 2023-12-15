# Assuming you have the latex_content
latex_content = r"""
{\title{\vspace{0cm} \fontsize{10}{12}\selectfont \textbf{COLOMBIAN JOURNAL OF ADVANCED TECHNOLOGIES INDICATIONS FOR PAPER SUBMITTION} 

\vspace{6mm} \textbf{REVISTA COLOMBIANA DE TECNOLOGÍAS DE AVANZADA INDICACIONES PARA LA PRESENTACIÓN DE ARTÍCULOS}\vspace{4mm}}
\author{\fontsize{10}{12}\selectfont \textbf{\fontsize{10}{12}\selectfont PhD. Autor Principal, Msc. Co-Autor I,} \\ \textbf{\fontsize{10}{12}\selectfont Msc. Co-Autor II}\\ \\
\small{\textbf{\fontsize{10}{12}\selectfont Universidad de Pamplona}}\\
\small{\fontsize{10}{12}\selectfont Comité Editorial Revista Colombiana de Tecnologías de Avanzada}\\
\small{\fontsize{10}{12}\selectfont Ciudadela Universitaria. Pamplona, Norte de Santander, Colombia.} \\ \small{\fontsize{10}{12}\selectfont Tel.: 57-7-5685303, Fax: 57-7-5685303, Ext. 144}\\
\small{\fontsize{10}{12}\selectfont E-mail: \{correo1,correo2,correo3\}@unipamplona.edu.co}
}
"""

# Function to remove LaTeX commands
import re

class team2:
    def __init__(self, latex_content, begin_document_index):
        self.latex_content = latex_content
        self.begin_document_index = begin_document_index

    def process_title(latex_title):
        # Remove LaTeX formatting commands
        processed_title = re.sub(r'\\[a-zA-Z]+\{.*?\}', '', latex_title)
    
        # Remove additional spaces and curly braces
        processed_title = re.sub(r'\s+', ' ', processed_title)
        processed_title = processed_title.strip('{}')
    
        # Remove unwanted numbers
        processed_title = re.sub(r'\b\d+\b', '', processed_title)
    
        # Remove additional spaces and curly braces again
        processed_title = re.sub(r'\s+', ' ', processed_title)
        processed_title = processed_title.strip('{}')

        # Count the number of words
        word_count = len(processed_title.split())

        return processed_title, word_count

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
    


#Example usage:
obj_team2 = team2(latex_content, 0)  # begin_document_index
title = obj_team2.extract_title()

if title:
        print("Title (Original):")
        print(title)

        processed_title, word_count = process_title(title)

        print(f"Title (Processed): {processed_title}")
        print(f"Number of words in the processed title: {word_count}")
else:
        print("No title found.")
