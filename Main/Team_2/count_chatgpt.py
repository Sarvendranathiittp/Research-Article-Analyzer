def count_characters_except_spaces(input_string):
    count = 0
    inside_word = False

    for char in input_string:
        if char != ' ':
            count += 1
            inside_word = True
        elif inside_word:
            inside_word = False

    return count

# Example usage:
input_string = r""" \documentclass{article}%
\usepackage[T1]{fontenc}%
\usepackage[utf8]{inputenc}%
\usepackage{lmodern}%
\usepackage{textcomp}%
\usepackage{lastpage}%
%
\title{Speech Deterioration in COPD}%
\author{Piyush Gupta}%
\date{}%
%
"""
result = count_characters_except_spaces(input_string)
print(f"Number of characters except spaces: {result}")
