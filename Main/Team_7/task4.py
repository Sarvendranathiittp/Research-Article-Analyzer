from Main.Team_7.zero import zero


class Task_4:
    def __init__(self, code, begin_index):
        self.code = code
        self.begin_index = begin_index

    @property
    def run(self):
        z = zero(self.code, self.begin_index)
        equations = z.display_equations() + z.get_inline_equations()
        error_index = []
        for eq in equations:
            comma_status = False
            newline_status = False
            for i in range(eq[0], eq[1]):

                if self.code[i] == '.' & (not comma_status):
                    break
                if self.code[i] == ',':
                    comma_status = True
                if (self.code[i: len("\\case")] == "\\case") & (not comma_status):
                    j = i + len("\\case")
                    forall = False
                    while not (self.code[j: len("\\\\")] == "\\\\" & self.code[
                                                                     j: len("\\newline")] == "\\newline" & self.code[
                                                                                                           j: len(
                                                                                                               "\\linebreak")] == "\\linebreak") &self.code[j] == '.':
                        if self.code[j: len("\\forall")] == "\\forall":
                            forall = True
                            break
                        j=j+1
                    if not forall:
                        error_index.append(i)
                elif (self.code[i: len("\\text")] == "\\text") & (not comma_status):
                    j = i + len("\\text")
                    forall = False
                    while not (self.code[j: len("\\\\")] == "\\\\" & self.code[
                                                                     j: len("\\newline")] == "\\newline" & self.code[
                                                                                                           j: len(
                                                                                                               "\\linebreak")] == "\\linebreak") &self.code[j] == '.':
                        if self.code[j: len("\\forall")] == "\\forall":
                            forall = True
                            break
                        j = j + 1
                    if not forall:
                        error_index.append(i)
                elif (self.code[i: len("\\mbox")] == "\\mbox") & (not comma_status):
                    j = i + len("\\mbox")
                    forall = False
                    while not (self.code[j: len("\\\\")] == "\\\\" & self.code[
                                                                     j: len("\\newline")] == "\\newline" & self.code[
                                                                                                           j: len(
                                                                                                               "\\linebreak")] == "\\linebreak") &self.code[j] == '.':
                        if self.code[j: len("\\forall")] == "\\forall":
                            forall = True
                            break
                        j = j + 1
                    if not forall:
                        error_index.append(i)



        return error_index
