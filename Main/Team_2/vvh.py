# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
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

        print("Total acronyms:", total_occurrences)

# Example usage:
input_string = """Transmit antenna selection (TASs) aalo Teacher Assistant(TA) is a technique that achieves better performance than a single\n"
    "antenna system while using the same number of radio frequency chains. We propose a novel TAS\n"
    "rule called the $\\lambda$-weighted interference indicator rule (LWIIRs). We prove that for the general\n"
    "class of fading models with TED continuous cumulative  EDD distribution functions, LWIIR achieves TASs the lowest\n"
    "average symbol error probability (SEPs) among all TAS rules for an underlay cognitive radio system\n" "TSA"
    "that employs binary power control and is subject to the interference-outage constraint(IOC)."""


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
processor.count_matching_words()
processor.check_and_print_occurrences()

lines = input_string.split('\n')
pattern = re.compile(r'\((\w+)\)')
for i, line in enumerate(lines, start=1):
    matches = pattern.findall(line)
    for match in matches:
        print(f"\nWord  {match} occured in Line Number: {i}")
tches = re.findall(r'\([^)]*\)', input_string)

# Process each match
for match in tches:
    # Count the number of uppercase letters in the word
    num_uppercase = sum(1 for char in match if char.isupper())
    
    # Find the position of the word in the input string
    match_position = input_string.find(match)
    
    # Find the substring before the word
    substring_before_word = input_string[:match_position]
    
    # Find the n words before the word (excluding '(')
    words_before = re.findall(r'\b\w+\b', substring_before_word)[-num_uppercase:]
    
    # Print the result
    print(f"Word {match}")
    print(f"Full form is: {' '.join(words_before)}\n")

