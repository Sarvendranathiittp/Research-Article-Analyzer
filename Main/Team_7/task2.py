from Main.Team_7.zero import zero


class Task_2:
    def __init__(self, code, begin_index):
        self.begin_index = begin_index
        self.code = code

    def run(self):
        z = zero(self.code, self.begin_index)
        equations = z.get_inline_equations() + z.display_equations()
        dot_index = []
        for i in range(self.begin_index, len(self.code)):
            if (self.code[i] == '.') & (not (z.is_in_equation(i, equations))):
                dot_index.append(i)
        error_index = []
        for ind in dot_index:
            i = ind
            while i < len(self.code):
                if not (self.code[i] == ' '):
                    break
                i += 1
            if self.code[i].isdigit():
                error_index.append(i)
        return error_index
