#1.Count the number of words in the title and abstract.
#2. Create a list of acronyms used.
#3. Count the number of times each acronym occurred.
#4. Identify the acronyms that are not expanded at the first occurrence .

#Instructions: pip install tabulate
'''Pending tasks 
    
    NOTE : If the acronym is not repeated the whole body then no need to add parentheses.

1) Output in form of Name of acr -Acro -Occurrence 
     # This includes plural and singular both 

Comments Type 
2) If apostrophe is present ,then " Check whether this is for possessive form or mistaken by user for plural "
    # eliminate the confusion between the actual symbol of ’ and the mistaken symbol  ' 
 '''
import re   
from tabulate import tabulate
acronyms_dict = {
    "AF": "Audio frequency",
    "AFC": "Automatic frequency control",
    "AGC": "Automatic gain control",
    "AM": "Amplitude modulation",
    "APD": "Avalanche photodiode",
    "AR": "Antireflection",
    "ARMA": "Autoregressive moving average",
    "ASIC": "Application-specified integrated circuit",
    "ASK": "Amplitude shift keying",
    "ATM": "Asynchronous transfer mode",
    "AWGN": "Additive white Gaussian noise",
    "BER": "Bit error rate",
    "BPSK": "Binary phase-shift keying",
    "BWO": "Backward-wave oscillator",
    "CCD": "Charge-coupled device",
    "CDMA": "Code division multiple access",
    "CD-ROM": "Compact disk read-only memory",
    "CIM": "Computer integrated manufacturing",
    "CIR": "Carrier-to-interference ratio",
    "CMOS": "Complimentary metal–oxide–semiconductor",
    "CPFSK": "Continuous phase frequency-shift keying",
    "CPM": "Continuous phase modulation",
    "CPSK": "Continuous phase-shift keying",
    "CPU": "Central processing unit",
    "CRT": "Cathode-ray tube",
    "CT": "Current transformer",
    "CV": "Capacitance–voltage",
    "CW": "Continuous wave",
    "DC": "Direct current",
    "DFT": "Discrete Fourier transform",
    "DMA": "Direct memory access",
    "DPCM": "Differential pulse code modulation",
    "DPSK": "Differential phase-shift keying",
    "EDP": "Electronic data processing",
    "EHF": "Extremely high frequency",
    "ELF": "Extremely low frequency",
    "EMC": "Electromagnetic compatibility",
    "EMF": "Electromotive force",
    "EMI": "Electromagnetic interference",
    "FDM": "Frequency division multiplexing",
    "FDMA": "Frequency division multiple access",
    "FET": "Field-effect transistor",
    "FFT": "Fast Fourier transform",
    "FIR": "Finite-impulse response",
    "FM": "Frequency modulation",
    "FSK": "Frequency-shift keying",
    "FTP": "File transfer protocol",
    "FWHM": "Full-width at half-maximum",
    "GUI": "Graphical user interface",
    "HBT": "Heterojunction bipolar transistor",
    "HEMT": "High-electron mobility transistor",
    "HF": "High frequency",
    "HTML": "Hypertext markup language",
    "HV": "High voltage",
    "HVdc": "High voltage direct current",
    "IC": "Integrated circuit",
    "IDP": "Integrated data processing",
    "IF": "Intermediate frequency",
    "IGFET": "Insulated-gate field-effect transistor",
    "IM": "Intermediate modulation",
    "IMPATT": "Impact ionization avalanche transit time (diode)",
    "I/O": "Input–output",
    "IR": "Infrared",
    "ISI": "Intersymbol interference",
    "JFET": "Junction field-effect transistor",
    "JPEG": "Joint Photographers Expert Group",
    "LAN": "Local area network",
    "LC": "Inductance–capacitance",
    "LED": "Light-emitting diode",
    "LHS": "Left-hand side",
    "LMS": "Least mean square",
    "LO": "Local oscillator",
    "LP": "Linear programming",
    "LPE": "Liquid phase epitaxy",
    "LR": "Inductance–resistance",
    "MESFET": "Metal–semiconductor field-effect transistor",
    "MF": "Medium frequency",
    "MFSK": "Minimum frequency-shift keying",
    "MHD": "Magnetohydrodynamics",
    "MIS": "Metal–insulator–semiconductor",
    "MLE": "Maximum-likelihood estimator",
    "MLSE": "Maximum-likelihood sequence estimator",
    "MMF": "Magnetomotive force",
    "MOS": "Metal–oxide–semiconductor",
    "MOSFET": "Metal–oxide–semiconductor field-effect transistor",
    "MOST": "Metal–oxide–semiconductor transistor",
    "MPEG": "Motion Pictures Expert Group",
    "NIR": "Near infrared response",
    "NMR": "Nuclear magnetic resonance",
    "NRZ": "Nonreturn to zero",
    "OD": "Outside diameter",
    "OEIC": "Optoelectronic integrated circuit",
    "OOP": "Object-oriented programming",
    "PAM": "Pulse-amplitude modulation",
    "PC": "Personal computer",
    "PCM": "Pulse-code modulation",
    "PDF": "Probability density function",
    "PDM": "Pulse-duration modulation",
    "PF": "Power factor",
    "PID": "Proportional-integral differential",
    "PLL": "Phase-locked loop",
    "PM": "Phase modulation",
    "PML": "Perfectly matched layer",
    "PP": "Peak-to-peak",
    "PPM": "Pulse-position modulation",
    "PRF": "Pulse-repetition frequency",
    "PRR": "Pulse-repetition rate",
    "PSK": "Phase-shift keying",
    "PTM": "Pulse–time modulation",
    "PWM": "Pulse width modulation",
    "Q": "Quality factor",
    "QoS": "Quality of service",
    "QPSK": "Quaternary phase-shift keying",
    "RAM": "Random access memory",
    "RC": "Resistance–capacitance",
    "RF": "Radio frequency",
    "RFI": "Radio frequency interference",
    "RIN": "Relative intensity noise",
    "RL": "Resistance–inductance",
    "R&D": "Research and development",
    "RV": "Random variable",
    "SAW": "Surface acoustic wave",
    "SGML": "Standard generalized markup language",
    "SHF": "Super high frequency",
    "SI": "International System of Units",
    "SIR": "Signal-to-interference ratio",
    "S/N": "Signal-to-noise ratio",
    "SOC": "System-on-a-chip",
    "SSB": "Single sideband",
    "SW": "Short wave",
    "SWR": "Standing-wave ratio",
    "TDM": "Time-division modulation",
    "TDMA": "Time-division multiple access",
    "TE": "Transverse electric",
    "TEM": "Transverse electromagnetic",
    "TFT": "Thin-film transistor",
    "TM": "Transverse magnetic",
    "TVI": "Television interference",
    "TWA": "Traveling-wave amplifier",
    "UHF": "Ultrahigh frequency",
    "UV": "Ultraviolet",
    "VCO": "Voltage-controlled oscillator",
    "VHF": "Very high frequency",
    "VLSI": "Very large scale integration",
    "WAN": "Wide area network",
    "WDM": "Wavelength division multiplexing",
}


