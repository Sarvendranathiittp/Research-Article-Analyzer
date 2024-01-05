"""Tasks given:
   1.To find syntax related errors in different references like journal,conference,textbook,etc
   2.To find acronym related errors
   3.To print a list of Electrical Engineering related acronyms used in bibliography
(more names can be added to the list electrical_engineering_acronyms[] to make it more exhaustive)
   4.To find and print number of times a each reference has been cited in the latex document
   5.To print the total number of references"""

import re
class team_8:
    # Constructor
    def __init__(self, latex_code, bbl_code,text_begin):
        self.latex_code = latex_code  # The entire LaTex code is in the form of string in the latex_code string
        self.text_begin = text_begin  # location of \begin
        self.bbl_code   = bbl_code    # The entire bibliography is in the form of string in the bbl_code string
    def run(self):  # will be invoked by wrapper, shouldn't take arguments
        output = []
        text = self.latex_code
         text2 = self.bbl_code
        # use self
        str_line = '=' * 50
        output.append(str_line + '\n\tSyntax related comments\n' + str_line + '\n')
        bibliography = self.extract_bibliography(text2)
        self.trans(bibliography, output)
        self.proc(bibliography, output)
        self.syntax_check(bibliography, output)
        output.append(str_line + '\n\tAcronym related comments\n' + str_line + '\n')
        self.check_acronym_casing(bibliography, output)
        self.check_acronym_format(bibliography, output)
        output.append(str_line + '\n\tElectrical Engineering related Acronyms\n' + str_line + '\n')
        electrical_engineering_acronyms = [
        "PLD", "VHDL", "ASIC", "RTL", "GUI",
        "GSM", "CDMA", "LTE", "RFID", "ZIF",
        "MTBF", "QFN", "PFC", "UPS", "NAND",
        "IIR", "FIR", "EMC", "ECL", "PCI",
        "LAN", "CAN", "LIN", "JTAG", "GPIO",
        "RTOS", "HDL", "HMI", "PID", "HDD",
        "VLSI", "OSI", "VGA", "PCB", "USB",
        "DDR", "IOT", "ZIF", "SMT", "EEPROM",
        "ADC", "DAC", "DCM", "PLL", "DDS",
        "GPS", "DVI", "PWM", "RISC", "CISC",
        "MIPS", "SPICE", "ROM", "RAM", "FPGA",
        "DSP", "ISP", "QAM", "SDRAM", "SCADA",
        "LVDT", "RTOS", "ARM", "SIMD", "LED",
        "IOT", "VCO", "DCS", "BOM", "MOSFET",
        "HBT", "ESD", "CMOS", "ASIC", "PAM",
        "CRC", "IEEE", "OEM", "PCBA", "ICP",
        "VLSI", "APD", "APM", "GFCI", "MOSFET",
        "LSI", "PCMCIA", "FET", "NOR", "XOR",
        "ADC", "VGA", "DIP", "LCD", "VCO",
        "PLL", "RFM", "JFET", "LTE-A", "SIMO",
        "MIMO", "QPSK", "IRIG", "CMRR", "NEC",
        "CCD", "DRAM", "OLED", "VCO", "SDLC",
        "SIMD", "SPI", "ISO", "EEPROM", "SOC",
        "NAND", "SCPI", "UART", "USB-C", "WDM"]
        self.print_unique_acronyms(bibliography, output,electrical_engineering_acronyms)
        output.append(str_line + '\n\tReference Citation related comments\n' + str_line + '\n')
        self.count_references(text, output)

        return output

    def count_references(self, text, output):
        # Extract all \cite commands
        cite_matches = re.findall(r'\\cite\{([^}]+)\}', text)

        # Flatten and split the citations
        all_citations = [cite.strip() for group in cite_matches for cite in group.split(',')]

        # Maintain the order of citations
        unique_citations = []
        citation_counts = {}
        for citation in all_citations:
            if citation not in citation_counts and citation not in unique_citations:
                unique_citations.append(citation)
            citation_counts[citation] = citation_counts.get(citation, 0) + 1

        # Display the results in the same order as in the LaTeX file
        for citation in unique_citations:
            count = citation_counts.get(citation, 0)
            output.append(f'Reference {citation} is cited {count} times.\n')

        # Calculate and display the total number of unique references
        total_unique_references = len(unique_citations)
        output.append(f'Total Unique References: {total_unique_references}\n')

    def extract_bibliography(self, text2):
        bibliography_pattern = re.compile(r'\\begin{thebibliography}(.*?)\\end{thebibliography}', re.DOTALL)
        match = bibliography_pattern.search(text2)

        if match:
            return match.group(1).strip()
        else:
            return None

    def syntax_check(self, bibliography, output):
        # Regular expression to match author names, volume, number, page range, and month formats
        author_pattern = re.compile(r'\\bibitem{[^}]+}\s*([^,]+(?:,\s*[^,]+)),\s["“”]([^"“”]+)["“”]')
        format_pattern = re.compile(
            r'\\bibitem{[^}]+}\s*.*?vol\.\s*~?\d+|no\.\s*~?\d+|pp\.\s*~?\d+--\d+|'
            r'(Jan\.|Feb\.|Mar\.|Apr\.|May|Jun\.|Jul\.|Aug\.|Sep\.|Oct\.|Nov\.|Dec\.)'
        )

        # Find all matches in the bibliography for author names
        author_matches = re.finditer(author_pattern, bibliography)

        for match in author_matches:
            authors = match.group(1).split(', ')

            # Check for missing commas between authors
            if len(authors) > 1 and ', and' not in match.group(0):
                output.append(f"In reference number {match.start(0) + 1}, comma is missing after the second last author's name\n")

            # Check for missing ~ in author names
            for author in authors:
                if ' ' not in author and '~' not in author:
                    output.append(f"In reference number {match.start(0) + 1}, ~ is missing in author's name {author}\n")

                # Check for author names not in short form
                if len(author.split()) > 2 and '.' not in author:
                    output.append(f"In reference number {match.start(0) + 1}, author's name {author} is not in short form (like A.~Goldsmith)\n")

                # Check for missing comma between initials
                initials = re.findall(r'\b\w', author)
                if len(initials) > 1 and ', and' not in match.group(0) and ',' not in author:
                    output.append(f"In reference number {match.start(0) + 1}, comma is missing between authors' names {author}\n")

                # Check for lowercase initials
                if any(initial.islower() for initial in initials):
                    output.append(f"In reference number {match.start(0) + 1}, in author's name {author} the initials should be in capitals\n")

            # Find all matches in the bibliography for volume, number, page range, and month formats
            format_matches = re.finditer(format_pattern, bibliography)

        for match in format_matches:
            match_text = match.group(0)

            # Check for volume format errors
            if re.search(r'vol\.\s*\d+', match_text):
                if 'vol. ' in match_text:
                    output.append(f"In reference, volume {match_text} is wrong because of missing ~\n")
                if 'volume ' in match_text:
                    output.append(f"In reference, volume {match_text} is wrong because volume should be in short form like vol.\n")

            # Check for number format errors
            if re.search(r'no\.\s*\d+', match_text):
                if 'number ' in match_text:
                    output.append(f"In reference, number {match_text} is wrong because number should be in short form like no.\n")

            # Check for page range format errors
            if re.search(r'pp\.\s*\d+--\d+', match_text):
                if 'pp. ' in match_text:
                    output.append(f"In reference, page number range {match_text} is wrong because it should be written in short form like pp.\n")
                if '--' not in match_text:
                    output.append(f"In reference, page number range {match_text} is wrong because of one extra missing hyphen\n")

            # Check for month format errors
            if re.search(r'(Jan\.|Feb\.|Mar\.|Apr\.|May|Jun\.|Jul\.|Aug\.|Sep\.|Oct\.|Nov\.|Dec\.)', match_text):
                if '.' not in match_text:
                    output.append(f"In reference, month {match_text} is wrong because fullstop is missing\n")
                if len(match_text) > 4:
                    output.append(f"In reference, month {match_text} is wrong because it should be written in short form like Jan., Feb., etc.\n")


    def check_acronym_casing(self, bibliography, output):
        # Extracting all occurrences of acronyms within curly braces excluding \bibitem{} and \emph{}
        references = re.findall(r'(?<=\\bibitem\{.*?\})(.*?)\}', bibliography, re.DOTALL)

       # Checking the casing of each acronym in each reference
        for i, reference in enumerate(references, start=1):
           acronyms = re.findall(r'(?<!\\emph\{)\{([A-Za-z]+)\}', reference)
           for j, acronym in enumerate(acronyms, start=1):
                if not acronym.isupper():
                    output.append(f"In reference number [{i}], acronym {acronym} is not in capitals\n")

    def check_acronym_format(self, bibliography, output):
        # Extracting all occurrences of potential acronyms with at least two uppercase letters and their reference numbers
        matches = re.finditer(r'(?<!\\bibitem\{.*?)(?<!\\emph\{)(?<!{)([A-Z]{2,})[^}]*\}', bibliography)

        # Checking the format of each potential acronym
        for match in matches:
            reference_number = bibliography.count('\\bibitem', 0, match.start()) + 1
            acronym = match.group(1)

        if f'{{{acronym}}}' not in match.group():
            if '{' not in acronym and '}' not in acronym:
                output.append(f"In reference number [{reference_number}], acronym {acronym} should be inside curly braces\n")
            elif '{' not in acronym:
                output.append(f"In reference number [{reference_number}], acronym {acronym} has a missing opening brace\n")
            elif '}' not in acronym:
                output.append(f"In reference number [{reference_number}], acronym {acronym} has a missing closing brace\n")
            else:
                pass

    def print_unique_acronyms(self,bibliography, output,electrical_engineering_acronyms):
         # Extracting all occurrences of acronyms within curly braces excluding \bibitem{} and \emph{}
        references = re.findall(r'(?<=\\bibitem\{.*?\})(.*?)\}', bibliography, re.DOTALL)

        # Extracting acronyms from the references and converting to uppercase
        all_acronyms = [acronym.upper() for reference in references for acronym in re.findall(r'(?<!\\emph\{)\{([A-Za-z]+)\}', reference)]

        # Keeping track of unique acronyms
        unique_acronyms = list(set(all_acronyms) & set(electrical_engineering_acronyms))
   
        # Printing unique acronyms within double quotes and separated by commas
        output.append("Unique acronyms:", ", ".join(f'"{acronym}"' for acronym in unique_acronyms))
        output.append('\n')

    def trans(self,bibliography, output):
        references = re.findall(r'\\bibitem{([^}]*)}\n\s*(.*?)\n', bibliography)

        for ref_key, ref_content in references:
            if '\\emph{Trans.' in ref_content:
                match = re.search(r'\\emph{Trans\.\s*\\(.*?)}\s*,\s*vol\.\s*~(\d+)\s*,\s*no\.\s*~(\d+)\s*,\s*pp\.\s*(\d+--\d+)\s*,\s*([A-Za-z]+\.\s*\d+)', ref_content)
            if match:
                journal_name, volume, number, page_numbers, date = match.groups()
                if not volume:
                    output.append(f"In reference number [{ref_key}], volume is missing\n")
                if not number:
                    output.append(f"In reference number [{ref_key}], number is missing\n")
                if not page_numbers:
                    output.append(f"In reference number [{ref_key}], page numbers are missing\n")
                if not date:
                    output.append(f"In reference number [{ref_key}], date is missing\n")


                if not volume or not number or not page_numbers or not date:
                    pass
                elif ref_content.find(f"vol.~{volume}, no.~{number}, pp. {page_numbers}, {date}") == -1:
                    output.append(f"In reference number [{ref_key}], volume, number, page numbers, and date should be written in the same order\n")
                else:
                     pass

    def proc(self,bibliography, output):
        references = re.findall(r'\\bibitem{([^}]*)}\n\s*(.*?)\n', bibliography)

        for ref_key, ref_content in references:
            if '\\emph{Proc.' in ref_content:
                match = re.search(r'\\emph{Proc\.\s*\\(.*?)}\s*,\s*([^,]*)\s*,\s*pp\.\s*(\d+--\d+)', ref_content)
            if match:
                conference_name, date, page_numbers = match.groups()
                if not date:
                    output.append(f"In reference number [{ref_key}], date is missing\n")
                if not page_numbers:
                    output.append(f"In reference number [{ref_key}], page numbers are missing\n")

