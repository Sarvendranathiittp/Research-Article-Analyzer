# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import re

class AcronymProcessor:

    def __init__(self, input_string):
        self.input_string = input_string
        self.acro_list, self.new_acro_list = self.process_input()
        self.matching_word_count = self.count_matching_words()

    def process_input(self):
        acro_list = []
        new_acro_list = []

        matches = re.finditer(r'\(([^)]+)\)', self.input_string)
        for match in matches:
            word = match.group(1)
            if word.isupper():
                acro_list.append(word)
            else:
                acro_list.append(word[:-1])

        new_acro_list.extend(word[:-1] for word in self.input_string.split() if (
            word[:-1].isupper() and (word[-1] == 's' or word[-1] == 'x') and word[:-1].isalpha() and word[-1].islower()
        ))

        return acro_list, new_acro_list

    def count_matching_words(self):
        word_count = {}
        words_in_input = re.findall(r'\b\w+\b', self.input_string)

        for word in words_in_input:
            if word in self.acro_list:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

        return word_count

    def find_and_print_remaining_uppercase_words(self):
        pattern = r'\b[A-Z]+\b'
        uppercase_words = re.findall(pattern, self.input_string)

        if uppercase_words:
            return uppercase_words
        else:
            return None

    def check_and_print_occurrences(self):
        total_occurrences = 0
        for word in self.acro_list:
            occurrences = self.new_acro_list.count(word) + self.matching_word_count.get(word, 0)
            total_occurrences += occurrences
            if occurrences > 0:
                print(f"\n{word}: {occurrences} times")

        print("\nTotal acronyms:", total_occurrences)

# Example usage:
input_string = """Transmit antenna selection (TASs) aalo Teacher Assistant(TA) is a technique that achieves better performance than a single\n"
    "antenna system while using the same number of radio frequency chains. We propose a novel TAS\n"
    "rule called the $\\lambda$-weighted interference (EDS) TAS indicator rule (LWIIRs). We prove that for the general\n"
    "class of fading models with TED continuous cumulative  EDD distribution functions, LWIIR achieves TASs the lowest\n"
    "average symbol error probability (SEPs) among all TAS rules for an underlay cognitive radio system\n" "TSA"
    "that employs binary power control and is subject to the interference-outage constraint."""

processor = AcronymProcessor(input_string)

print("Acronyms list:")
print(processor.acro_list)

print("\nPlural acronyms:")
print(processor.new_acro_list)

b = processor.matching_word_count.items()
#print(list(b))
keys = [item[0] for item in b]
#print(keys)

a = processor.find_and_print_remaining_uppercase_words()

if a == keys:
    print("All defined")
else:
    diff = set(a) - set(keys)
    print("\nNot defined:")
    print(diff)


# Split the input string into lines
lines = input_string.split('\n')

# Define a regular expression pattern to find words within parentheses
pattern = re.compile(r'\((\w+)\)')

# Iterate through each line and find matches
for i, line in enumerate(lines, start=1):
    matches = pattern.findall(line)
    for match in matches:
        print(f"\nWord  {match} occured in Line Number: {i}")



