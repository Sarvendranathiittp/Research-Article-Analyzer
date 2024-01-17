# Wrapper Class

from tkinter import *
from tkinter import filedialog

# Teams' main file import

from Team_0.task import team_0
from Team_1.Task import team_1
from Team_2.task import team_2
from Team_3.task import team_3
from Team_4.task import team_4
from Team_5.task import team_5
from Team_6.task import team_6
from Team_7.main import team_7
from Team_8.code_bbl import team_8

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
        obj_team_3 = team_3(text,begin_index)
        output.append(obj_team_3.run())
        obj_team_4 = team_4(text,begin_index)
        output.append(obj_team_4.run())
        obj_team_5 = team_5(text,begin_index)
        output.append(obj_team_5.run())
        obj_team_6 = team_6(text,begin_index)
        output.append(obj_team_6.run())
        obj_team_7 = team_7(text,begin_index)
        output.append(obj_team_7.run())
        obj_team_8 = team_8(text,begin_index)
        output.append(obj_team_8.run())

        # Writing all the output logs to the log file
        with open ("LOGII", "a") as logw:
            for logs in output:
                for log in logs:
                    logw.write(log)
                print()

obj = wrapper()
obj.run()