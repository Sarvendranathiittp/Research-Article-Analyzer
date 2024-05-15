# Research-Article-Analyzer

A collaborative project under [**Dr. Sarvendranath Rimalpudi**](https://sarvendranath.in/) to analyze and detect common errors in a Research Article written in _LaTeX_. 

## Table of Contents

- [Implementation](#implementation)
  - [Tasks](#tasks)
- [Snapshots](#snapshots)
- [Contributors](#contributors)

## Implementation

### Tasks

#### Team 1: G Jaswanth CS22B020 Nishchith G CS22B021
Analyze: Titles, authors,

Refer to guidelines in Writing Principles page 4

II. Writing Principles—4

A. Writing Parts of an Article

a. Title
b. Byline and Membership Citation

\title{Transmit Antenna Selection for Interference-Outage Constrained Underlay CR}
\author{Rimalapudi Sarvendranath, {\it Student Member, IEEE}, Neelesh B. Mehta, {\it
Senior Member, IEEE}

Chong Zhang , Student Member, IEEE, Min Dong , Senior Member, IEEE, and Ben Liang ,
Fellow, IEEE

Or

Yuanwei Liu, Jiaqi Xu, Zhaolin Wang, Xidong Mu, Jianhua Zhang, and Ping Zhang

Or

Min Dong , Senior Member, IEEE, and Qiqi Wang
A comma is missing after the first author name

#### Team 2: Rashmitha CS22B050 Tanvi Gupta CE22B035 Piyush Gupta EE22B056

1. Count the number of words in the title and abstract.
2. Create a list of acronyms used.
3. Count the number of times each acronym occurred.
4. Identify the acronyms that are not expanded at the first occurrence.
   
Abstract and main text should be treated separately

Acronym defined in abstract should be defined again

Define acronyms the first time they appear in the Abstract as well as the first time they appear in the body of the
article, written out first as part of the sentence, followed by the acronym in parentheses.

Coined plurals or plurals of acronyms do not take the apostrophe as per Chicago Manual of Style.
Example: FET (singular); FETs (plural).

Indefinite articles are assigned to abbreviations to fit the sound of the first letter: an FCC regulation; a BRI.
Refer to IV. APPENDIX A. Some Common Acronyms and Abbreviations in page III. Grammar and
Usage in Transactions—24

#### Team 3: Shivadharshan S CS22B057 Akilesh P CS22B040 Anirudhan S EE22B061

Analyze index terms: Similar to a sentence only first word should be capitalized

\begin{IEEEkeywords}
Cognitive radio, underlay, antenna selection, interference outage constraint, SEP,
imperfect CSI.
\end{IEEEkeywords}

a. Standard names and capitalizations

i. Create a list of scientist's names used in research articles

a. Gaussian, Doppler,

Index Terms

All articles must contain Index Terms. These are keywords provided by the authors. Index Terms appear in
alphabetical order, and as a final paragraph of the Abstract section. Capitalize the first word of the Index Terms
list; lowercase the rest unless capitalized in text.
Example:
Index Terms—Abstraction, computer-aided system engineering (CASE), conceptual schema, data model, entity type hierarchy, ISO
reference model, layered architecture meta model, reverse engineering.

#### Team 5: T Mokshith Reddy CS22B046 M Susank EE22B025 G Suryanarayana Murthy EE22B017

Equations analyzer:
Punctuation of equations: Identify different construct used to write equations
1. Every equation should end with a punctuation.
a. Comma or full-stop
b. Check for comma if next letter is small letter
c. Check for full stop if next letter is Capital
2. Multiple equations using allign
a. Comma for all intermediate the equations
b. Last equation will have full stop if a new sentence starts after it
3. One equation in multiple lines using Multline
a. Math operator should be in the new line
Refer to other cases in IEEE-Math-Typesetting-Guide-for-LaTeX-Users.pdf

#### Team 6: Yuvraj ee22b054 Arin mehta ee22b002

Title case for the subsections and subsubsections

\subsection{Antenna Selection Options and Data Transmission}
\subsubsection{Interference-Outage Probability}

All nouns, pronouns, adjectives, verbs, adverbs, and subordinating conjunctions (If, Because, That, Which)
should be capitalized.

Capitalize abbreviations that are otherwise lowercase (i.e., use DC, not dc or Dc) except for unit abbreviations
and acronyms.

Articles (a, an, the), coordinating conjunctions (and, but, for, or, nor), and most short prepositions are
lowercase unless they are the first or last word.

Prepositions of more than three letters (Before, From, Through, With, Versus, Among, Under, Between,
Without) are capitalized.

#### Team 7 : A Aswin EE22B055 Chakrala Sai Madhav CS22B060 Deepak EE22B011

Refer to section on Math in page II. Writing Principles—21

1) Always add a zero before decimals, but do not add after
a. 0.25 and not .25
b. 0.5 and not 0.50
c. Start with text and then move to inside equations.
2) Do not start a sentence with a numeral.
a. 20 apples [Avoid writing 20 at the beginning of the sentence]
b. Twenty apples [This is preferred]
3) Inline math equations/expressions check for other inline math modes
a. Fractions may be broken down (shilled) multiline (built-up) so they can be placed on one line.
Sometimes parentheses may need to be added to distinguish between expressions, especially
when a minus appears
4) Conditions: In displayed equations, a comma or parentheses and a two-em space is inserted between the main expression and
the condition following it.

#### Team 8: Girban Mandal EE22B016 Sarvagna Sripathi EE22B046

Bibtex: separate file filename.bbl
Inside main file itself

Task: Bibliography: Read References section in page number 11 from the style guide pdf

Process the text between \begin{thebibliography} and \end{thebibliography}

Check for the punctuation mistakes in each bib item

d. Task 1: Crate list of references and how many times cited

Journal

 \bibitem{Zhao_2008_TSP}
 
 Q.~Zhao, S.~Geirhofer, L.~Tong, and B.~M. Sadler, ``Opportunistic spectrum
 access via periodic channel sensing,'' \emph{IEEE Trans.\ Signal Process.},
 vol.~56, no.~2, pp. 785--796, Feb. 2008.
Conference
 \bibitem{RZhang_2008_DSAN}
 R.~Zhang and Y.~C. Liang, ``Exploiting hidden power-feedback loops for
 cognitive radio,'' in \emph{Proc.\ DySPAN}, Oct. 2008, pp. 1--5.
 
Textbook

i. Format, Authors: captals and full stops

ii. Vol. ??,

iii. no. ??,

iv. pp. ??

v. month (Should be in short form with dot), Ex: Jan. Feb. Apr. May

vi. year.

vii. Missing acronym capitalization in bibliography and punctuation

List of standard acronyms should be in capitals and inside {}. Ex. {MIMO} and not
MIMO

Create a list of technical acronyms typically used in Electrical engineering

Count the number of times a reference is cited 

## Snapshots

## Executable

## Contributors

[![](https://contrib.rocks/image?repo=Sarvendranathiittp/Research-Article-Analyzer)](https://github.com/Sarvendranathiittp/Research-Article-Analyzer/graphs/contributors)

Feel free to contribute and enhance the learning experience!
