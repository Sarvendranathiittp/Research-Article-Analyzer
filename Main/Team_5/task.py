#example task
import re
class team_5:
    
    def __init__(self, latex_code, text_begin):
        self.latex_code = latex_code
        self.text_begin = text_begin
        
    
    def extract_equations(self,latex_content):
        self.latex_content = latex_content
        
        # Define a regular expression to match equations using \begin{equation}
        equation_pattern = re.compile(r'\\begin\{equation\}(.*?)\\end\{equation\}', re.DOTALL)
    
        # Find all equations in the LaTeX content
        equations = re.findall(equation_pattern, latex_content)
    
        return equations

    def run(self):  # The function which is going to be invoked in the wrapper class should contain no arguments

        output = [] # The output list with the errors to be returned
        text = self.latex_code
        equations = self.extract_equations(text)
        for equation in equations:
          print(equation)
        return output