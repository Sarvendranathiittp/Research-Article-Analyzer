class Inline:
    def __init__(self, code, begin_index):
        self.code=code
        self.begin_index = begin_index
    def getfrac(self):
        # Generates a list containing beginning and ending index of fraction block
        fractions =[]
        found=False
        current_fraction =[]
        for i in range(self.begin_index,len(self.code)):
            if self.code[i:i + len("\\frac")] == "\\frac":
                for j in range(2):
                    while not(self.code[i]=='{'):
                        i+=1
                    ind1 = i
                    while not(self.code[i]=='}'):
                        i+=1
                    ind2=i
                    current_fraction.append(ind1)
                    current_fraction.append(ind2)
                    fractions.append(current_fraction)
                    current_fraction = []
        return fractions


    def get_paren(self, fractions):
        # Generates a list containing beginning index of expressions without parenthesis
        paren_index = []
        for current_fraction in fractions:
            len_expr = 0
            for ind in range(current_fraction[0], current_fraction[1] + 1):
                paren_status = False
                op_status = False
                left = ind
                if self.code[ind] == '{':
                    while not(self.code[ind] == '}'):
                        if self.code[ind]=='(':
                            paren_status=True
                        if isop(self.code[ind]):
                            op_status=True
                        ind+=1
                    if ind-left-2 > 1 and (not(paren_status))  and (op_status):
                        paren_index.append(ind-2)


        return paren_index
    def get_exp(self):
    # Geneartes a list of indices which are at exponential functions
        exp_index =[]
        for i in range(self.begin_index,len(self.code)) :
            if (self.code[i] == 'e') and (self.code[i+1] == '^'):
                exp_index.append(i)

        return exp_index
    def get_line(self, index):
        line = 1
        for i in range(0, len(self.code)):
            if i == index:
                return line
            elif self.code[i] == '\n':
                line += 1
        return None
    
def isop(ch):
    if ch=='+' or ch=='-' or ch=='/' or ch=='%':
        return True
    return False









