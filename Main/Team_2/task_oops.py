import re

def remove_latex_commands(text):
    # Function to remove LaTeX commands
    text_withoutcommands = re.sub(r'\\[a-zA-Z]+', '', text)
    pattern = r'\{[\d.]+(cm|mm)?\}'
    cleaned_text = re.sub(pattern, '', text_withoutcommands)
    return cleaned_text

class Wrapper:
    def __init__(self, latex_content, begin_document_index):
        self.latex_content = latex_content
        self.begin_document_index = begin_document_index
        self.title = None
        self.abstract = None
        self.title_word_count = 0
        self.abstract_word_count = 0
        self.output = []

    def extract_abstract(self):
        begin_abstract_index = self.latex_content.find(r'\begin{abstract}', self.begin_document_index)
        end_abstract_index = self.latex_content.find(r'\end{abstract}', begin_abstract_index)
        if begin_abstract_index != -1 and end_abstract_index != -1:
            self.abstract = self.latex_content[begin_abstract_index + len(r'\begin{abstract}'):end_abstract_index].strip()
        else:
            self.abstract = None

    def extract_title(self, title_command=r'\title', opening_brace='{', closing_brace='}'):
        begin_title_index = self.latex_content.find(title_command, self.begin_document_index)
        opening_brace_index = self.latex_content.find(opening_brace, begin_title_index)
        depth = 0
        current_index = opening_brace_index

        while current_index < len(self.latex_content):
            current_char = self.latex_content[current_index]

            if current_char == opening_brace:
                depth += 1
            elif current_char == closing_brace:
                depth -= 1

            if depth == 0 and current_char == closing_brace:
                self.title = self.latex_content[opening_brace_index + 1:current_index].strip()
                break

            current_index += 1

    def count_words(self, text):
        words = text.split()
        return len(words)

    def extract_acronyms(self, text):
        potential_acronyms = re.findall(r'\b[A-Z]+\b', text)
        acronyms = [acronym for acronym in potential_acronyms if len(acronym) > 1]
        return acronyms

    def process_document(self):
        self.extract_abstract()
        self.extract_title()

        self.output.append(f"\n ================================================\n Title Related Comments \n ================================================ ")

        if self.title:
            processed_title = remove_latex_commands(self.title)
            self.output.append(f"\n Title (Processed): \n{processed_title}")
            self.title_word_count = self.count_words(processed_title)
            self.output.append(f"\n Number of words in the processed title: {self.title_word_count}")
        else:
            self.output.append(f"\n No title found.")

        self.output.append(f"\n ================================================\n Related Comments \n ================================================ ")
        processed_abstract = remove_latex_commands(self.abstract)
        if self.abstract:
            
            self.output.append(f"\n Abstract (Processed): \n{processed_abstract}")
            self.abstract_word_count = self.count_words(processed_abstract)
            self.output.append(f"\n Number of words in the abstract: {self.abstract_word_count}")
        else:
            self.output.append("\n No abstract found.")

        # Extract acronyms from the processed title and abstract
        title_acronyms = self.extract_acronyms(processed_title)
        abstract_acronyms = self.extract_acronyms(processed_abstract)

        self.output.append(f"\n Acronyms in the title: {title_acronyms}")
        self.output.append(f"\n Acronyms in the abstract: {abstract_acronyms}")

        return self.output

# Example usage:
# Corrected LaTeX content without unnecessary characters and with proper line breaks
latex_content_example = """
\\title{Sample Title}
\\begin{document}
\\begin{abstract}
example
\\end{abstract}

\\selectlanguage{english}

\\renewcommand{\\abstractname}{}

\\begin{abstract}
    \\fontsize{10}{12}\\selectfont
    \\textbf{Abstract:} Our journal has a biannual basis and is dedicated to the engineering area, mainly to the disciplines of electrical, electronics, telecommunications, and systems engineering, so the target audience for the magazine is interested in such areas. We publish scientific research papers or problem reflections in a specific topic, review articles, papers, reviews, discussions, and translations, within this thematic framework. We use the IFAC standards for publications.

    \\vspace{3mm}

    \\textbf{Keywords:} Publishing rules, procedures, publication, IFAC format.
    \\vspace{-7mm}
\\end{abstract}

\\selectlanguage{spanish}

\\renewcommand{\\abstractname}{}

\\begin{abstract}
    \\fontsize{10}{12}\\selectfont
    \\textbf{Resumen:} Nuestra revista tiene una periodicidad semestral y está dedicada al área de las Ingenierías, principalmente a las disciplinas de Ingenierías Eléctrica, Electrónica, Telecomunicaciones y Sistemas; por tanto, el público objetivo de la revista es aquel interesado en tales áreas. Se publicarán artículos de investigación científica o de reflexión sobre un problema o tópico de un área, artículos de revisión, ponencias, reseñas, discusiones y traducciones, dentro de este marco temático. Utilizamos las normas IFAC para publicaciones.

    \\vspace{3mm}

    \\textbf{Palabras Clave:} Normativa de publicación, procedimientos, publicación, formato IFAC.
\\end{abstract}
\\end{document}
"""

begin_document_index_example = 0

# Create an instance of the Wrapper class
team_2_processor = Wrapper(latex_content_example, begin_document_index_example)

# Process the document and print the output
result_output = team_2_processor.process_document()
for output_line in result_output:
    print(output_line)

