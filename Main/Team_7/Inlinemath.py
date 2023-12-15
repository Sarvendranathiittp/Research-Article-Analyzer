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

    def get_paren(self, fractions):
        # Generates a list containing beginning index of expressions without parenthesis
        paren_index = []

        for current_fraction in fractions:
            len_expr = 0
            for ind in range(current_fraction[0], current_fraction[1] + 1):
                if self.code[ind] == '{':
                    # Increment ind to enter the while loop
                    ind += 1
                    while self.code[ind] != '}':
                        len_expr += 1
                        ind += 1  # Increment ind inside the while loop
                    if len_expr > 1:
                        paren_index.append(ind)

        return paren_index









