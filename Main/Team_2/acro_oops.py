import re
from collections import Counter

class Wrapper:
    def __init__(self, input_string):
        self.input_string = input_string
        self.acronym_list = []

    def extract_capital_words(self):
        pattern = r'\(([^)]+)\)'
        matches = re.finditer(pattern, self.input_string)

        for match in matches:
            content_between_parentheses = match.group(1)
            
            if content_between_parentheses.isupper():
                words = content_between_parentheses.split()
                self.acronym_list.extend(words)

    def count_matching_words(self):
        word_count = Counter(re.findall(r'\b\w+\b', self.input_string))

        matching_words = {word: count for word, count in word_count.items() if word in self.acronym_list}

        return matching_words

    def find_and_print_remaining_uppercase_words(self):
        pattern = r'\b[A-Z]+\b'
        uppercase_words = re.findall(pattern, self.input_string)

        if uppercase_words:
            
            for word in uppercase_words:
                return(word)
        else:
            return("\nNo remaining uppercase words.")

# Example usage:
input_string = """Transmit antenna selection (TAS) is a technique that achieves better performance than a single\n"
    "antenna system while using the same number of radio frequency chains. We propose a novel TAS\n"
    "rule called the $\\lambda$-weighted interference indicator rule (LWIIR). We prove that for the general\n"
    "class of fading models with TED continuous cumulative distribution functions, LWIIR achieves the lowest\n"
    "average symbol error probability (SEP) among all TAS rules for an underlay cognitive radio system\n"
    "that employs binary power control and is subject to the interference-outage constraint."""

# Create an instance of AcronymAnalyzer
analyzer = Wrapper(input_string)

# Extract acronyms, count matching words, and print remaining uppercase words
analyzer.extract_capital_words()
matching_word_count = analyzer.count_matching_words()
analyzer.find_and_print_remaining_uppercase_words()

# Print the results
print("\nMatching Acronyms and Their Counts:")
for word, count in matching_word_count.items():
    print(f"{word}: {count} times")
