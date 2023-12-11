class team_1:
    #Constructor
    def __init__(self, latex_code, text_begin):
        self.latex_code = latex_code
        self.text_begin = text_begin # location of \begin

    def run(self): # will be invoked by wrapper, shouldn't take arguments
        output = []
        text = self.latex_code
        """
        Call ur functions and append the output to the output list
        """
        return output
        # return output # all output ahould be written in this var
    """
    Make seperate functions for whatever you do and call it in run
    """
