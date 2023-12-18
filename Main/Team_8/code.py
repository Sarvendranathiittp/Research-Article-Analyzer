import re

class team_8:
    # Constructor
    def _init_(self, latex_code, text_begin):
        self.latex_code = latex_code  # The entire LaTex code is in the form of string in the latex_code string
        self.text_begin = text_begin  # location of \begin

    def run(self):  # will be invoked by wrapper, shouldn't take arguments
        output = []
        text = self.latex_code
        # use self
        str_line = '=' * 50
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