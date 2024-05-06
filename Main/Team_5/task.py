import re
class team_5:
    
    def __init__(self, latex_code, text_begin):
        self.latex_code = latex_code
        self.text_begin = text_begin
    
    
    # def find_line_number_for_equation(self, latex_code, equation):
    #    lines = latex_code.split('\n')
    #    equation_lines = equation.split('\n')
    #    print(equation)
    #    print(equation_lines)
    #    for i, line in enumerate(lines, start=1):
    #     # Check if the first line of the equation is present in the current line
    #     if equation_lines[0] in line:
    #         # Check if all lines of the equation are in continuous order
    #         print(equation_lines[0])
    #         continuous_order = all(equation_lines[j] in lines[i + j] for j in range(len(equation_lines)))
            
    #         if continuous_order:
    #             return i

    #     return None
   
    def find_line_number_for_equation(self, latex_code, equation):
        # Remove spaces and empty lines from the LaTeX code
        #    lines = [line.strip() for line in latex_code.split('\n') if line.strip()]
       lines = [line for line in latex_code.split('\n')]

       # Remove spaces and empty lines from the equation
       equation_lines = [line for line in equation.split('\n') if line.strip()]

       for i, line in enumerate(lines, start=1):
        # Check if the first line of the equation is present in the current line
        
        if equation_lines and equation_lines[0] in line:
            # Check if all lines of the equation are in continuous order
            continuous_order = all(equation_lines[j] == lines[i-1+ j] for j in range(len(equation_lines)))
            # if not continuous_order:
            #     print(f"Lines not matching at line {i}:")
            #     for j in range(len(equation_lines)):
            #         if equation_lines[j] != lines[i - 1 + j]:
            #             print(f"Expected: {equation_lines[j]}")
            #             print(f"Actual  : {lines[i - 1 + j]}")
            # print(continuous_order)
            # print(line)
            # print('&')
            # print(lines[i-1])
            # print('$')
            # print(equation_lines[0])
            # print(equation_lines)
            # print('%')
            # for j in range(len(equation_lines)):
            #     print(equation_lines[j]) 
            #     print('@')
            #     print(lines[i-1+j])
            if continuous_order:
                return i

       return None
        
    def skip_line_by_first_word(self,text, first_word_to_skip):
        # Split the text into lines
        lines = text.split('\n')
        
        # Find and filter out the line with the specified first word
        filtered_lines = [line for line in lines if line.split() and line.split()[0] != first_word_to_skip]
        
        # Join the remaining lines back into a single string
        result = '\n'.join(filtered_lines)
        
        return result

    def check_punctuation_between_multiequations(self,latex_content):
        self.latex_content=latex_content
        result = []
        punc = False
        char_next = False
        equation_pattern = re.compile(r'\\begin{align}(.*?)\\end{align}',re.DOTALL)
        equations = re.findall(equation_pattern, latex_content)
        for equation in equations:
            if(equation.strip().split()[0].startswith('%')):
                continue
            for i in range(0,len(equation) - 1):
                if equation[i]=='\\' and equation[i+1]=='\\':
                    
                    for j in range(i - 1, -1, -1):
                        if equation[j] != ' ':  # If the character is not a space
                            if equation[j]==',':
                                punc = True
                                # print("1")
                                # print(equation)
                            break
                    
                    for k in range(i+2,i+10):
                        # print(equation[j])
                        if equation[k] not in [' ', '\n']:
                            if equation[k]=="\\":  
                                char_next = True
                                # print(equation[k])
                            if punc==True and equation[k]=="&":
                                char_next = True
                            break
                # if char_next and punc:
                #     print("yes")
                #     print(equation)
                if punc and (not char_next):
                    # print("hi")
                    # print(equation)
                    line_no = self.find_line_number_for_equation(latex_content,equation)
                    if(line_no==None):
                            continue
                    # result.append("here , is placed at the end of one of the equation, but it is not expexted there. The equation is  "+equation+"\n")
                    result.append(f"Warning: Unexpected punction (',') is seen at the end of an equation whose line no is: {line_no}\n")
                if char_next and (not punc):
                    # print("bye")
                    line_no = self.find_line_number_for_equation(latex_content,equation)
                    if(line_no==None):
                            continue
                    # print(equation)
                    # print(char_next)
                    # print(equation[len(equation)-2])
                    result.append(f"Warning: punction (',') is missing at the end of an equation whose line no is: {line_no}\n")
                char_next=False
                punc=False   
        return result;  
    def check_punctuations_for_array(self,latex_content):
        self.latex_content=latex_content
        result = []
        punc = False
        char_next = False
        equation_pattern = re.compile(r'\\begin{array}{ll}(.*?)\\end{array}',re.DOTALL)
        equations = re.findall(equation_pattern, latex_content)
        for equation in equations:
            if(equation.strip().split()[0].startswith('%')):
                continue
            # nnn=self.find_line_number_for_equation(latex_content,equation)
            # print("***********************")
            # print(nnn)
            # print("@@@@@@@@@@@@@@@@@@@@@@@@")
            for i in range(0,len(equation) - 1):
                if equation[i]=='\\' and equation[i+1]=='\\':
                    
                    for j in range(i - 1, -1, -1):
                        if equation[j] != ' ':  # If the character is not a space
                            if equation[j]==',':
                                punc = True
                                # print("1")
                                # print(equation)
                            break
                    
                    for k in range(i+2,i+10):
                        # print(equation[j])
                        if equation[k] not in [' ', '\n']:
                            if equation[k]=="\\":  
                                char_next = True
                                # print(equation[k])
                            if punc==True and equation[k]=="&":
                                char_next = True
                            break
                # if char_next and punc:
                #     print("yes")
                #     print(equation)
                if punc and (not char_next):
                    # print("hi")
                    # print(equation)
                    line_no = self.find_line_number_for_equation(latex_content,equation)
                    if(line_no==None):
                            continue                    
                    result.append(f"Warning: Unexpected punction (',') is seen at the end of an equation whose line no is: {line_no}\n")
                if char_next and (not punc):
                    # print("bye")
                    # print(equation)
                    line_no = self.find_line_number_for_equation(latex_content,equation)
                    if(line_no==None):
                            continue           
                    print(char_next)  
                    print(equation[len(equation)-1])       
                    result.append(f"Warning: punction (',') is missing at the end of an equation whose line no is: {line_no}\n")
                char_next=False
                punc=False   
        return result; 
                                 
    def check_punctuation(self,latex_content):
        self.latex_content = latex_content
            # Define a regular expression to match LaTeX equations and labels
        equation_pattern = re.compile(r'\\begin{equation}(.*?)\\end{equation}', re.DOTALL)
        result=[]
        # Find all equations in the LaTeX file
        equations = re.findall(equation_pattern, latex_content)
    
        for equation in equations:
            if(equation.strip().split()[0].startswith('%')):
                continue
            # ng = self.find_line_number_for_equation(latex_content,equation)
            # print("!!!!!!!!!!!!!!!!!!!!!!!!")
            # print(ng)
            # print("^^^^^^^^^^^^^^^^^^^^^^^^")
            # Extract the equation label if present
            label_match = re.search(r'\\label{([^}]*)}', equation)
            equation_pattern1 = re.compile(r'\\begin{array}(.*?)\\end{array}', re.DOTALL)
            equations1 = re.findall(equation_pattern1, equation)
            
            if equations1 != []:
                equation1 = equations1[0]
                last_char = equation1.strip()[-1] if equation1.strip() else None
            else: 
                last_char = equation.strip()[-1] if equation.strip() else None
            if last_char =="." or last_char ==",":
                index1 = latex_content.find(equation)
            else: 
                if label_match:
                    label = label_match.group(1)
                    # Check for punctuation before the label
                    index = equation.find('\\label{' + label + '}')
                    if index > 0:
                        preceding_text = equation[:index]
                    index1 = latex_content.find(equation)
                    # Check if there is a comma or period at the end of the preceding text
                    last_char = preceding_text.strip()[-1] if preceding_text.strip() else None

            if last_char in [',', '.']:
                # print(f"Punctuation ({last_char}) found before label '{label}' in equation (if any):\n{equation}")
    
                # Find the index of \end{equation} after the current equation
                end_equation_index = latex_content.find('\\end{equation}', index1)
                if end_equation_index != -1:
                    # Extract the text immediately after \end{equation}
                    text_after_end = latex_content[end_equation_index + len('\\end{equation}'):].lstrip()
    
                    # Find the first word after \end{equation}
                    # match = re.search(r'\w+', text_after_end)
                    match = re.search(r'\S+', text_after_end)
                    word_after_end = match.group()
                    
                    # print(word_after_end)
                    # print('@@@@')
                    # print(equation)
                    # print(word_after_end)
                    
                    
                    # if word_after_end == '%':
                    #     end_index = match.end()  # Get the end index of the matched substring
                    #     remaining_text = text_after_end[end_index:].strip()  # Get the text after the matched substring, removing leading/trailing whitespaces

                    #     # Check if the next line starts with '%'
                    #     if remaining_text.startswith('%'):
                    #         # If it does, take the first word after '%'
                    #         word_after_end = remaining_text.split()[0]
                    #     else:
                    #         # If not, take the first word of the next line
                    #         word_after_end = remaining_text.split('\n')[0].strip()

                    #     a = 1
                    #     while word_after_end == '%':
                    #         # Handle the case where '%' is followed by another '%'
                    #         word_after_end = remaining_text.split()[a]
                    #         a += 1
                    if word_after_end[0] == '%' or word_after_end == "%" :
                        end_index = match.end()  # Get the end index of the matched substring    
                        word_after_end = text_after_end[end_index:].split()[0]  # Get the next word after the matched substring
                        end_index_dupe=end_index
                        next_line_start_index = text_after_end.find('\n', end_index_dupe)
                        word_after_end=text_after_end[next_line_start_index:].split()[0]
                        text_after_end=text_after_end[next_line_start_index:]
                        while(word_after_end[0]=='%' or word_after_end==" "):
                        
                           next_line_start_index = text_after_end.find('\n', end_index_dupe)
                           end_index_dupe=next_line_start_index
                           word_after_end=text_after_end[next_line_start_index:].split()[0]
                           text_after_end=text_after_end[next_line_start_index:]

                        # print(word_after_end)
                        # print(equation)
                        if word_after_end==r"{\em":
                            index2 =  text_after_end.index(word_after_end)
                            start_index_next_word = index2 + len(word_after_end) + 1
                            word_after_end = text_after_end[start_index_next_word]
                            # print(word_after_end)
                            
                        if word_after_end[0:11]=="\\subsection":
                           next_line_start_index = text_after_end.find('\n', end_index_dupe)
                           end_index_dupe=next_line_start_index
                           word_after_end=text_after_end[next_line_start_index:].split()[0]
                           text_after_end=text_after_end[next_line_start_index:]                           
                           
                        if word_after_end[0:8]=="\\section":
                           next_line_start_index = text_after_end.find('\n', end_index_dupe)
                           end_index_dupe=next_line_start_index
                           word_after_end=text_after_end[next_line_start_index:].split()[0]
                           text_after_end=text_after_end[next_line_start_index:]
                        #    print(word_after_end)
                           
                        if word_after_end[0:6]=="\\label":
                           next_line_start_index = text_after_end.find('\n', end_index_dupe)
                           end_index_dupe=next_line_start_index
                           word_after_end=text_after_end[next_line_start_index:].split()[0]
                           text_after_end=text_after_end[next_line_start_index:]       
                        #    print(word_after_end)                    
                           
                        
                        if last_char=='.' and word_after_end[0]== '(':
                            pass
                        elif word_after_end[0].isalnum() and word_after_end[0].isupper():
                            if last_char != '.':
                                line_no = self.find_line_number_for_equation(latex_content,equation)
                                if(line_no==None):
                                          continue                                
                                # print("The word after \\end{equation} starts with a capital letter, but the punctuation is not a full stop.")
                                # result.append("The word after \\end{equation} starts with a capital letter, but the punctuation is not a full stop."+equation+"next word is:"+word_after_end+"\n"+"\n")
                                result.append(f"Error: ',' is seen instead of '.'  at the end of equation whose line no is {line_no}\n")
                        else:
                            if last_char != ',':
                                line_no = self.find_line_number_for_equation(latex_content,equation)
                                if(line_no==None):
                                    continue
                                # print("The word after \\end{equation} does not start with a capital letter, but the punctuation is not a comma.")
                                # print(word_after_end)
                                # print(equation)
                                result.append(f"Error: '.' is seen instead of ',' of at the end of equation whose line no is {line_no}\n")
                    
                    elif word_after_end:
                        # word_after_end = match.group()
                        # print(word_after_end)
                        if r"\sub" in word_after_end:
                            # print("hi")
                            nextt=self.skip_line_by_first_word(text_after_end,word_after_end)
                            # print("\\\\\\\\\\\\\\\\\\\its done//////////////////"+nextt[0])
                            word_after_end = nextt
                            
                        if word_after_end==r"{\em":
                            index2 =  text_after_end.index(word_after_end)
                            start_index_next_word = index2 + len(word_after_end) + 1
                            word_after_end = text_after_end[start_index_next_word]
                        
                        if word_after_end[0:11]=="\\subsection":
                           next_line_start_index = text_after_end.find('\n', end_index_dupe)
                           end_index_dupe=next_line_start_index
                           word_after_end=text_after_end[next_line_start_index:].split()[0]
                           text_after_end=text_after_end[next_line_start_index:]                           
                           
                        if word_after_end[0:8]=="\\section":
                           next_line_start_index = text_after_end.find('\n', end_index_dupe)
                           end_index_dupe=next_line_start_index
                           word_after_end=text_after_end[next_line_start_index:].split()[0]
                           text_after_end=text_after_end[next_line_start_index:]
                        #    print(word_after_end)
                           
                        if word_after_end[0:6]=="\\label":
                           next_line_start_index = text_after_end.find('\n', end_index_dupe)
                           end_index_dupe=next_line_start_index
                           word_after_end=text_after_end[next_line_start_index:].split()[0]
                           text_after_end=text_after_end[next_line_start_index:]
                            
                        if last_char=='.' and word_after_end[0]== '(':
                            pass
                        elif last_char=='.' and word_after_end== r"\item":
                            pass
                        elif word_after_end and word_after_end[0].isupper():
                            if last_char != '.':
                                line_no = self.find_line_number_for_equation(latex_content,equation)
                                if(line_no==None):
                                   continue
                                # print("The word after \\end{equation} starts with a capital letter, but the punctuation is not a full stop.")
                                # result.append("The word after \\end{equation} starts with a capital letter, but the punctuation is not a full stop."+equation+"next word is:"+word_after_end+"\n"+"\n")
                                result.append("Warning: '.' is not seen at the end of equation whose line no is {line_no}\n")
                        else:
                            if last_char != ',':
                                line_no = self.find_line_number_for_equation(latex_content,equation)
                                # print(word_after_end)
                                # print("***")
                                # result.append("Warning: ',' is not seen at the end of equation whose line no is {line_no}\n")
                                if(line_no==None):
                                  continue
                                # print("The word after \\end{equation} does not start with a capital letter, but the punctuation is not a comma.")
                                # result.append("The word after \\end{equation} does not start with a capital letter, but the punctuation is not a comma."+equation+"next word is:"+word_after_end+"\n"+"\n")
                                result.append(f"Warning: ',' is not seen at the end of equation whose line no is {line_no}\n")
                    else:
                        print(f"Error: Word after end of equation not found.")
                else:
                    print(f"Error: end{equation} not found after the equation.")
            elif last_char not in [',', '.']:
                # print("Warning: Punctuation not found at the end of the equation (if any).")
                line_no = self.find_line_number_for_equation(latex_content,equation)
                if(line_no==None):
                    continue                
                # if(line_no==None):
                #     print("****")
                result.append(f"Warning: Punctuation not found at the end of the equation whose line no is {line_no}\n")
        return result     
    def check_punctuation_align(self,latex_content):
        self.latex_content = latex_content
            # Define a regular expression to match LaTeX equations and labels
        equation_pattern = re.compile(r'\\begin{align}(.*?)\\end{align}', re.DOTALL)
        result=[]
        # Find all equations in the LaTeX file
        equations = re.findall(equation_pattern, latex_content)

        for equation in equations:
            if(equation.strip().split()[0].startswith('%')):
                continue            
            # Extract the equation label if present
            label_match = re.search(r'\\label{([^}]*)}', equation)
            last_char = equation.strip()[-1] if equation.strip() else None
            if last_char =="." or last_char ==",":
                index1 = latex_content.find(equation)
            else: 
                if label_match:
                    label = label_match.group(1)
    
                    # Check for punctuation before the label
                    index = equation.find('\\label{' + label + '}')
                    if index > 0:
                        preceding_text = equation[:index]
                    index1 = latex_content.find(equation)
                    # Check if there is a comma or period at the end of the preceding text
                    last_char = preceding_text.strip()[-1] if preceding_text.strip() else None

            if last_char in [',', '.']:
                # print(f"Punctuation ({last_char}) found before label '{label}' in equation (if any):\n{equation}")
    
                # Find the index of \end{equation} after the current equation
                end_equation_index = latex_content.find('\\end{align}', index1)
                if end_equation_index != -1:
                    # Extract the text immediately after \end{align}
                    text_after_end = latex_content[end_equation_index + len('\\end{align}'):].lstrip()
    
                    # Find the first word after \end{align}
                    match = re.search(r'\S+', text_after_end)
                    word_after_end = match.group()
                    # print(word_after_end)
                    
                    if word_after_end[0] == '%' or word_after_end == "%" :
                        end_index = match.end()  # Get the end index of the matched substring    
                        word_after_end = text_after_end[end_index:].split()[0]  # Get the next word after the matched substring
                        end_index_dupe=end_index
                        next_line_start_index = text_after_end.find('\n', end_index_dupe)
                        word_after_end=text_after_end[next_line_start_index:].split()[0]
                        text_after_end=text_after_end[next_line_start_index:]
                        while(word_after_end[0]=='%' or word_after_end==" "):
                        
                           next_line_start_index = text_after_end.find('\n', end_index_dupe)
                           end_index_dupe=next_line_start_index
                           word_after_end=text_after_end[next_line_start_index:].split()[0]
                           text_after_end=text_after_end[next_line_start_index:]
                        
                        if word_after_end==r"{\em":
                            index2 =  text_after_end.index(word_after_end)
                            start_index_next_word = index2 + len(word_after_end) + 1
                            word_after_end = text_after_end[start_index_next_word]
                            # print(word_after_end)
                        
                        if word_after_end[0:11]=="\\subsection":
                           next_line_start_index = text_after_end.find('\n', end_index_dupe)
                           end_index_dupe=next_line_start_index
                           word_after_end=text_after_end[next_line_start_index:].split()[0]
                           text_after_end=text_after_end[next_line_start_index:]
                           
                        if word_after_end[0:8]=="\\section":
                           next_line_start_index = text_after_end.find('\n', end_index_dupe)
                           end_index_dupe=next_line_start_index
                           word_after_end=text_after_end[next_line_start_index:].split()[0]
                           text_after_end=text_after_end[next_line_start_index:]   
                           
                        if word_after_end[0:6]=="\\label":
                           next_line_start_index = text_after_end.find('\n', end_index_dupe)
                           end_index_dupe=next_line_start_index
                           word_after_end=text_after_end[next_line_start_index:].split()[0]
                           text_after_end=text_after_end[next_line_start_index:]
                        
                            
                        if last_char=='.' and word_after_end[0]== '(':
                            pass
                        elif last_char=='.' and word_after_end[0].isalnum()==False:
                            pass
                        elif word_after_end[0].isalnum() and word_after_end[0].isupper():
                            if last_char != '.':
                                line_no = self.find_line_number_for_equation(latex_content,equation)
                                if(line_no==None):
                                    continue
                                # print("The word after \\end{equation} starts with a capital letter, but the punctuation is not a full stop.")
                                # result.append("The word after \\end{equation} starts with a capital letter, but the punctuation is not a full stop."+equation+"next word is:"+word_after_end+"\n"+"\n")
                                result.append(f"Error: ',' is seen instead of '.'  at the end of equation whose line no is {line_no}\n")
                        else:
                            if last_char != ',':
                                line_no = self.find_line_number_for_equation(latex_content,equation)
                                if(line_no==None):
                                    continue
                                # print(word_after_end)
                                # print("The word after \\end{equation} does not start with a capital letter, but the punctuation is not a comma.")
                                result.append(f"Error: '.' is seen instead of ',' of at the end of equation whose line no is {line_no}\n")
                    
                    elif word_after_end:
                        # word_after_end = match.group()
                        # print(word_after_end)
                        if r"\sub" in word_after_end:
                            # print("hi")
                            nextt=self.skip_line_by_first_word(text_after_end,word_after_end)
                            # print("\\\\\\\\\\\\\\\\\\\its done//////////////////"+nextt[0])
                            word_after_end = nextt
                            
                        if word_after_end==r"{\em":
                            index2 =  text_after_end.index(word_after_end)
                            start_index_next_word = index2 + len(word_after_end) + 1
                            word_after_end = text_after_end[start_index_next_word]
                        
                        if word_after_end[0:11]=="\\subsection":
                           next_line_start_index = text_after_end.find('\n', end_index_dupe)
                           end_index_dupe=next_line_start_index
                           word_after_end=text_after_end[next_line_start_index:].split()[0]
                           text_after_end=text_after_end[next_line_start_index:]                           
                           
                        if word_after_end[0:8]=="\\section":
                           next_line_start_index = text_after_end.find('\n', end_index_dupe)
                           end_index_dupe=next_line_start_index
                           word_after_end=text_after_end[next_line_start_index:].split()[0]
                           text_after_end=text_after_end[next_line_start_index:]
                        #    print(word_after_end)
                           
                        if word_after_end[0:6]=="\\label":
                           next_line_start_index = text_after_end.find('\n', end_index_dupe)
                           end_index_dupe=next_line_start_index
                           word_after_end=text_after_end[next_line_start_index:].split()[0]
                           text_after_end=text_after_end[next_line_start_index:]
                            
                        if last_char=='.' and word_after_end[0]== '(':
                            pass
                        elif last_char=='.' and word_after_end== r"\item":
                            pass
                        elif last_char=='.' and word_after_end[0].isalnum()==False:
                            pass
                        elif word_after_end and word_after_end[0].isupper():
                            if last_char != '.':
                                line_no = self.find_line_number_for_equation(latex_content,equation)
                                if(line_no==None):
                                    continue
                                # print("The word after \\end{equation} starts with a capital letter, but the punctuation is not a full stop.")
                                # result.append("The word after \\end{equation} starts with a capital letter, but the punctuation is not a full stop."+equation+"next word is:"+word_after_end+"\n"+"\n")
                                result.append(f"Warning: '.' is not seen at the end of equation whose line no is {line_no}\n")
                        else:
                            if last_char != ',':
                                line_no = self.find_line_number_for_equation(latex_content,equation)
                                # print(word_after_end)
                                # print("***")
                                # result.append("Warning: ',' is not seen at the end of equation whose line no is {line_no}\n")
                                if(line_no==None):
                                    continue
                                # print("The word after \\end{equation} does not start with a capital letter, but the punctuation is not a comma.")
                                # result.append("The word after \\end{equation} does not start with a capital letter, but the punctuation is not a comma."+equation+"next word is:"+word_after_end+"\n"+"\n")
                                result.append(f"Warning: ',' is not seen at the end of equation whose line no is {line_no}\n")
                    else:
                        print(f"Error: Word after end of align equation not found.")
                else:
                    print(f"Error: end{align} not found after the equation.")
            elif last_char not in [',', '.']:
                line_no = self.find_line_number_for_equation(latex_content,equation)
                if(line_no==None):
                         continue
                # print("Warning: Punctuation not found at the end of the equation (if any).")
                # if(line_no==None):
                #    print("&&&&")
                result.append(f"Warning: Punctuation not found at the end of the equation whose line no is {line_no}\n")
        return result    
    def check_math_operator(self,latex_content):
        self.latex_content=latex_content
        equation_pattern=re.compile(r'\\begin{multline}(.*?)\\end{multline}', re.DOTALL)
        result=[]
        math_operator=["+","-",">","<","=","/","\times"]
        # other_operator=["\leq","\geq"]
        other_operator = [r"\leq", r"\geq"]

        equations = re.findall(equation_pattern,latex_content)
        for equation in equations:
           dupeq=equation
           if(equation.strip().split()[0].startswith('%')):
              continue
           equation=equation.replace(" ",'')
        #    print(equation)
           for i in range(len(equation)):
               if equation[i]=="\\" and equation[i+1]=="\\":
                   if equation[i-1] not in math_operator and equation[i+2] in math_operator:
                        # print("yes***")
                        # print(equation[i-1])
                        pass
                   if equation[i-1] not in math_operator and equation[i+2:i+6] in other_operator:
                    #   // print("yes")
                    #    print(equation[i-1])
                       pass
                   else:
                       if equation[i-1] in math_operator:
                        #    print("The math operator should not be there before \\")
                        #    print(equation[i-1])
                           line_no = self.find_line_number_for_equation(latex_content,dupeq)
                           if(line_no==None):
                                continue
                           result.append(f"The math operator should not be there before in this equation whose line no is {line_no}\n")
        return result

    def run(self):  # The function which is going to be invoked in the wrapper class should contain no arguments

        output = [] # The output list with the errors to be returned
        text = self.latex_code
        result1=self.check_punctuation(text) 
        result2=self.check_punctuation_align(text) 
        result3=self.check_punctuation_between_multiequations(text) 
        result4=self.check_punctuations_for_array(text)
        result5=self.check_math_operator(text)
        start="""
===============================================================
                Equation related comments
===============================================================\n"""
        oprel="""
===============================================================
                Math operator related comments
===============================================================\n"""
        output.extend(start)
        output.extend(result1)
        output.extend(result2)    
        output.extend(result3)
        output.extend(result4)
        output.extend(oprel)
        output.extend(result5)
        return output