class team_2:
    def __init__(self, latex_content, begin_document_index):        

        self.latex_content = latex_content
        
        title_index = latex_content.find(r'\title{')
        begin_document_index = latex_content.find(r'\begin{document}')

        # Check if both indices were found
        if title_index != -1 and begin_document_index != -1:
            # Choose the minimum index (earlier occurrence)
            begin_index = min(title_index, begin_document_index)
        else:
            # If one index is -1, choose the other (whichever is not -1)
            begin_index = max(title_index, begin_document_index)

        self.begin_document_index = begin_index

        self.text=""
        self.work=""
        self.error=[]
        self.line_number=0
        self.keyword_line=0
        self.acronyms = []
        self.acro_count={}
        self.acro_full={}
        self.warnings = []

    def extract_title(self, title_command=r'\title', opening_brace='{', closing_brace='}'):
        # Find the index of the title command using the given begin_document_index
        begin_title_index = self.latex_content.find(title_command, self.begin_document_index)

        # Find the index of the opening curly brace after the title command
        opening_brace_index = self.latex_content.find(opening_brace, begin_title_index)

        # Initialize variables to track the depth of nested curly braces
        depth = 0
        current_index = opening_brace_index

        # Iterate through characters starting from the opening brace
        while current_index < len(self.latex_content):
            current_char = self.latex_content[current_index]

            if current_char == opening_brace:
                depth += 1
            elif current_char == closing_brace:
                depth -= 1

            # Check if the closing brace is found and the depth becomes zero
            if depth == 0 and current_char == closing_brace:
                title_content = self.latex_content[opening_brace_index + 1:current_index].strip()
                return title_content

            current_index += 1

        return None
    
    def extract_abstract(self):
        # Find the index of \begin{abstract} using the given begin_document_index
        begin_abstract_index = self.latex_content.find(r'\begin{abstract}', self.begin_document_index)

        # Find the index of \end{abstract}
        end_abstract_index = self.latex_content.find(r'\end{abstract}', begin_abstract_index)

        # Extract the abstract content without \begin{abstract} and \end{abstract}
        if begin_abstract_index != -1 and end_abstract_index != -1:
            abstract_content = self.latex_content[begin_abstract_index + len(r'\begin{abstract}'):end_abstract_index]
           
            # Count the number of newlines before the abstract_start_index to get the line number
            self.line_number = self.latex_content.count('\n', 0, begin_abstract_index) + 1
            
            return abstract_content
        else:
            return None
       
       
    def extract_keywords(self):
        # Find the index of \begin{abstract} using the given begin_document_index
        begin_keywords_index = self.latex_content.find(r'\begin{IEEEkeywords}', self.begin_document_index)
        
        # Find the index of \end{abstract}
        end_keywords_index = self.latex_content.find(r'\end{IEEEkeywords}', begin_keywords_index)

        # Extract the abstract content without \begin{abstract} and \end{abstract}
        if begin_keywords_index != -1 and end_keywords_index != -1:
            keywords_content = self.latex_content[begin_keywords_index + len(r'\begin{IEEEkeywords}'):end_keywords_index]
            
             # Count the number of newlines before the abstract_start_index to get the line number
            self.keyword_line = self.latex_content.count('\n', 0, begin_keywords_index) + 1
                
            return keywords_content
        else:
            return None
        
       
    def remove_latex_commands(self,text):
        
        # Function to remove LaTeX commands
        text_withoutcommands = re.sub(r'\\[a-zA-Z]+', '', text.strip())
        # Define a regular expression pattern to match the unwanted patterns
        pattern = r'\{[\d.]+(cm|mm)?\}'

        # Use re.sub to replace the matched patterns with an empty string
        cleaned_text = re.sub(pattern, '', text_withoutcommands)
        # Split the cleaned text into words
        words = cleaned_text.split()
        
        if words:
            # Get the first word
            first_word = words[0]
            
            # Find the index of the first occurrence of the first word in the original text
            end_index = text.find(first_word)
            
            # Count the number of newline characters before the first word
            count_newlines = text[:end_index].count('\n')
            
            # Update the line number
            self.line_number += count_newlines
        
        return cleaned_text
    
    
    def remove_latex_commands1(self,text):
        
        # Function to remove LaTeX commands
        text_withoutcommands = re.sub(r'\\[a-zA-Z]+', '', text.strip())
        # Define a regular expression pattern to match the unwanted patterns
        pattern = r'\{[\d.]+(cm|mm)?\}'

        # Use re.sub to replace the matched patterns with an empty string
        cleaned_text = re.sub(pattern, '', text_withoutcommands)
        # Split the cleaned text into words
        words = cleaned_text.split()
        
        if words:
            # Get the first word
            first_word = words[0]
            
            # Find the index of the first occurrence of the first word in the original text
            end_index = text.find(first_word)
            
            # Count the number of newline characters before the first word
            count_newlines = text[:end_index].count('\n')
            
            # Update the line number
            self.keyword_line += count_newlines
        
        return cleaned_text
    
    

    def count_words(self, text):
        # Split the text into words and return the count
        words = text.split()
        return len(words)
   
    def extract_acronyms(self):
        # Extract acronyms with all capital letters (e.g., TASD)
        capital_acronyms = re.findall(r'\b[A-Z]+\b', self.text)
        
        # Extract acronyms ending with 's' (e.g., LEDs)
        s_suffix_acronyms = re.findall(r'\b[A-Z]+s\b', self.text)

        # Extract acronyms with an apostrophe and 's' (e.g., TA's)
        apostrophe_acronyms = re.findall(r'\b[A-Z]+\'s\b', self.text)

        # Combine the results into a single list
        self.acronyms = capital_acronyms + s_suffix_acronyms + apostrophe_acronyms

    def count_acronyms_occurrences(self):
        
        for word in self.acronyms:
            if word in self.acro_count:
                self.acro_count[word] += 1
            else:
                self.acro_count[word] = 1

    def check_enclosed_in_parentheses(self,acronym):
        # Check if the acronym is properly enclosed within parentheses 
        pattern = re.compile(rf'\({re.escape(acronym)}\)')
        return bool(pattern.search(self.work))

    def acro_defined(self,acronym):
        # Count the number of uppercase letters in the acronym
        num_uppercase = sum(1 for char in acronym if char.isupper())

       # Find the position of the acronym in the text
        acronym_position = self.work.find(acronym)

       # Count the number of newline characters before the acronym
        num_newlines_before_acronym = self.work.count('\n', 0, acronym_position)

        # Increment the line number by the number of newline characters before the acronym
        self.line_acro = '{:04d}'.format(int(self.line_acro) + num_newlines_before_acronym)
       
       # Find the substring before the acronym
        substring_before_acronym = self.work[:acronym_position]
        
       # Remove the substring before the acronym position, including the acronym
        self.work = self.work[acronym_position + len(acronym):]
    
        # Find the n words before the acronym (excluding non-alphabetic characters)
        words_before = re.findall(r'\b\w+\b', substring_before_acronym)[-num_uppercase:]

        # Join the initial characters of the words before the acronym
        initial_chars = ''.join(word[0].upper() for word in words_before)
        
        # Check if the words before the acronym match its initial characters
        if initial_chars.upper() == acronym.upper() :    
                # Add the full form of the acronym to the dictionary
                self.acro_full[acronym] = ' '.join(words_before)
                return True
        else:
            # Return False if the acronym is not defined
            return False


    def verify_acronyms(self):       
        self.full_form_counts = {}
        self.parentheses_counts = {}

        for acronym, count in self.acro_count.items():
            self.work=self.text
            if acronym in self.remove_latex_commands(self.extract_abstract()):
                self.line_acro=self.line_number
            else:
                self.line_acro=self.keyword_line
            is_common_acronym = acronym in acronyms_dict
            for i in range(count):                
                enclosed_in_parentheses = self.check_enclosed_in_parentheses(acronym)
                full_form =self.acro_defined(acronym) 
                full_form_value = self.acro_full.get(acronym, None)

                # Count parentheses usage
                if enclosed_in_parentheses:
                    self.parentheses_counts[acronym] = self.parentheses_counts.get(acronym, 0) + 1

                # Count repeated definitions
                if full_form and full_form_value:
                    key = (acronym, full_form_value)
                    self.full_form_counts[key] = self.full_form_counts.get(key, 0) + 1
            
                # Check if the acronym is properly defined at the first occurrence                      
                if i == 0: 
                            
                    if i == 0: 
                        if full_form and not enclosed_in_parentheses:
                            self.warnings.append(f"\nLine {self.line_acro} [Warning]: Acronym '{acronym}' is properly expanded but not enclosed in parentheses at the first occurrence.")
                        elif not full_form and enclosed_in_parentheses:
                            if is_common_acronym:
                                # Use the full form from the common acronym dictionary
                                full_form = acronyms_dict[acronym]
                                self.warnings.append(f"\nLine {self.line_acro} [Warning]: '{acronym}' is not properly expanded at the first occurrence.\n\t\t\t\t\t It is a common acronym Full form: {full_form}.Define if it doesn't matched with your defination.")
                            else:
                                self.warnings.append(f"\nLine {self.line_acro} [Warning]: Acronym '{acronym}' is not properly expanded at the first occurrence.")
                        elif not full_form and not enclosed_in_parentheses:
                            if is_common_acronym:
                                #Use the full form from the common acronym dictionary
                                full_form = acronyms_dict[acronym]
                                self.warnings.append(f"\nLine {self.line_acro} [Warning]: '{acronym}' s not properly expanded and not enclosed in parentheses at the first occurrence.\n\t\t\t\t\t It is a commom acronym Full form: {full_form}.Define if it doesn't matched with your defination.")
                            else:
                                self.warnings.append(f"\nLine {self.line_acro} [Warning]: Acronym '{acronym}' is not properly expanded and not enclosed in parentheses at the first occurrence.")
                    # For occurrences other than the first occurrence 
                    else:     
                        if full_form or enclosed_in_parentheses:
                           self.warnings.append(f"\nLine {self.line_acro} [Warning]: Acronym '{acronym}' should be expanded and enclosed in parentheses only at the first occurrence.") 
    
         
        # Post-loop: Check for multiple definitions or enclosures
        for (acronym, full_form), count in self.full_form_counts.items():
                if count > 1:
                    self.warnings.append(f"\nLine {self.line_acro} [Warning]: Acronym '{acronym}' has been defined with full form  multiple times.It should be expanded only at the first occurrence.")

        for acronym, count in self.parentheses_counts.items():
                if count > 1:
                    self.warnings.append(f"\nLine {self.line_acro} [Warning]: Acronym '{acronym}' is enclosed in parentheses multiple times. It should be enclosed only at the first occurrence.")
    
    def run(self):
        abstract = self.remove_latex_commands(self.extract_abstract())
        title = self.remove_latex_commands(self.extract_title())
        keywords = self.remove_latex_commands1(self.extract_keywords())
        output = []  # The output would be updated with the extracted title and abstract along with the word counts respectively.

        output.append('\n'+'='*50+"\n Title Related Comments \n"+'='*50)
        if title:          
            
            # Process the title by removing LaTeX commands           
            output.append(f"\n Title (Processed): \n{title}")

            # Count words in the processed title
            word_count = len(title.split())
            output.append(f"\n\n Number of words in the processed title: {word_count}")

        else:
            output.append(f"\n No title found.")
        
        output.append('\n'+'='*50+"\n Abstract Related Comments \n"+'='*50)
        
        if abstract:

            # Process the abstract by removing LaTeX commands
            output.append(f"\n Abstract (Processed): ")

            # Count words in the processed abstract
            word_count = self.count_words(abstract)
            output.append(f"\n\n Number of words in the abstract: {word_count}")
        
        else:
            output.append("\n No abstract found.")
                
        output.append('\n'+'='*50+"\n keywords Related Comments \n"+'='*50)
        
        if keywords:

            # Process the keywords by removing LaTeX commands
            output.append(f"\n keywords (Processed): \n{keywords}")

            # Count words in the processed abstract
            word_count = self.count_words(keywords)
            output.append(f"\n\n Number of words in the keywords: {word_count}")
            
         # New IEEE style checks
        keyword_list = [kw.strip() for kw in keywords.split(',') if kw.strip()]
        
        # Check if keywords are in alphabetical order
        if keyword_list != sorted(keyword_list, key=str.lower):
            self.warnings.append(f"\nLine {self.keyword_line:04d} [Warning] : IEEE Style Violation: Keywords are not in alphabetical order.")


        # Check if first keyword starts with a capital letter
            if not keyword_list[0][0].isupper():
                self.warnings.append(f"\nLine {self.keyword_line:04d} [warning] : IEEE Style Violation: The first keyword should begin with a capital letter.")

        else:
            output.append("\n No keywords found.")
                
        self.text = f"{abstract} {keywords}"
        
        self.extract_acronyms()

        if self.acronyms:
            self.count_acronyms_occurrences()
            self.verify_acronyms()
            #for error in self.error:
            #    output.append(f"\n {error}")
        
            acronym_data = {}
            for acronym, count in self.acro_count.items():
                full_form = self.acro_full.get(acronym, "Not Defined")
                acronym_data[acronym] = {"Occurrences": count, "Full Form": full_form}
           
            data = [[acronym, values["Occurrences"], values["Full Form"]] for acronym, values in acronym_data.items()]    
            # Generate table
            table = tabulate(data, headers=["Acronym", "Occurrences", "Full Form"], tablefmt="grid")
            output.append('\n' + '=' * 50 + "\n  List of Acronyms: \n" + '=' * 50) 
            output.append(f"\n {table}")

            if self.warnings:
                
                output.append('\n' + '=' * 50 + "\n Warnings  \n" + '=' * 50)
               
                for warning in self.warnings:
                    output.append(warning)
        else:
            output.append("\n No acronyms found in the given text.")
        return output