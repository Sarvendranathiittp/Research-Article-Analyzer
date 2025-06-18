# Wrapper Class

from tkinter import *
from tkinter import filedialog, messagebox
import shutil
import os

# Teams' main file import

from Team_0.task import team_0
from Team_1.Task import team_1
from Team_2.task import team_2
from Team_3.task import team_3
from Team_4.task import team_4
from Team_5.task import team_5
from Team_6.task import team_6
from Team_7.main import team_7
from Team_8.code_tex import team_8

class wrapper:

    def __init__(self, master):
        self.master = master
        master.title("Research Article Analyzer GUI")

        self.title_label = Label(master, text="Research Article Analyzer", font=("Helvetica", 20))
        self.title_label.pack(pady=10)

        self.description_label = Label(master, text="Select a LaTeX File to detect and analyze errors", font=("Helvetica", 15))
        self.description_label.pack(pady=5)

        self.button = Button(master, text="Upload .tex/.bbl file", command=self.show_wait_screen)
        self.button.pack(pady=20)

        # the wait screen 
        self.wait_screen = Toplevel()
        self.wait_screen.geometry("500x100")
        self.wait_screen.title("Research Article Analyzer GUI")
        self.wait_label = Label(self.wait_screen, text="Please wait while the output is being processed...", font=("Helvetica", 15))
        self.wait_label.pack(pady=20)
        self.wait_screen.withdraw()  # Hide the wait screen initially

    def show_wait_screen(self):
        self.master.withdraw()  # Hide the main window
        self.wait_screen.deiconify()  # Show the wait screen
        self.master.after(100, self.run)

    def run(self):
        filepath = filedialog.askopenfilename()
        raw_data = []
        output = []
        bbl_text =  ""

        with open(filepath,'r',errors='ignore') as file:
            text=str(file.read())
        begin_index = text.find(r'\begin{document}')

        if filepath:
            # Creating a LOG file in the same directory as the input file
            ip_dir = os.path.dirname(filepath)
            
            # Get the original file name of the input  without extension
            ip_file_basename = os.path.splitext(os.path.basename(filepath))[0] 

            # creating the new log file
            log_filename =ip_file_basename +"_comments.log"
            
            # Construction of full path for the new log file in the same directory as the input file
            out_filepath = os.path.join(ip_dir,log_filename )
            
            # Checking if .bbl file exists in the same directory as the input file
            ip_dir_ext = os.path.splitext(os.path.basename(filepath))[0]
            bbl_path = os.path.join(ip_dir, ip_dir_ext+".bbl")

            if os.path.exists(bbl_path):
                with open(bbl_path, 'r') as bbl_file:
                    bbl_text = str(bbl_file.read())
                    begin_index = bbl_text.find(r'\begin{document}')

        # Calling all team run() files
        team_classes = [team_1, team_2, team_3, team_4, team_5, team_6, team_7, team_8]
        for team_class in team_classes:
            try:
                obj_team = team_class(text, begin_index)
                output.append(obj_team.run())
            except Exception as e:
                print(f"Error in team {team_class.__name__} : {e}")

        #Writing all the output logs to the log file
        with open (out_filepath, "w") as logw:
            for logs in output:
                for log in logs:
                    logw.write(log)
                logw.write("\n")
                logw.write("\n")
        
        with open ("LOGII", "w") as logw:
            for logs in output:
                for log in logs:
                    logw.write(log)
                logw.write("\n")
                logw.write("\n")

        # Close wait screen and open output screen
        self.wait_screen.destroy()
        self.open_output_screen(out_filepath)

    def open_output_screen(self, output_file_path):
        output_screen = Toplevel()
        output_screen.title("Research Article Analyzer GUI")

        output_text_area = Text(output_screen)
        output_text_area.pack(fill=BOTH, expand=YES)

        # Display contents of LOG file if it exists
        if os.path.exists(output_file_path):
            with open(output_file_path, "r") as log_file:
                output_text = log_file.read()
            output_text_area.insert(END, output_text)
            output_text_area.config(state=DISABLED)
            
            # Add download button if LOG file exists
            download_button = Button(output_screen, text="Download LOG File", command=lambda: self.download_log(output_file_path))
            download_button.pack(pady=10)

        else:
            output_text_area.insert(END, "No output available.")

        output_screen.protocol("WM_DELETE_WINDOW", self.close_program)
    
    def close_program(self):
        self.master.destroy()

    def download_log(self, output_file_path):
        # Open file dialog to choose download location
        download_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if download_path:
            # Copy content of LOG to the selected location
            with open(output_file_path, "r") as log_file:
                with open(download_path, "w") as download_file:
                    download_file.write(log_file.read())
            messagebox.showinfo("Download Complete", "LOG downloaded successfully.")


# obj = wrapper()
# obj.run()
root = Tk()
root.geometry("500x300")
wrapper_gui = wrapper(root)
root.mainloop()