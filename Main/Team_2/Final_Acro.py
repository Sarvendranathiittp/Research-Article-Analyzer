import re

class AcronymProcessor:

    #exclude_path = r'C:\Users\rashm\Downloads\lab1\lab1\Research-Article-Analyzer\Main\Team_2\list.csv'

    def __init__(self, input_string):
        self.input_string = input_string
        # self.exclude_acronyms = self.read_exclude_file()
        self.acro_list, self.new_acro_list = self.process_input()
        self.matching_word_count = self.count_matching_words()

    exclude_acronyms = "ANM APL ARSH ASHA BCC BPL  BPMU  CH CHC DC DPMU FP FRU GoI HMIS HPD  HR  HRD  IEC JSSK  JSY  M&E MAS MCD MH MU MOHFW NHM NGO  NLEP NPCC"

    def process_input(self):
        acro_list = []
        new_acro_list = []

        matches = re.finditer(r'\(([^)]+)\)', self.input_string)
        for match in matches:
            word = match.group(1)

            if word.isupper() and word not in self.exclude_acronyms:
                acro_list.append(word)
            else:
                acro_list.append(word[:-1])

        new_acro_list.extend(word[:-1] for word in self.input_string.split() if (
                word[:-1].isupper() and (word[-1] == 's' or word[-1] == 'x') and word[:-1].isalpha() and word[
            -1].islower()
                and word[:-1] not in self.exclude_acronyms
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
        print("\n")
        print("DEFINED Acronyms:", total_occurrences)


# Read input string from file
file_path = r'C:\Users\rashm\Downloads\lab1\lab1\Research-Article-Analyzer\Main\Team_2\latex_example.txt'
with open(file_path, 'r') as file:
    input_string = file.read()

# Example usage:
processor = AcronymProcessor(input_string)
print("Defined Acronyms list:")
print(processor.acro_list)

print("\nPlural acronyms:")
print(processor.new_acro_list)
print("====================================")
b = processor.matching_word_count.items()
keys = [item[0] for item in b]
a = processor.find_and_print_remaining_uppercase_words()
if a == keys:
    print("All defined")
else:
    diff = set(a) - set(keys)
    print("\nNot defined or standard abbreviations:")
    print(diff)
    print("=========================================")

processor.count_matching_words()
processor.check_and_print_occurrences()

lines = input_string.split('\n')
pattern = re.compile(r'\((\w+)\)')
print("===============================================")
print("\nOccurrences of acronyms:")
for i, line in enumerate(lines, start=1):
    matches = pattern.findall(line)

    for match in matches:
        print(f"\nWord  {match} occurred in Line Number: {i}")
tches = re.findall(r'\([^)]*\)', input_string)
print("=================================================")
print("\nPrinting Full forms of defined acronyms:")
# Process each match
for match in tches:
    # Count the number of uppercase letters in the word
    num_uppercase = sum(1 for char in match if char.isupper())

    # Find the position of the word in the input string
    match_position = input_string.find(match)

    # Find the substring before the word
    substring_before_word = input_string[:match_position]

    # Find the n words before the word (excluding '(')
    words_before = re.findall(r'\b\w+\b', substring_before_word)[-num_uppercase-1:]

    # Print the result
    print(f"Word {match}")
    print(f"Full form is: {' '.join(words_before)}\n")
