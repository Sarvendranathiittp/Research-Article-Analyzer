from pylatex import Document, Section, Command, NoEscape

# Title and abstract content
title = "Transmit Antenna Selection for Interference-Outage Constrained Underlay CR"
abstract = (
    "Transmit antenna selection (TAS) is a technique that achieves better performance than a single\n"
    "antenna system while using the same number of radio frequency chains. We propose a novel TAS\n"
    "rule called the $\\lambda$-weighted interference indicator rule (LWIIR). We prove that for the general\n"
    "class of fading models with continuous cumulative distribution functions, LWIIR achieves the lowest\n"
    "average symbol error probability (SEP) among all TAS rules for an underlay cognitive radio system\n"
    "that employs binary power control and is subject to the interference-outage constraint."
)

# Create a PyLaTeX document
doc = Document()

# Add title and abstract to the document
with doc.create(Section(title, numbering=False)):
    doc.append(NoEscape(r'\begin{abstract}'))
    doc.append(abstract)
    doc.append(NoEscape(r'\end{abstract}'))

# Save the document to a .tex file
doc.generate_tex("output_jr")

# Compile the LaTeX document to generate the PDF
#doc.generate_pdf("output_document", clean_tex=True)
