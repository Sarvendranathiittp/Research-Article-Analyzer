#1.Count the number of words in the title and abstract.
#2. Create a list of acronyms used.
#3. Count the number of times each acronym occurred.
#4. Identify the acronyms that are not expanded at the first occurrence
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
    
    def remove_latex_commands(self,text):

        # Function to remove LaTeX commands
        text_withoutcommands = re.sub(r'\\[a-zA-Z]+', '', text)
        # Define a regular expression pattern to match the unwanted patterns
        pattern = r'\{[\d.]+(cm|mm)?\}'

        # Use re.sub to replace the matched patterns with an empty string
        cleaned_text = re.sub(pattern, '', text_withoutcommands)
    
        return cleaned_text
   
    def count_words(self, text):
        # Split the text into words and return the count
        words = text.split()
        return len(words)
    
    def run(self):
        abstract = self.extract_abstract()
        title = self.extract_title()
        output = [] # The output would be updated with the extracted title and abstract along with the word counts respectively.

        output.append(f"\n ================================================\n Title Related Comments \n ================================================ ")
    
        if title:          
            #output.append(f"Title (Original): \n{title}")

            # Process the title by removing LaTeX commands
            processed_title = self.remove_latex_commands(title)            
            output.append(f"\n Title (Processed): \n{processed_title}")

            print(f"Title is found,data is updated in LOGII file")

            # Count words in the processed title
            word_count = len(processed_title.split())
            output.append(f"\n Number of words in the processed title: {word_count}")

        else:
            output.append(f"\n No title found.")
            print("No title found.")
        
        output.append(f"\n ================================================\n  Related Comments \n ================================================ ")

        if abstract:

            #output.append(f"Abstract: \n{abstract}")

            # Process the abstract by removing LaTeX commands
            processed_abstract = self.remove_latex_commands(abstract)            
            output.append(f"\n Abstract (Processed): \n{processed_abstract}")

            # Call the count_words method using the obj_team_2 instance
            word_count = self.count_words(abstract)
            print(f"Abstract is found,data is updated in LOGII file")

            output.append(f"\n Number of words in the abstract: {word_count}")
        
        else:
            output.append("\n No abstract found.")

            print("No abstract found.")
        
        
        return output