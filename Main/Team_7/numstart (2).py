class NumStart:
    def __init__(self, code, begin_index):
        self.code = code
        self.begin_index = begin_index

    def run(self):
        error_index = []
        for i in range(len(self.code)):
            if self.code[i] == '.':
                j = i + 1
                while not self.code[j].isalphanum:
                    if self.code[j] == '$':
                        error_index.append(j)
                    else:
                        j += 1
        return error_index
