import re
class team_4:
    
    def __init__(self, latex_code, text_begin):
        # Initialize the tema_4 class with latex code and text_begin attributes.
        self.latex_code = latex_code
        self.text_begin = text_begin
    def find_units(self,latex_file_path):
        """
        Method to find specific units within a Latex file.
        Parameters: 
            latex_file_path (str): The path to the latex file
        Returns:
            dict: A dictionary containing found units and keys and their occurences as values.
        """
        self.latex_file_path = latex_file_path
        units_to_find = ["ampere hour", "A·h", "A h", "Ah", "amp hr","bit", "byte", "cubic feet per minute", "CFM",
        "gallon", "gal", "gl", "GL", "gallon gas equivalent", "GGE",
        "litre", "liter", "l", "L", "li", "lit",
        "per", "/",
        "pounds per square inch", "lb/in2", "psi",
        "square", "symbol2", "sq",
        "tesla", "T",
        "ton", "tonne", "t", "T"]

        found_units = {}

        for unit in units_to_find:
            # Compile regax pattern to find the unit with word boundaries and case insensitivity
            pattern = re.compile(r'\b{}\b'.format(unit), re.IGNORECASE)
            # Find all matches of the unit in the Latex file content. 
            matches = pattern.findall(latex_file_path)
            # Iterate over each match
            for match in matches:
                # Group the match into number-part, _. unit_part
                number_part, _, unit_part = match.groups()
                # If there's a space in the number part, replace it with a non-breaking space in Latex
                if ' ' in number_part:
                    modified_unit_part = unit_part.replace(' ', '~')
                    # Replace the matched string with modified version in Latex content
                    modified_latex_content = modified_latex_content.replace(match.group(), f'{number_part}{modified_unit_part}', 1)
    def run(self):
        """"  
        The function which is going to be invoked in the wrapper class should contain no arguments
        Returns:
            list: A list containing errors to be returned.
        """
        output = [] # Initialize the output list
        text = self.latex_code
        result=self.check_punctuation(text)   # Call method to check puncuation  
        output = result   # Assign the result to output list  
        return output
