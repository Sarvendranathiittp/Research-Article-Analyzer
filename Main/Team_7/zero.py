class zero:
    def __init__(self,code,begin_index):
        self.code=code
        self.begin_index=begin_index
    def run(self):
        dotindex =[]
        for i in range(self.begin_index,len(self.code)):
            if (self.code(i) == '.') & ((self.code(i + 1) <= '9') & (self.code(i + 1) >= '0')):
                dotindex.append(i)


