class zero:
    def __init__(self,code,begin_index):
        self.code = code
        self.begin_index = begin_index

    def run(self):
        dotindex =[]
        for i in range(self.begin_index,len(self.code)):
            if (self.code(i) == '.') & ((self.code(i + 1) <= '9') & (self.code(i + 1) >= '0')):
                dotindex.append(i)

    def get_inline_equations(self):
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
        return equations






