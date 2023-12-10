# Wrapper Class

from tkinter import *
from tkinter import filedialog
import csv

# Teams' main file import
from Team_0 import team_0


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


obj = wrapper()
obj.run()