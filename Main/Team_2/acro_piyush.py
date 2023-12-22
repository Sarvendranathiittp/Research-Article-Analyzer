
#Make list of full form of acronyms , acronym and occurance
#make warnings for acro. that are  1) not defined entirely  2) defined but not at first occurrence
#cronym must be followed by parentheses for the first time
#NOTE : If the acronym is not repeated the whole body then no need to add parentheses.
'''Brief of TO DO LIST

1) Output in form of Name of acr -Acro -Occurrence 
     # This includes plural and singular both 

Comments Type 
2) If apostrophe is present ,then " Check whether this is for possessive form or mistaken by user for plural "
    # eliminate the confusion between the actual symbol of ’ and the mistaken symbol  ' 
3)If acronym has been defined but not at the first occurrence then " Acronym is defined on line ___ but not on the first occurrence ,i.e. line___ " otherwise "Acronyms is not defined ,Define it on the line ____ ,i.e. the first occurrence 
  # Also check whether if its a common acronym mentioned in a list we have created ,then don't give the warning if its not defined anywhere but     I    if its defined then it should be at first occurrence
'''
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

        self.acronyms = []
        self.first_occurrence_line = {}
        self.warnings = []
        self.common_acronyms = ['DIY', 'NASA', 'HTML']
           
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
    

    def extract_acronyms(self):
        # Extract acronyms with all capital letters (e.g., TASD)
        capital_acronyms = re.findall(r'\b[A-Z]+\b', self.text)
        
        # Extract acronyms ending with 's' (e.g., LEDs)
        s_suffix_acronyms = re.findall(r'\b[A-Z]+s\b', self.text)

        # Extract acronyms with an apostrophe and 's' (e.g., TA's)
        apostrophe_acronyms = re.findall(r'\b[A-Z]+\'s\b', self.text)

        # Combine the results into a single list
        self.acronyms = capital_acronyms + s_suffix_acronyms + apostrophe_acronyms

    def verify_acronyms(self):
        lines = self.text.split('\n')

        for acronym in self.acronyms:
            first_occurrence_line = None
            defined_at_first_occurrence = False
            defined_without_parentheses = False
            is_common_acronym = acronym in self.common_acronyms

            for line_number, line in enumerate(lines, start=1):
                if re.search(fr'\b{re.escape(acronym)}\b', line):
                    first_occurrence_line = line_number

                    if '(' in line and ')' in line:
                        defined_at_first_occurrence = True

                    if not defined_at_first_occurrence and '(' not in line and ')' not in line:
                        defined_without_parentheses = True

                    break

            if first_occurrence_line is None and not is_common_acronym:
                self.warnings.append(f"Warning: Acronym '{acronym}' is not defined at all.")
            elif not defined_at_first_occurrence:
                if not is_common_acronym:
                    self.warnings.append(f"Warning: Acronym '{acronym}' is defined, but not at the first occurrence (Line {first_occurrence_line}).")
                else:
                    print(f"Acronym '{acronym}' is a common acronym and is not defined at the first occurrence.")
            elif defined_without_parentheses:
                if not is_common_acronym:
                    print(f"Acronym '{acronym}' is defined without parentheses at Line {first_occurrence_line}.")
                else:
                    print(f"Acronym '{acronym}' is a common acronym and is defined without parentheses at Line {first_occurrence_line}.")
            elif is_common_acronym:
                print(f"Acronym '{acronym}' is a common acronym and is defined at Line {first_occurrence_line}, but within parentheses.")

            self.first_occurrence_line[acronym] = first_occurrence_line
        
    def run(self):
        abstract = self.remove_latex_commands(self.extract_abstract()) 
        output = []  # The output would be updated with the extracted title and abstract along with the word counts respectively.

        output.append('\n' + '=' * 50 + "\n\t\t Abstract Related Comments \n" + '=' * 50)

        # Assuming team_2 is your class
        self.text = abstract  # Set the text attribute before creating an instance
        acronym_processor = team_2(self.text,0)
        acronym_processor.extract_acronyms()
        
        if acronym_processor.acronyms:
            acronym_processor.verify_acronyms()
            output.append("List of Acronyms: " + str(acronym_processor.acronyms))
            
            if acronym_processor.warnings:
                output.append("\nWarnings:")
                for warning in acronym_processor.warnings:
                    output.append(warning)
        else:
            output.append("No acronyms found in the given text.")

        return output





