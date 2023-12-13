from pylatex import Document, Section, Subsection, Command, NoEscape

# Create a new document
doc = Document()

# Title and author
doc.preamble.append(Command('title', 'Speech Deterioration in COPD'))
doc.preamble.append(Command('author', 'Piyush Gupta'))
doc.preamble.append(Command('date', ''))  # Use an empty date to omit the date

# Begin the document
doc.append(NoEscape(r'\maketitle'))

# Abstract section
doc.append(Section('Abstract'))
doc.append("Research suggests that speech deterioration indicates an exacerbation in patients with chronic obstructive pulmonary disease (COPD). This study provides a comparison of read speech of 9 stable COPD patients and 5 healthy controls (I) and 9 stable COPD patients and 9 COPD patients in exacerbation (II). Results showed a significant effect of condition on the number of (non-linguistic) in- and exhalations per syllable (I, II) and the ratio of voiced and silence intervals (II). Also, sustained vowels by 10 COPD patients in exacerbation were compared with 10 vowels in stable condition (III). Results showed an effect of condition on duration, shimmer, harmonics-to-noise ratio (HNR), and voice breaks. It was concluded that HNR, vowel duration, and the number of (non-linguistic) in- and exhalations per syllable show potential for remote monitoring. Further research is needed to examine the validity of the results for natural speech and larger sample sizes.")

# Main sections with random content
doc.append(Section('Introduction'))
doc.append("This is the introduction section. Add your content here.")

doc.append(Section('Methodology'))
doc.append("Describe your methodology in this section.")

doc.append(Section('Results'))
doc.append("Present your results in this section.")

doc.append(Section('Conclusion'))
doc.append("Summarize your findings and conclude the study.")

# Save the document to a file
doc.generate_tex('output_document')

# Compile the generated LaTeX document (you may need to install a LaTeX distribution)
#doc.generate_pdf('output_document', clean_tex=True)
