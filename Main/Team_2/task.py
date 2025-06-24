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
        self.main_start_line_number=0
        self.acronyms = []
        self.acro_count={}
        self.acro_full={}
        self.warnings = []
        self.abstract_acro_data = {}
        self.maintext_acro_data = {}
        self.issued_warnings = set()

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
    def extract_main_text(self):
        doc_start = self.latex_content.find(r'\begin{document}')
        if doc_start == -1:
            return ''

        # Skip title and citations (optional)
        title_start = self.latex_content.find(r'\title{', doc_start)
        if title_start != -1:
            title_end = self.latex_content.find('}', title_start)
            doc_start = title_end + 1 if title_end != -1 else doc_start

        cite_start = self.latex_content.find(r'\cite{', doc_start)
        if cite_start != -1:
            cite_end = self.latex_content.find('}', cite_start)
            doc_start = cite_end + 1 if cite_end != -1 else doc_start

        abstract_end = self.latex_content.find(r'\end{abstract}', doc_start)
        keywords_end = self.latex_content.find(r'\end{IEEEkeywords}', doc_start)

        content_start = (
            keywords_end + len(r'\end{IEEEkeywords}') if keywords_end != -1 else
            abstract_end + len(r'\end{abstract}') if abstract_end != -1 else
            doc_start
        )

        # Find the end of the main text
        bib_starts = [
            self.latex_content.find(r'\begin{thebibliography}', content_start),
            self.latex_content.find(r'\bibliography', content_start),
            self.latex_content.find(r'\bibliographystyle', content_start),
            self.latex_content.find(r'\end{document}', content_start)
        ]
        content_end = min([i for i in bib_starts if i != -1], default=len(self.latex_content))

        all_lines = self.latex_content.split('\n')

        # Find starting line number of main text
        cumulative_chars = 0
        self.main_start_line_number = 0
        for i, line in enumerate(all_lines):
            cumulative_chars += len(line) + 1
            if cumulative_chars >= content_start:
                self.main_start_line_number = i + 1
                break

        # Use original lines starting from that point
        main_text_lines = all_lines[self.main_start_line_number - 1:]
        self.main_text_with_lines = []
        cleaned_lines = []

        for idx, raw_line in enumerate(main_text_lines):
            line_number = self.main_start_line_number + idx

            # Stop processing if we reach end of main content
            if content_end != len(self.latex_content):
                cumulative_chars += len(raw_line) + 1
                if cumulative_chars >= content_end:
                    break

            # Remove LaTeX comments
            comment_index = raw_line.find('%')
            if comment_index != -1 and (comment_index == 0 or raw_line[comment_index - 1] != '\\'):
                raw_line = raw_line[:comment_index]

            cleaned = self.remove_latex_commands2(raw_line)
            if cleaned.strip():
                self.main_text_with_lines.append((line_number, cleaned))
                cleaned_lines.append(cleaned)

        return '\n'.join(cleaned_lines)
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
            #print(self.keyword_line)
        
        return cleaned_text
    def remove_latex_commands2(self, text):

        # Remove LaTeX math environments
        text = re.sub(r'\$.*?\$', '', text)
        text = re.sub(r'\\begin\{.*?\}.*?\\end\{.*?\}', '', text, flags=re.DOTALL)

        # Remove inline LaTeX commands
        text = re.sub(r'\\[a-zA-Z]+\*?(?:\[[^\]]*\])?(?:\{[^}]*\})?', '', text)

        # Remove {1cm}, {2.5mm}, etc.
        text = re.sub(r'\{[\d.]+(cm|mm|in)?\}', '', text)

        # Remove leftover braces and trim
        text = re.sub(r'[{}]', '', text)

        return text.strip()


    
    

    def count_words(self, text):
        # Split the text into words and return the count
        words = text.split()
        return len(words)
   
    def extract_acronyms(self):
        # Extract acronyms with all capital letters (e.g., TASD)
        capital_acronyms = re.findall(r'(?!\bX\b)[A-Z]{2,}', self.text)
        
        # Extract acronyms ending with 's' (e.g., LEDs)
        s_suffix_acronyms = re.findall(r"\b[A-Z]{2,}s\b", self.text)

        # Extract acronyms with an apostrophe and 's' (e.g., TA's)
        apostrophe_acronyms = re.findall(r"\b[A-Z]{2,}'s\b", self.text)

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
        
        num_uppercase = sum(1 for char in acronym if char.isupper())

        # Find the first occurrence of the acronym
        position = self.work.find(acronym)
        if position == -1:
            return False

        # Extract a limited window of text before the acronym
        context_window = self.work[max(0, position - 300):position]
        
        # Get the last 'num_uppercase' words before the acronym
        words_before = re.findall(r'\b\w+\b', context_window)[-num_uppercase:]

        if len(words_before) != num_uppercase:
            return False

        # Match initial letters with acronym letters
        initials = ''.join(word[0].upper() for word in words_before)

        if initials.upper() == acronym.upper():
            self.acro_full[acronym] = ' '.join(words_before)
            return True
        else:
            return False
        
        
    def normalize_acronym(self, acronym):
        """Normalize acronyms by removing possessive or plural suffixes."""
        if acronym.endswith("'s"):
            return acronym[:-2]
        elif acronym.endswith("s") and not acronym.endswith("ss"):
            return acronym[:-1]
        return acronym

    
    def verify_acronyms(self):
        self.full_form_counts = {}
        self.parentheses_counts = {}
        self.acronym_line_map = {}
        self.acronym_first_flags = {}

        abstract = self.remove_latex_commands(self.extract_abstract())
        keywords = self.remove_latex_commands1(self.extract_keywords())

        for acronym in self.acro_count:
            self.work = self.text
            normalized = self.normalize_acronym(acronym)

            # Step 1: Map acronym line numbers
            if acronym in abstract:
                self.acronym_line_map[acronym] = self.line_number
            elif acronym in keywords:
                self.acronym_line_map[acronym] = self.keyword_line
            else:
                for line_number, line in self.main_text_with_lines:
                    if acronym in line:
                        self.acronym_line_map[acronym] = line_number
                        break
                else:
                    self.acronym_line_map[acronym] = -1

            # Step 2: Check full form and parentheses
            self.work = self.text

            enclosed = self.check_enclosed_in_parentheses(normalized)
            expanded = self.acro_defined(normalized)

            line_number = self.acronym_line_map.get(acronym, '?')

            # If normalized acronym has a full form, link it to the original
            if expanded:
                self.acro_full[acronym] = self.acro_full.get(normalized)

            self.acronym_first_flags[acronym] = {
                "full_form": expanded,
                "enclosed": enclosed,
                "line": line_number
            }

            # Step 3: Issue warnings (but only if not already issued)
            key_base = (acronym,)
        
            if key_base in self.issued_warnings:
                continue

            if expanded and not enclosed:
                key = (acronym, "expanded_no_parens")
                if key not in self.issued_warnings:
                    self.warnings.append(
                        f"\nLine {line_number:04d} [Warning]: Acronym '{acronym}' is expanded but not enclosed in parentheses at first occurrence."
                    )
                    self.issued_warnings.add(key)

            elif not expanded and enclosed:
                key = (acronym, "enclosed_no_expand")
                if key not in self.issued_warnings:
                    self.warnings.append(
                        f"\nLine {line_number:04d} [Warning]: Acronym '{acronym}' is enclosed in parentheses but not properly expanded at first occurrence."
                    )
                    self.issued_warnings.add(key)

            elif not expanded and not enclosed:
                key = (acronym, "no_expand_no_enclose")
                if key not in self.issued_warnings:
                    self.warnings.append(
                        f"\nLine {line_number:04d} [Warning]: Acronym '{acronym}' is not properly expanded and not enclosed in parentheses at the first occurrence."
                    )
                    self.issued_warnings.add(key)

    def check_repeated_full_forms_from_acronyms(self):
        issued_full_form_warnings = set()
        full_text = (
            self.remove_latex_commands(self.extract_abstract()) + "\n" +
            self.remove_latex_commands1(self.extract_keywords()) + "\n" +
            "\n".join([line for _, line in self.main_text_with_lines])
        ).lower()

        for acronym, full_form in self.acro_full.items():
            if not full_form:
                continue

            normalized_full_form = ' '.join(full_form.lower().split())
            count = full_text.count(normalized_full_form)

            if count > 1:
                line_numbers = [
                    f"{line_number:04d}"
                    for line_number, line in self.main_text_with_lines
                    if normalized_full_form in line.lower()
                ]

                lines_str = ", ".join(line_numbers) if line_numbers else "?"
                first_line = line_numbers[0] if line_numbers else "????"

                key = (acronym, normalized_full_form)
                if key not in issued_full_form_warnings:
                    self.warnings.append(
                        f"\nLine {first_line} [Warning]: Full form '{full_form}' (for acronym '{acronym}') is expanded {count} times at lines: {lines_str}."
                    )
                    issued_full_form_warnings.add(key)

                    
    def check_multiple_parentheses(self):
        checked = set()

        # Make a list to store all (line_number, line) from abstract + keywords + main text
        full_text_lines = []

        # Add abstract lines with their line numbers
        abstract_lines = self.extract_abstract().splitlines()
        for i, line in enumerate(abstract_lines, start=self.line_number):
            full_text_lines.append((i, line))

        # Add keyword lines with their line numbers
        keyword_lines = self.extract_keywords().splitlines()
        for i, line in enumerate(keyword_lines, start=self.keyword_line):
            full_text_lines.append((i, line))

        # Add main text lines
        full_text_lines.extend(self.main_text_with_lines)

        # Now check each acronym
        for acronym in set(self.acronyms):
            if acronym in checked:
                continue

            pattern = rf'\({re.escape(acronym)}\)'
            count = len(re.findall(pattern, self.text))

            if count > 1:
                # Now collect all lines where acronym is found in parentheses
                line_numbers = [
                    f"{line_number:04d}"
                    for line_number, line in full_text_lines
                    if re.search(pattern, line)
                ]
                lines_str = ", ".join(line_numbers) if line_numbers else "?"
                first_line = line_numbers[0] if line_numbers else "????"

                self.warnings.append(
                    f"\nLine {first_line} [Warning]: Acronym '{acronym}' is enclosed in parentheses {count} times at lines: {lines_str}."
                )

            checked.add(acronym)




    def run(self):
        abstract = self.remove_latex_commands(self.extract_abstract())
        title = self.remove_latex_commands(self.extract_title())
        keywords = self.remove_latex_commands1(self.extract_keywords())
        main_text_raw = self.extract_main_text()
        main_text = self.remove_latex_commands2(main_text_raw)
        
        output = []  # The output would be updated with the extracted title and abstract along with the word counts respectively.
       
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


            # Count words in the processed abstract
            word_count = self.count_words(abstract)
            output.append(f"\n\n Number of words in the abstract: {word_count}")
        
        else:
            output.append("\n No abstract found.")
                
        output.append('\n' + '=' * 50 + "\n Keywords Related Comments \n" + '=' * 50)

        # Extract and clean keywords
        keyword_list = [kw.strip() for kw in keywords.split(',') if kw.strip()]
        self.remove_latex_commands1(self.extract_keywords())
        self.line_acro = self.keyword_line

        # Check if keywords are in alphabetical order
        if keyword_list != sorted(keyword_list, key=str.lower):
            self.warnings.append(f"\nLine {self.keyword_line:04d} [Warning] : IEEE Style Violation: Keywords are not in alphabetical order.")

        # Check if last keyword ends with a full stop
        if keyword_list:
            last_keyword = keyword_list[-1].strip()
            if not last_keyword.endswith('.'):
                self.warnings.append(f"\nLine {self.keyword_line:04d} [Warning] : IEEE Style Violation: Last keyword '{last_keyword}' should end with a full stop.")

            # Check if first keyword starts with a capital letter
            if not keyword_list[0][0].isupper():
                self.warnings.append(f"\nLine {self.keyword_line:04d} [Warning] : IEEE Style Violation: The first keyword should begin with a capital letter.")

            # Check remaining keywords for lowercase
            for i, keyword in enumerate(keyword_list[1:], start=2):  # start=2 for second keyword
                words = keyword.split()

                for word in words:
                    # Skip if word is an acronym (all caps and more than 1 character)
                    if word.isupper() and len(word) > 1:
                        continue
                    # Skip if word is all lowercase
                    elif word.islower():
                        continue
                    else:
                        # Capitalized non-acronym word found → generate warning
                        self.warnings.append(
                            f"\nLine {self.keyword_line:04d} [Warning] : IEEE Style Violation: In Keyword {i} ('{keyword}'), the word '{word}' should be entirely lowercase.Only the first keyword is capitalized."
                        )
                        break  # Only one warning per keyword

        if keywords:

            # Process the keywords by removing LaTeX commands
            output.append(f" \n{keywords}")

            # Count words in the processed abstract
            word_count = self.count_words(keywords)
            output.append(f"\n\n Number of keywords: {len(keyword_list)}")
            
        
        else:
            output.append("\n No keywords found.")
            
        keyword_style_warnings = []
         # Collect keyword style warnings
        for warning in self.warnings:
            if "keyword" in warning.lower():
                keyword_style_warnings.append(warning)
        if keyword_style_warnings:
            output.append("\n--- Warnings ---")
            output.extend(keyword_style_warnings)
        else:
            output.append("\nNo keyword style issues found.")   
       
                       
        
        
        self.text = f"{abstract} {keywords}"

        self.acro_count.clear()
        self.acro_full.clear()
        self.acronyms.clear()

        self.extract_acronyms()
    

        if self.acronyms:
            self.count_acronyms_occurrences()
            self.verify_acronyms()
            #self.check_repeated_full_forms_from_acronyms()

            # Store abstract+keywords data
         # Step 4: Build abstract acronym data
            for acronym, count in self.acro_count.items():
                normalized = self.normalize_acronym(acronym)
                
                # Prefer exact acronym full form if available, else fallback to normalized
                full_form = self.acro_full.get(acronym)
                if not full_form:
                    full_form = self.acro_full.get(normalized)

                self.abstract_acro_data[acronym] = {
                    "Occurrences": count,
                    "Full Form": full_form if full_form else "Not Defined"
                }

        # Step 5: Print table only once
        if self.abstract_acro_data:
            data = [[acronym, details["Occurrences"], details["Full Form"]] for acronym, details in self.abstract_acro_data.items()]
            table = tabulate(data, headers=["Acronym", "Occurrences", "Full Form"], tablefmt="grid")
            output.append("\n" + "=" * 50 + "\n  Acronyms in the Abstract \n" + "=" * 50)
            output.append(f"\n{table}")
        else:
            output.append("\n No acronyms found in abstract and keywords.")
            
        self.text = ""
        self.text = main_text

        self.acro_count.clear()
        self.acro_full.clear()
        self.acronyms.clear()
        self.maintext_acro_data = {} 

        self.extract_acronyms()
    


        if self.acronyms:
            self.count_acronyms_occurrences()
            self.verify_acronyms()
            self.check_repeated_full_forms_from_acronyms()
            

            # Store main text acronym data
           
        for acronym, count in self.acro_count.items():
                normalized = self.normalize_acronym(acronym)
                
                # Prefer exact match first
                full_form = self.acro_full.get(acronym)
                if not full_form:
                    full_form = self.acro_full.get(normalized)

                self.maintext_acro_data[acronym] = {
                    "Occurrences": count,
                    "Full Form": full_form if full_form else "Not Defined"
                }

        # Step 6: Generate table only once
        if self.maintext_acro_data:
            main_data = [[acro, info["Occurrences"], info["Full Form"]] for acro, info in self.maintext_acro_data.items()]
            main_table = tabulate(main_data, headers=["Acronym", "Occurrences", "Full Form"], tablefmt="grid")
            output.append('\n' + '=' * 50 + "\n Acronyms in Main Text \n" + '=' * 50)
            output.append(f"\n{main_table}")
        else:
            output.append("\n No acronyms found in the main text.")
        self.text=""
        self.text = f"{abstract} {keywords} {main_text}"
        self.check_multiple_parentheses()

        # Categorize warnings
       # keyword_style_warnings = []
        acronym_warnings = []

        for warning in self.warnings:
            if "Keyword" in warning or "keyword" in warning:
                pass
            else:
                acronym_warnings.append(warning)

        # === Keywords Section ===
        #output.append('\n' + '=' * 50 + "\n Keywords Related Comments \n" + '=' * 50)

        #if keyword_style_warnings:
            #output.append("\n--- Keyword Style Warnings ---")
            #output.extend(keyword_style_warnings)
        #else:
            #output.append("\nNo keyword style issues found.")

        # === All Acronym Warnings Section ===
        if acronym_warnings:
            output.append('\n' + '=' * 50 + "\n Acronym Warnings \n" + '=' * 50)
            output.extend(acronym_warnings)
        else:
            output.append("\nNo acronym issues found in the given text.")

        return output