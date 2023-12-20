# Wrapper Class

from tkinter import *
from tkinter import filedialog

# Teams' main file import

from Team_0.task import team_0
from Team_1.Task import team_1
from Team_2.task import team_2
from Team_5.task import team_5


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

        obj_team_0 = team_0(text,begin_index)
        output.append(obj_team_0.run())
        obj_team_1 = team_1(text,begin_index)
        output.append(obj_team_1.run())
        obj_team_2 =team_2(text,0)
        output.append(obj_team_2.run())
        obj_team_5 = team_5(text,begin_index)
        output.append(obj_team_5.run())

        

        # Writing all the output logs to the log file
        with open ("LOGII", "a") as logw:
            for logs in output:
                for log in logs:
                    logw.write(log)
                print()

obj = wrapper()
obj.run()