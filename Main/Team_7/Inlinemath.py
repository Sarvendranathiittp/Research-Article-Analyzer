class Inline:
    def __intit__(self,code,begin_index):
        self.code=code
        self.begin_index=begin_index
    def getfrac(self):
        # Generates a list containing beginning and ending index of fraction block
        fractions =[]
        found=False
        current_fraction =[]
        for i in range(self.begin_index,len(self.code)):
            if self.code[i:i+len("\\frac")] == "\\frac" :
                current_fraction.append(i)
                if not found:
                    found=True
                else:
                    fractions.append(current_fraction)
                    current_fraction=[]
                    found=False
        return fractions
    