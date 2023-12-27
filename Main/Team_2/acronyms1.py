# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import re

def process_input(abstract):
    acro_list = re.findall(r'\(([^)]+)\)', abstract)
    new_acro_list = [word[:-1] for word in abstract.split() if (
        word[:-1].isupper() and word[-1] == 's' and word[:-1].isalpha() and word[-1].islower()
    )]
    return acro_list, new_acro_list

def count_matching_words(abstract, acronym_list):
    word_count = {}
    word_first_occurrence = {}

    lines = abstract.split('\n')
    for line_number, line in enumerate(lines, start=1):
        words_in_line = re.findall(r'\b\w+\b', line)
        for word in words_in_line:
            if word in acronym_list:
                if word not in word_first_occurrence:
                    word_first_occurrence[word] = line_number

                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    return word_count, word_first_occurrence

def find_and_print_remaining_uppercase_words(abstract):
    pattern = r'\b[A-Z]+\b'
    uppercase_words = re.findall(pattern, abstract)

    if uppercase_words:
        print("\nAll acronyms:")
        print(uppercase_words)
    else:
        return None

    return uppercase_words

def check_and_print_occurrences(acro_list, new_acro_list, abstract):
    total_occurrences = 0
    matching_word_count, word_first_occurrence = count_matching_words(abstract, acro_list)

    for word in acro_list:
        occurrences = new_acro_list.count(word) + matching_word_count.get(word, 0)
        total_occurrences += occurrences
        if occurrences > 0:
            print(f"\n{word}: {occurrences} times \n(First occurrence in line {word_first_occurrence.get(word, 'N/A')})")

    print("\nTotal acronyms:", total_occurrences)



class team_2a:
    def __init__(self, abstract_content):
        self.abstract_content =abstract_content

    def run(self):
        abstract = self.abstract_content
       
        output = [] # The output would be updated with the extracted title and abstract along with the word counts respectively.
        
        acro_list, new_acro_list = process_input(abstract)
        
        if abstract:            

            #find_and_print_remaining_uppercase_words(abstract)

            #check_and_print_occurrences(acro_list, new_acro_list, abstract)
        

            
            output.append(f"\n Acronyms list: \n{acro_list}")
            output.append(f"\nPlural acronyms: \n{new_acro_list}")


            print(f"Acronyms are found,data is updated in LOGII file")

            
        
        else:
            output.append("\n No abstract found.")

            print("No abstract found.")
        
        
        return output