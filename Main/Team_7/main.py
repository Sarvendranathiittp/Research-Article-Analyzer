from Main.Team_7.zero import zero
from Main.Team_7.numstart import NumStart


class team_7:
    def __init__(self, latex_code, text_begin):
        self.latex_code = latex_code
        self.text_begin = text_begin
        self.n = len(self.latex_code)

    def run(self):
        z = zero(self.latex_code, self.text_begin)
        s1, s2 = z.run()
        n = NumStart(self.latex_code, self.text_begin)

    # Calculates the line at which the index is present
    def get_line(self, index):
        line = 1
        for i in range(0, self.n):
            if i == index:
                return line
            elif self.latex_code[i] == '\n':
                line += 1
        return None

    def create_error_msg(self,error_index_list, error_type):
        string_list = []
        for i in error_index_list:
            error_string = f"{error_type} at line {self.get_line(i)}"
            string_list.append(error_string)
        return string_list



