import re

def extract_capital_words(input_string):
    result = []
    pattern = r'\(([^)]+)\)'

    matches = re.finditer(pattern, input_string)

    for match in matches:
        content_between_parentheses = match.group(1)
        
        if content_between_parentheses.isupper():
            words = content_between_parentheses.split()
            result.extend(words)

    return result

def count_matching_words(input_string, acronym_list):
    input_words = input_string.split()
    matching_words = [word for word in input_words if word in acronym_list]
    return len(matching_words)

# Example usage:
input_string = """Transmit antenna selection (TAS) is a technique that achieves better performance than a single\n"
    "antenna system while using the same number of radio frequency chains. We propose a novel TAS\n"
    "rule called the $\\lambda$-weighted interference indicator rule (LWIIR). We prove that for the general\n"
    "class of fading models with TED continuous cumulative distribution functions, LWIIR achieves the lowest\n"
    "average symbol error probability (SEP) among all TAS rules for an underlay cognitive radio system\n"
    "that employs binary power control and is subject to the interference-outage constraint."""

def count_matching_words(input_string, acronym_list):
    word_count = {}
    words_in_input = re.findall(r'\b\w+\b', input_string)

    for word in words_in_input:
        if word in acronym_list:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    return word_count

acronym_list = extract_capital_words(input_string)
matching_word_count = count_matching_words(input_string, acronym_list)

def find_and_print_remaining_uppercase_words(input_string):
    pattern = r'\b[A-Z]+\b'
    uppercase_words = re.findall(pattern, input_string)

    if uppercase_words:
        print()
    else:
        return None
    return uppercase_words
# Print the results
for word, count in matching_word_count.items():
    print(f"{word}: {count} times")
    e=input_string.split()
b=matching_word_count.items()
print(b)
b_list=list(b)
keys=[item[0] for item in b_list]
print(keys)
a=find_and_print_remaining_uppercase_words(input_string)
if(a==keys):
    print("no error")
else:
    diff=set(a)-set(keys)
    print(diff,"is not defined in starting")


