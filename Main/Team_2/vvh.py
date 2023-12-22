import re

def process_input(input_string):
    # Extract words between ( and ) into acro_list
    acro_list = re.findall(r'\(([^)]+)\)', input_string)

    # Check for words in input_string with specific conditions
    new_acro_list = [word[:-1] for word in input_string.split() if (
        word[:-1].isupper() and word[-1] == 's' and word[:-1].isalpha() and word[-1].islower()
    )]

    return acro_list, new_acro_list

# Example usage:

input_string = """Transmit antenna selection (TAS) is a technique that achieves better performance than a single\n"
    "antenna system while using the same number of radio frequency chains. We propose a novel TAS\n"
    "rule called the $\\lambda$-weighted interference indicator rule (LWIIR). We prove that for the general\n"
    "class of fading models with TED continuous cumulative distribution functions, LWIIR achieves TASs the lowest\n"
    "average symbol error probability (SEP) among all TAS rules for an underlay cognitive radio system\n"
    "that employs binary power control and is subject to the interference-outage constraint."""
acro_list, new_acro_list = process_input(input_string)

print("Acronyms list:")
print(acro_list)

print("\nPlural acronyms:")
print(new_acro_list)
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
matching_word_count = count_matching_words(input_string, acro_list)
def check_and_print_occurrences(acro_list, new_acro_list):
    occurrences_count = {}

    for acro_word in acro_list:
        count = new_acro_list.count(acro_word)
        if count > 0:
            occurrences_count[acro_word] = count

    if occurrences_count:
        print("\nOccurrences in new_acro_list:")
        for word, count in occurrences_count.items():
            print(f"{word}: {count} times")
    else:
        print("\nNo occurrences found in new_acro_list")

# Example usage:
check_and_print_occurrences(acro_list, new_acro_list)


# Print the results
for word, count in matching_word_count.items():
    print(f"{word}: {count} times")
e=input_string.split()

def find_and_print_remaining_uppercase_words(input_string):
    pattern = r'\b[A-Z]+\b'
    uppercase_words = re.findall(pattern, input_string)

    if uppercase_words:
        print()
    else:
        return None
    return uppercase_words

b=matching_word_count.items()
print(b)
b_list=list(b)
keys=[item[0] for item in b_list]
print(keys)
a=find_and_print_remaining_uppercase_words(input_string)
if(a==keys):
    print("All defined")
else:
    diff=set(a)-set(keys)
    print("not defined")
    print(diff)
