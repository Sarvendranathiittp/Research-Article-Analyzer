import re

class AcronymProcessor:
    def _init_(self, abstract_content):
        self.abstract_content = abstract_content
        self.output = ""
        self.word_first_occurrence = {}  # Define word_first_occurrence as a class attribute

    def extract_acronyms(self):
        acronyms_with_parentheses = re.findall(r'\(([^)]+)\)', self.abstract_content)
        plural_acronyms = [word[:-1] for word in self.abstract_content.split() if (
            word[:-1].isupper() and word[-1] == 's' and word[:-1].isalpha() and word[-1].islower()
        )]
        return acronyms_with_parentheses, plural_acronyms

    def count_matching_words(self, acronyms):
        word_count = {}

        lines = self.abstract_content.split('\n')
        for line_number, line in enumerate(lines, start=1):
            words_in_line = re.findall(r'\b\w+\b', line)
            for word in words_in_line:
                if word in acronyms:
                    if word not in self.word_first_occurrence:
                        self.word_first_occurrence[word] = line_number

                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1

        return word_count

    def find_and_accumulate_remaining_acronyms(self, acronyms):
        pattern = r'\b[A-Z]+\b'
        remaining_acronyms = re.findall(pattern, self.abstract_content)

        if remaining_acronyms:
            self.output += "\nAll acronyms:\n" + str(remaining_acronyms)
        else:
            return None

        return remaining_acronyms

    def accumulate_occurrences(self, acronyms_with_parentheses, plural_acronyms):
        total_occurrences = 0
        matching_word_count = self.count_matching_words(acronyms_with_parentheses)

        for word in acronyms_with_parentheses:
            occurrences = plural_acronyms.count(word) + matching_word_count.get(word, 0)
            total_occurrences += occurrences
            if occurrences > 0:
                self.output += f"\n{word}: {occurrences} times \n(First occurrence in line {self.word_first_occurrence.get(word, 'N/A')})"

        self.output += "\nTotal acronyms: " + str(total_occurrences)

    def check_acronym_definitions(self, acronyms_with_parentheses, plural_acronyms):
        defined_acronyms = set()
    
        for acronym in acronyms_with_parentheses:
            first_occurrence_line = self.word_first_occurrence.get(acronym, None)
        
        # Check if the acronym is defined at all
            if first_occurrence_line is None:
                print(f"Warning: Acronym '{acronym}' is not defined at all")
                continue

        # Check if the acronym is defined at the first occurrence
            if first_occurrence_line != 0:
                print(f"Warning: Acronym '{acronym}' is defined at the first occurrence (Line {first_occurrence_line})")

        # Check if the acronym is enclosed in parentheses at its first occurrence
            first_occurrence_text = re.search(fr'\b{re.escape(acronym)}\b', self.abstract_content)
            if first_occurrence_text and not first_occurrence_text.group().startswith('('):
                print(f"Warning: Acronym '{acronym}' is not enclosed in parentheses at its first occurrence (Line {first_occurrence_line})")

        # Add the acronym to the set of defined acronyms
            defined_acronyms.add(acronym)

    # Check if the acronym is used later without a warning
        for acronym in plural_acronyms:
            if acronym in defined_acronyms:
                print(f"Warning: Acronym '{acronym}' is used without a warning in the later part of the content.")


    def run_analysis(self):
        acronyms_with_parentheses, plural_acronyms = self.extract_acronyms()

        if self.abstract_content:
            self.find_and_accumulate_remaining_acronyms(acronyms_with_parentheses)
            self.accumulate_occurrences(acronyms_with_parentheses, plural_acronyms)
            acronym_processor.check_acronym_definitions(acronyms_with_parentheses, plural_acronyms)

        else:
            self.output += "No abstract found."

        return self.output

# Example usage:
abstract_content_example = """
Transmit antenna selection (TAS) is a technique that achieves better performance than a single\n"
"antenna system while using the same number of radio frequency chains. We propose a novel TAS\n"
"rule called the $\\lambda$-weighted interference indicator rule (LWIIR). We prove that for the general\n"
"class of fading models with TED continuous cumulative distribution functions, LWIIR achieves the lowest\n"
"average symbol error probability (SEP) among all TAS rules for an underlay cognitive radio system\n"
"that employs binary power control and is subject to the interference-outage constraint.
"""

# Create an instance of AcronymProcessor
acronym_processor = AcronymProcessor(abstract_content_example)

# Run the analysis and print the result
result = acronym_processor.run_analysis()
print(result)