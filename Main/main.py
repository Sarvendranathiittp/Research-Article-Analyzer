# Wrapper Class

from tkinter import *
from tkinter import filedialog
import csv

# Teams' main file import
from Team_0.task import team_0


class wrapper:

    def run(self):
        filepath = filedialog.askopenfilename()
        acronyms = 0  # number of acronyms
        acronym_word = []  # creating a list to store acronyms found in the file
        raw_data = []
        with open(filepath,'r',errors='ignore') as file:
            text=str(file.read())

        # Calling all team run() files
        obj_team_0 = team_0(text)
        output_team_0 = obj_team_0.run()




        # Writing all the output logs to the log file
        with open ("LOGII", "a") as logw:
            for log in output_team_0:
                logw.write(log)

obj = wrapper()
obj.run()