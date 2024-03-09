from Team_7.Inlinemath import Inline
from Team_7.task2 import Task_2
from Team_7.task4 import Task_4
from Team_7.zero import zero
from Team_7.numstart import NumStart


class team_7:
    def __init__(self, latex_code, text_begin):
        self.latex_code = latex_code
        self.text_begin = text_begin
        self.n = len(self.latex_code)

    def run(self):
        z = zero(self.latex_code, self.text_begin)
        s1, s1_ = z.run()
        n = NumStart(self.latex_code, self.text_begin)
        t2 = Task_2(self.latex_code, self.text_begin)
        s2 = t2.run()
        inmath = Inline(self.latex_code, self.text_begin)
        s3 = inmath.get_paren(inmath.getfrac())
        s3_ = inmath.get_exp()
        t4 = Task_4(self.latex_code,self.text_begin)
        s4, s4_ = t4.run
        t2 = Task_2(self.latex_code,self.text_begin)
        s2 = t2.run()
        error_string=[]
        error_string = error_string + ['='*50 + "\n"]
        error_string =error_string + self.create_error_msg(s1,"Leading zero error.")
        error_string = error_string + self.create_error_msg(s1_, "Trailing zero error.")
        error_string = error_string + self.create_error_msg(s2, "Sentence starting with number warning.")
        error_string = error_string + self.create_error_msg(s3, "Extra Parenthesis warning.")
        error_string = error_string + self.create_error_msg(s3_, "Long Exponential expression warning.")
        error_string = error_string + self.create_error_msg(s4, "No comma before condition warning.")
        error_string = error_string + self.create_error_msg(s4_, "No required space at expression and condition.")
        str= ''
        pruned_error_str = []
        for i in error_string:
            if i not in pruned_error_str:
                pruned_error_str.append(i)
        return pruned_error_str
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
            if not self.is_in_comment(i):
                error_string = f"Line {self.get_line(i)}: {error_type}\n"
                string_list.append(error_string)
        return string_list

    def get_comment_list(self):
        is_in_comment = False
        comment_list = []
        comment_indices = []
        for i in range(self.n):
            if self.latex_code[i] == '%' and not is_in_comment:
                is_in_comment = True
                comment_indices.append(i)
            elif self.latex_code[i] == '\n' and is_in_comment:
                is_in_comment = False
                comment_indices.append(i)
                comment_list.append(comment_indices)
                comment_indices = []
        return comment_list

    def is_in_comment(self, index):
        in_comment = False
        c_list = self.get_comment_list()
        for i in c_list:
            if i[0]<=index<=i[1]:
                in_comment = True
        return in_comment





