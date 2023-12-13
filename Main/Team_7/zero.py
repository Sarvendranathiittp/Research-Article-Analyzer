class zero:
    def __init__(self,code,begin_index):
        self.code = code
        self.begin_index = begin_index
    def run(self):
        dotindex =[]
        equations_=self.get_inline_equations()
        for i in range(self.begin_index,len(self.code)):
            if (self.code(i) == '.') & ((self.code(i + 1) <= '9') & (self.code(i + 1) >= '0')):
                dotindex.append(i)


    def get_inline_equations(self):
    # A function that generates a list containing starting and ending indices of all the equations
        equations = []
        found = False
        current_equation = []
        for i in range(self.begin_index,len(self.code)):
            if self.code[i] == '$':
                current_equation.append(i)
                if not found:
                    found = True
                else:
                    equations.append(current_equation)
                    current_equation = []
                    found = False
            elif not found and self.code[i:i+len("\\(")] == "\\(":
                current_equation.append(i)
                found = True
            elif found and self.code[i:i+len("\\)")] == "\\)":
                current_equation.append(i)
                equations.append(current_equation)
                found = False
                current_equation = []
            elif not found and self.code[i:i + len("\\begin{math}")] == "\\begin{math}":
                current_equation.append(i)
                found = True
            elif found and self.code[i:i + len("\\end{math}")] == "\\end{math}":
                current_equation.append(i)
                equations.append(current_equation)
                found = False
                current_equation = []
            elif not found and self.code[i:i + len("\\begin{equation}")] == "\\begin{equation}" :
                current_equation.append(i)
                found = True
            elif found and self.code[i:i + len("\\end{equation")] == "\\begin{equation}" :
                current_equation.append(i)
                equations.append(current_equation)
                found = False
                current_equation = []
            elif not found and self.code[i:i + len("\\begin{align}")] == "\\begin{align}" :
                current_equation.append(i)
                found = True
            elif found and self.code[i:i + len("\\end{align}")] =="\\end{align}" :
                current_equation.append(i)
                equations.append(current_equation)
                found = False
                current_equation = []
            elif not found and self.code[i:i + len("\\begin{align*}")] == "\\begin{align*}" :
                current_equation.append(i)
                found = True
            elif found and self.code[i:i + len("\\end{align*}")] =="\\end{align*}" :
                current_equation.append(i)
                equations.append(current_equation)
                found = False
                current_equation = []
            elif not found and self.code[i:i + len("\\begin{bmatrix}")] == "\\begin{bmatrix}" :
                current_equation.append(i)
                found = True
            elif found and self.code[i:i + len("\\end{bmatrix}")] =="\\end{bmatrix}" :
                current_equation.append(i)
                equations.append(current_equation)
                found = False
                current_equation = []
            elif not found and self.code[i:i + len("\\begin{multiline}")] == "\\begin{multiline}" :
                current_equation.append(i)
                found = True
            elif found and self.code[i:i + len("\\end{multiline}")] =="\\end{multiline}" :
                current_equation.append(i)
                equations.append(current_equation)
                found = False
                current_equation = []
            elif not found and self.code[i:i + len("\\begin{multiline*}")] == "\\begin{multiline*}" :
                current_equation.append(i)
                found = True
            elif found and self.code[i:i + len("\\end{multiline*}")] =="\\end{multiline*}" :
                current_equation.append(i)
                equations.append(current_equation)
                found = False
                current_equation = []
            elif not found and self.code[i:i + len("\\begin{gather}")] == "\\begin{gather}" :
                current_equation.append(i)
                found = True
            elif found and self.code[i:i + len("\\end{gather}")] =="\\end{gather}" :
                current_equation.append(i)
                equations.append(current_equation)
                found = False
                current_equation = []
            elif not found and self.code[i:i + len("\\begin{gather*}")] == "\\begin{gather*}" :
                current_equation.append(i)
                found = True
            elif found and self.code[i:i + len("\\end{gather*}")] =="\\end{gather*}" :
                current_equation.append(i)
                equations.append(current_equation)
                found = False
                current_equation = []
            elif not found and self.code[i:i + len("\\begin{tabular}")] == "\\begin{tabular}" :
                current_equation.append(i)
                found = True
            elif found and self.code[i:i + len("\\end{tabular}")] =="\\end{tabular}" :
                current_equation.append(i)
                equations.append(current_equation)
                found = False
                current_equation = []
            elif not found and self.code[i:i + len("\\begin{document}")] == "\\begin{document}" :
                current_equation.append(i)
                found = True
            elif found and self.code[i:i + len("\\end{document}")] =="\\end{document}" :
                current_equation.append(i)
                equations.append(current_equation)
                found = False
                current_equation = []




        return equations








