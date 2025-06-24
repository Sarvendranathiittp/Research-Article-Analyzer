import re

class team_4:
    """
    A comprehensive LaTeX style and formatting checker.

    This class performs a series of checks to ensure that LaTeX documents adhere to common academic style guidelines. The checks are categorized as follows:

    **Unit-Related Checks:**
    1.  **Spacing:** Ensures a non-breaking space (~) is used between a number and its unit (e.g., '50~Hz').
    2.  **Symbol Usage:** Verifies that standard unit symbols are used instead of full names when a quantity is present (e.g., '10 V' instead of '10 volts').

    **Mathematical Sequence and Formatting Checks:**
    1.  **Ellipsis Usage:**
        - Replaces literal '...' or '…' with the appropriate LaTeX command (`\ldots` or `\cdots`).
        - Ensures `\cdots` is used for operations (e.g., `a + \cdots + b`) and `\ldots` is used for sequences (e.g., `x_1, \ldots, x_n`).
        - Verifies that at least two terms precede an ellipsis command.
        - Checks for missing commas around `\ldots` in sequences.
    2.  **Multiplication:** Suggests using `\cdot` for multiplication between variables (e.g., `a \cdot b`).

    The script generates a categorized report of all issues found, with line numbers to help locate them in the source file.
    """
    
    def __init__(self, latex_code, text_begin):
        """
        Initializes the checker with LaTeX code.
        
        Args:
            latex_code (str): The string containing the LaTeX document.
            text_begin (int): The line number where the main text begins (e.g., at \\begin{document}).
        """
        # Store the LaTeX code and the starting line number of the main text.
        self.latex_code = latex_code
        self.text_begin = text_begin
        # Split the LaTeX code into a list of lines for easier processing.
        self.lines = self.latex_code.splitlines()
        
        # Define a list of standard scientific and technical units.
        # These are the symbols that the checker will look for.
        self.units = [
            'V', 'Ω', 'W', 'cm', 'mm', '°C', 'A', 'F', 'H', 'J', 'N', 'Pa', 'C', 'K',
            'mol', 'cd', 'rad', 'sr', 'lm', 'lx', 'Bq', 'Gy', 'Sv', 'kat', 'm', 's',
            'g', 'Hz', '%', 'Wb', 'T', 'S', 'rpm'
        ]
        # Create a mapping from common full-name spellings of units to their correct symbols.
        # This helps in identifying and correcting spelled-out units.
        self.unit_full_names = {
            'volts': 'V', 'volt': 'V', 'ohm': 'Ω', 'ohms': 'Ω', 'kph': 'km/h',
            'sec': 's', 'amps': 'A', 'sq.': '^2', 'cu.': '^3'
        }
        
        # Pre-compile regex patterns for efficiency
        math_environments = ['equation', 'align', 'gather', 'multline', 'flalign', 'alignat']
        self.begin_env_pattern = re.compile(fr'\\begin\{{({"|".join(math_environments)})\*?}}')
        self.end_env_pattern = re.compile(fr'\\end\{{({"|".join(math_environments)})\*?}}')
        self.inline_math_pattern = re.compile(r'\$.*?\$')
        self.display_math_pattern = re.compile(r'\\\[.*?\\\]')

        units_pattern = '|'.join(self.units)
        self.regex_no_space = re.compile(r"(\d+(?:\.\d+)?)(" + units_pattern + r")\b")
        self.regex_wrong_space = re.compile(r"(\d+(?:\.\d+)?)\s+(" + units_pattern + r")\b")

        full_names_pattern = '|'.join(re.escape(k) for k in self.unit_full_names.keys())
        self.regex_full_names = re.compile(r"(\d+(?:\.\d+)?)\s*(" + full_names_pattern + r")\b", re.IGNORECASE)

        self.any_ellipsis_pattern = re.compile(r'(\\ldots)|(\\cdots)|(\.\.\.)|(…)')
        op_pattern_str = r'[\+\-\*\/]'
        self.pre_op_pattern = re.compile(fr'\s({op_pattern_str})\s*$')
        self.post_op_pattern = re.compile(fr'^\s*({op_pattern_str})\s')
        
        self.cdot_regex = re.compile(r"([a-zA-Z]_\d+)\s+([a-zA-Z]_\d+)")
        

    def run(self):
        """
        Runs all checks on the LaTeX code and returns a formatted report.
        
        Returns:
            list: A list of strings forming a report of issues found.
        """
        unit_issues = []
        sequence_issues = []
        
        doc_start_line = 0
        for i, line in enumerate(self.lines):
            if r'\begin{document}' in line:
                doc_start_line = i
                break
        
        in_math_env = False
        for line_num, line_content in enumerate(self.lines[doc_start_line:], start=doc_start_line + 1):
            non_math_text, in_math_env = self._get_non_math_text(line_content, in_math_env)
            
            if non_math_text.strip():
                unit_issues.extend(self._check_spacing_and_units(non_math_text, line_num))
                unit_issues.extend(self._check_full_unit_names(non_math_text, line_num))

            sequence_issues.extend(self._check_ellipsis(line_content, line_num))
            sequence_issues.extend(self._check_cdot_in_sequences(line_content, line_num))

        report_lines = []
        
        # Units section
        report_lines.extend([
            "==================================================",
            "                Units Related Comments",
            "=================================================="
        ])
        
        if not unit_issues:
            report_lines.append("No unit-related issues found.")
        else:
            report_lines.extend(sorted(list(set(unit_issues))))
            
        # Sequence section
        report_lines.extend([
            "",
            "==================================================",
            "             Sequence Related Comments",
            "=================================================="
        ])

        if not sequence_issues:
            report_lines.append("No sequence-related issues found.")
        else:
            report_lines.extend(sorted(list(set(sequence_issues))))
            
        return [line + '\n' for line in report_lines]

    def _get_non_math_text(self, line, in_math_env):
        """
        Filters out LaTeX math environments from a line, handling multi-line environments.
        """
        if in_math_env:
            end_match = self.end_env_pattern.search(line)
            if end_match:
                line = line[end_match.end():]
                in_math_env = False
            else:
                return "", True

        processed_line = ""
        while True:
            begin_match = self.begin_env_pattern.search(line)
            if not begin_match:
                processed_line += line
                break
            
            processed_line += line[:begin_match.start()]
            
            end_match = self.end_env_pattern.search(line, begin_match.end())
            if end_match:
                line = line[end_match.end():]
            else:
                in_math_env = True
                line = ""
                break
        
        final_line = self.inline_math_pattern.sub(' ', processed_line)
        final_line = self.display_math_pattern.sub(' ', final_line)
        
        return final_line, in_math_env

    def _check_spacing_and_units(self, line, line_num):
        """
        Checks for missing or incorrect spacing before units.
        A non-breaking space is recommended between a quantity and its unit symbol in LaTeX
        to prevent them from being separated across lines. This function flags cases where
        there is no space or a regular space instead of a non-breaking one.
        For example, '50Hz' should be '50~Hz' and '50 Hz' should be '50~Hz'.
        """
        issues = []
        for match in self.regex_no_space.finditer(line):
            value, unit = match.groups()
            issues.append(f"Line {line_num}: [Spacing] Insert non-breaking space: {value}~{unit}.")

        for match in self.regex_wrong_space.finditer(line):
            if '~' not in match.group(0):
                value, unit = match.groups()
                issues.append(f"Line {line_num}: [Spacing] Insert non-breaking space: {value}~{unit}.")
        return issues

    def _check_full_unit_names(self, line, line_num):
        """
        Checks for spelled-out unit names used with quantities.
        When a unit is used with a quantity, its standard abbreviation should be used.
        For example, 'a 10 volt source' should be 'a 10~V source'. This function
        identifies and flags full unit names used with numbers.
        """
        issues = []
        for match in self.regex_full_names.finditer(line):
            value, unit_name = match.groups()
            correct_unit = self.unit_full_names.get(unit_name.lower(), unit_name)
            issues.append(f"Line {line_num}: [Symbol Use] Use correct unit symbol: {value}~{correct_unit}.")
        return issues

    def _check_ellipsis(self, line, line_num):
        """
        Checks for incorrect usage of ellipses based on revised rules.
        """
        issues = []
        for match in self.any_ellipsis_pattern.finditer(line):
            ellipsis_str = match.group(0)
            start_pos, end_pos = match.start(), match.end()
            
            pre_text = line[:start_pos].strip()
            post_text = line[end_pos:].strip()

            # Rule: Detect literal '...' or '…' and suggest replacement.
            if ellipsis_str in ['...', '…']:
                issues.append(f"Line {line_num}: [Ellipsis] Replace with LaTeX ellipsis: \\ldots.")
                continue

            # Determine if the ellipsis is used in an operational context (e.g., sums, products).
            is_operational = self.pre_op_pattern.search(line[:start_pos]) or \
                             self.post_op_pattern.search(line[end_pos:])

            # Rule: Flag incorrect ellipsis command for the context.
            # Suggests \cdots for operational use and \ldots for sequential use.
            if is_operational and ellipsis_str == r'\ldots':
                issues.append(f"Line {line_num}: [Math Formatting] Fix punctuation and command usage: Use \\cdots for operations.")
            
            if not is_operational and ellipsis_str == r'\cdots':
                issues.append(f"Line {line_num}: [Math Formatting] Fix punctuation and command usage: Use \\ldots for sequences.")

            # Rule: Ensure at least two terms precede an ellipsis.
            # This applies to both \ldots and \cdots.
            if ellipsis_str in [r'\ldots', r'\cdots']:
                elements = re.split(r'\s*,\s*|\s+', pre_text)
                elements = [e for e in elements if e and not e.endswith('(')]
                if len(elements) < 2:
                    if not pre_text.endswith('('):
                        issues.append(f"Line {line_num}: [Math Formatting] Fix punctuation and command usage: Use at least two terms before {ellipsis_str}.")

            # Rule: Check for missing commas around \ldots in sequences.
            # This ensures proper punctuation in lists like 'x_1, ..., x_n'.
            if ellipsis_str == r'\ldots' and not is_operational:
                if pre_text and post_text and pre_text[-1].isalnum() and post_text[0].isalnum():
                     if not (pre_text.endswith(',') or post_text.startswith(',')):
                        issues.append(f"Line {line_num}: [Math Formatting] Fix punctuation and command usage: Add commas around \\ldots.")

        return list(set(issues))

    def _check_cdot_in_sequences(self, line, line_num):
        """Checks for sequences that might require \\cdot."""
        issues = []
        for match in self.cdot_regex.finditer(line):
            var1, var2 = match.groups()
            issues.append(f"Line {line_num}: [Math Formatting] Fix punctuation and command usage: {var1} \\cdot {var2}.")
        return issues
