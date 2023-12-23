class team_8:
    # Constructor
    def __init__(self, latex_code, text_begin):
        self.latex_code = latex_code  # The entire LaTex code is in the form of string in the latex_code string
        self.text_begin = text_begin  # location of \begin

    def run(self):  # will be invoked by wrapper, shouldn't take arguments
        output = []
        text = self.latex_code
        # use self
        str_line = '=' * 50
        output.append(str_line + '\n\tSyntax related comments\n' + str_line + '\n')
        bibliography = self.extract_bibliography(text)
        self.syntax_check(bibliography, output)
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

    def extract_bibliography(self, text):
        bibliography_pattern = re.compile(r'\\begin{thebibliography}(.*?)\\end{thebibliography}', re.DOTALL)
        match = bibliography_pattern.search(text)

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
