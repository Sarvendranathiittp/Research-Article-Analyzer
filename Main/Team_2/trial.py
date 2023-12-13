def get_word_list(text):
    return text.split()

# Example usage with the provided abstract
input_text = "Research suggests that speech deterioration indicates an exacerbation in patients with chronic obstructive pulmonary disease (COPD). This study provides a comparison of read speech of 9 stable COPD patients and 5 healthy controls (1) and 9 stable COPD patients and 9 COPD patients in exacerbation (II). Results showed a significant effect of condition on the number of (non-linguistic) in- and exhalations per syllable (I, II) and the ratio of voiced and silence intervals (II). Also, sustained vowels by 10 COPD patients in exacerbation were compared with 10 vowels in stable condition (III). Results showed an effect of condition on duration, shimmer, harmonics- to-noise ratio (HNR) and voice breaks. It was concluded that HNR, vowel duration and the number of (non-linguistic) in- and exhalations per syllable show potential for remote monitoring. Further research is needed to examine the validity of the results for natural speech and larger sample sizes."

# Call the get_word_list function with the input text
word_list = get_word_list(input_text)

# Print the list of words
print("List of words:", word_list)

def count_words(text):
    words = text.split()
    return len(words)


word_count = count_words(input_text)
print(f"Number of words: {word_count}")
