#example task
import re
class team_5:
    
    def __init__(self, latex_code, text_begin):
        self.latex_code = latex_code
        self.text_begin = text_begin
        # self.filepath = filepath
    
    def check_punctuation(self,latex_content):
        self.latex_content = latex_content
            # Define a regular expression to match LaTeX equations and labels
        equation_pattern = re.compile(r'\\begin{equation}(.*?)\\end{equation}', re.DOTALL)
    
        # Find all equations in the LaTeX file
        equations = re.findall(equation_pattern, latex_content)
    
        for equation in equations:
            # Extract the equation label if present
            # line_number = self.find_equation_line_number(equation)
            label_match = re.search(r'\\label{([^}]*)}', equation)
            last_char = equation.strip()[-1] if equation.strip() else None
            if last_char =="." or last_char ==",":
                index1 = latex_content.find(equation)
            else: 
                if label_match:
                    label = label_match.group(1)
    
                    # Check for punctuation before the label
                    index = equation.find('\\label{' + label + '}')
                    if index > 0:
                        preceding_text = equation[:index]
                    index1 = latex_content.find(equation)
                    # Check if there is a comma or period at the end of the preceding text
                    last_char = preceding_text.strip()[-1] if preceding_text.strip() else None

            if last_char in [',', '.']:
                print(f"Punctuation ({last_char}) found before label '{label}' in equation (if any):\n{equation}")
    
                # Find the index of \end{equation} after the current equation
                end_equation_index = latex_content.find('\\end{equation}', index1)
                if end_equation_index != -1:
                    # Extract the text immediately after \end{equation}
                    text_after_end = latex_content[end_equation_index + len('\\end{equation}'):].lstrip()
    
                    # Find the first word after \end{equation}
                    match = re.search(r'\w+', text_after_end)
    
                    if match:
                        word_after_end = match.group()
                        print(word_after_end)
                        if word_after_end and word_after_end[0].isupper():
                            if last_char != '.':
                                
                                print("The word after \\end{equation} starts with a capital letter, but the punctuation is not a full stop. In line number")
                        else:
                            if last_char != ',':
                                print("The word after \\end{equation} does not start with a capital letter, but the punctuation is not a comma.In line number")
                    else:
                        print("Error: Word after \\end{equation} not found.")
                else:
                    print("Error: \\end{equation} not found after the equation.")
            elif last_char not in [',', '.']:
                print("Warning: Punctuation not found at the end of the equation (if any).In line number")

    # def find_equation_line_number(self,target_equation):
    #     with open(self.filepath, 'r', encoding='utf-8') as file:
    #        line_number = 0

    #        for line in file:
    #           line_number += 1

    #           # Check if the line contains the target equation
    #           if target_equation in line:
    #              return line_number

        # Equation not found in the file
        # return None

        
        

    
    
    
    
    def run(self):  # The function which is going to be invoked in the wrapper class should contain no arguments

        output = [] # The output list with the errors to be returned
        text = self.latex_code
        self.check_punctuation(text)          
        return output