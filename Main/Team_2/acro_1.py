import re

class Team2:
    def __init__(self, latex_content, begin_document_index):
        self.latex_content = latex_content
        self.begin_document_index = begin_document_index
        self.acronyms = []
        self.apostrophe_acronyms = []  # New attribute for apostrophe acronyms
        self.first_occurrence_line = {}
        self.warnings = []
        self.common_acronyms = ['DIY', 'NASA', 'HTML']

    def extract_abstract(self):
        begin_abstract_index = self.latex_content.find(r'\begin{abstract}', self.begin_document_index)
        end_abstract_index = self.latex_content.find(r'\end{abstract}', begin_abstract_index)

        if begin_abstract_index != -1 and end_abstract_index != -1:
            abstract_content = self.latex_content[begin_abstract_index + len(r'\begin{abstract}'):end_abstract_index].strip()
            return abstract_content
        else:
            return None

    def remove_latex_commands(self, text):
        text_without_commands = re.sub(r'\\[a-zA-Z]+', '', text)
        pattern = r'\{[\d.]+(cm|mm)?\}'
        cleaned_text = re.sub(pattern, '', text_without_commands)
        return cleaned_text

    def extract_apostrophe_acronyms(self):
        self.text = self.extract_abstract()
        apostrophe_acronyms = re.findall(r'\b[A-Z]+\'s\b', self.text)
        return apostrophe_acronyms

    def extract_acronyms(self):
        self.text = self.extract_abstract()
        capital_acronyms = re.findall(r'\b[A-Z]{2,}+\b', self.text)
        if len(self.text) > 2:
            s_suffix_acronyms = re.findall(r'\b[A-Z]{2,}+s\b', self.text)
            x_suffix_acronyms = re.findall(r'\b[A-Z]+x\b', self.text)
            

        self.acronyms = capital_acronyms + s_suffix_acronyms  + x_suffix_acronyms

    def verify_acronyms(self):
        lines = self.text.split('\n')

        for acronym in self.acronyms:
            first_occurrence_line = None
            defined_at_first_occurrence = False
            defined_without_parentheses = False
            is_common_acronym = acronym in self.common_acronyms

            for line_number, line in enumerate(lines, start=1):
                if re.search(fr'\b{re.escape(acronym)}\b', line):
                    first_occurrence_line = line_number

                    if '(' in line and ')' in line:
                        defined_at_first_occurrence = True

                    if not defined_at_first_occurrence and '(' not in line and ')' not in line:
                        defined_without_parentheses = True

                    break

            if first_occurrence_line is None and not is_common_acronym:
                self.warnings.append(f"Warning: Acronym '{acronym}' is not defined at all.")
            elif not defined_at_first_occurrence:
                if not is_common_acronym:
                    self.warnings.append(f"Warning: Acronym '{acronym}' is not defined.")
            elif defined_without_parentheses:
                if not is_common_acronym:
                    self.warnings.append(f"Warning: Acronym '{acronym}' is defined without parentheses at Line {first_occurrence_line}.")

            self.first_occurrence_line[acronym] = first_occurrence_line

    def run(self):
        abstract = self.remove_latex_commands(self.extract_abstract())
        output = []

        output.append('\n' + '=' * 50 + "\n\t\t Abstract Related Comments \n" + '=' * 50)

        self.text = abstract
        self.extract_acronyms()

        if self.acronyms:
            self.verify_acronyms()
            output.append("List of Acronyms: " + str(self.acronyms))

            if self.warnings:
                output.append("\nWarnings:")
                for warning in self.warnings:
                    output.append(warning)
        else:
            output.append("No acronyms found in the given text.")

        # Extract and print apostrophe acronyms separately
        self.apostrophe_acronyms = self.extract_apostrophe_acronyms()
        if self.apostrophe_acronyms:
            output.append("\nApostrophe Acronyms: " + str(self.apostrophe_acronyms))
        else:
            output.append("\nNo apostrophe acronyms found in the given text.")

        return output

# Example usage:
latex_content = r"""
\begin{document}
\title{Sample Document}
\begin{abstract}
This is a sample document with some acronyms such as DIY, NASA, and HTML.
We first propose a novel TAS rule called the $\lam$-weighted interference indicator
rule (LWIIR) for an interference-outage constrained underlay CR system. It selects
the antenna that minimizes a sum of AR's two terms. The first term is the instantaneous SEP
of a maximal ratio combining (MRC) receiver  and the second term is the indicator function
of the STx PRx channel power gain weighted by an interference-outage penalty factor $\lam$.
It differs from the rules proposed in the literature~\cite{Hanif_2015_globecom,Sarvendranath_2013_TCOM,
Sarvendranath_2014_TCOM,Wang_2011_TCom,Fakhan_2014_TSP}.As a result its analysis and performance
are also different.

\end{abstract}
\end{document}
"""

begin_document_index = 0
team_2_instance = Team2(latex_content, begin_document_index)
result = team_2_instance.run()

for item in result:
    print(item)
