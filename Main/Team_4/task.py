import re
class team_4:
    
    def __init__(self, latex_code, text_begin):
        self.latex_code = latex_code
        self.text_begin = text_begin
    def find_units(self,latex_file_path):
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
            pattern = re.compile(r'\b{}\b'.format(unit), re.IGNORECASE)
            matches = pattern.findall(latex_file_path)
            for match in matches:
                number_part, _, unit_part = match.groups()
                if ' ' in number_part:
                    modified_unit_part = unit_part.replace(' ', '~')
                    modified_latex_content = modified_latex_content.replace(match.group(), f'{number_part}{modified_unit_part}', 1)
    def run(self):  # The function which is going to be invoked in the wrapper class should contain no arguments
        output = [] # The output list with the errors to be returned
        text = self.latex_code
        result=self.check_punctuation(text)     
        output = result     
        return output