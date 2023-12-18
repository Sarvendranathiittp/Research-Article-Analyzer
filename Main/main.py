# Wrapper Class

from tkinter import *
from tkinter import filedialog

# Teams' main file import
#from Team_0.task import team_0
from Team_2.task import team_2
from Team_2.acronyms1 import team_2a



class wrapper:

    def run(self):
        filepath = filedialog.askopenfilename()
        raw_data = []
        output = []
        storage=[]

        with open(filepath,'r',errors='ignore') as file:
            text=str(file.read())
        begin_index = text.find(r'\begin{document}')

        # Calling all team run() files
        #obj_team_0 = team_0(text,begin_index)
        #output.append(obj_team_0.run())
        obj_team2= team_2(text,0)
        output.append(obj_team2.run())

        # Access processed_abstract from team_2 instance
        processed_abstract = obj_team2.remove_latex_commands(obj_team2.extract_abstract()) 
        obj_team2a=team_2a(processed_abstract)
        storage.append(obj_team2a.run())
        




        # Writing all the output logs to the log file
        with open ("LOGII_a", "a") as logw:
            for logs in storage:
                for log in logs:
                    logw.write(log)
                    print(log)
                print()

obj = wrapper()
obj.run()