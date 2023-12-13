from Main.Team_7.zero import zero
from Main.Team_7.numstart import NumStart

class team_7:
    def __init__(self, latex_code, text_begin):
        self.latex_code = latex_code
        self.text_begin = text_begin
    def run(self):
        z = zero(self.latex_code,self.text_begin)
        s = z.run()
        n = NumStart(self.latex_code,self.text_begin)


