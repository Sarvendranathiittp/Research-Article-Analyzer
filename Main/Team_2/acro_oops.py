# merge methods for line 36 and 10
#Make list of full form of acronyms , acronym and occurance
#make warnings for acro. that are  1) not defined entirely  2) defined but not at first occurrence
#cronym must be followed by parentheses for the first time
#NOTE : If the acronym is not repeated the whole body then no need to add parentheses.
'''Brief of TO DO LIST

1) Output in form of Name of acr -Acro -Occurrence 
     # This includes plural and singular both 

Comments Type 
2) If apostrophe is present ,then " Check whether this is for possessive form or mistaken by user for plural "
    # eliminate the confusion between the actual symbol of ’ and the mistaken symbol  ' 
3)If acronym has been defined but not at the first occurrence then " Acronym is defined on line ___ but not on the first occurrence ,i.e. line___ " otherwise "Acronyms is not defined ,Define it on the line ____ ,i.e. the first occurrence 
  # Also check whether if its a common acronym mentioned in a list we have created ,then don't give the warning if its not defined anywhere but     I    if its defined then it should be at first occurrence
'''

import re

class AcronymProcessor:
    def __init__(self, abstract_content):
        self.abstract_content = abstract_content
        self.output = ""

    def extract_acronyms(self):
        acronyms_with_parentheses = re.findall(r'\(([^)]+)\)', self.abstract_content)
        plural_acronyms = [word[:-1] for word in self.abstract_content.split() if (
            word[:-1].isupper() and word[-1] == 's' and word[:-1].isalpha() and word[-1].islower()
        )]
        return acronyms_with_parentheses, plural_acronyms

    def count_matching_words(self, acronyms):
        word_count = {}
        word_first_occurrence = {}

        lines = self.abstract_content.split('\n')
        for line_number, line in enumerate(lines, start=1):
            words_in_line = re.findall(r'\b\w+\b', line)
            for word in words_in_line:
                if word in acronyms:
                    if word not in word_first_occurrence:
                        word_first_occurrence[word] = line_number

                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1

        return word_count, word_first_occurrence

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
        matching_word_count, word_first_occurrence = self.count_matching_words(acronyms_with_parentheses)

        for word in acronyms_with_parentheses:
            occurrences = plural_acronyms.count(word) + matching_word_count.get(word, 0)
            total_occurrences += occurrences
            if occurrences > 0:
                self.output += f"\n{word}: {occurrences} times \n(First occurrence in line {word_first_occurrence.get(word, 'N/A')})"

        self.output += "\nTotal acronyms: " + str(total_occurrences)

    def run_analysis(self):
        acronyms_with_parentheses, plural_acronyms = self.extract_acronyms()

        if self.abstract_content:
            self.find_and_accumulate_remaining_acronyms(acronyms_with_parentheses)
            self.accumulate_occurrences(acronyms_with_parentheses, plural_acronyms)
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
