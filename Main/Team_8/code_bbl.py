"""Tasks given:
   1).To find syntax related errors in different references like journal,conference,textbook,etc
   2.To find acronym related errors
   3.To print a list of Electrical Engineering related acronyms used in bibliography
(more names can be added to the list electrical_engineering_acronyms[] to make it more exhaustive)
   4.To find and print number of times a each reference has been cited in the latex document
   5.To print the total number of references"""
import re
class team_8:
    # Constructor
    def __init__(self, latex_code,bbl_code,text_begin):
        self.latex_code = latex_code  # The entire LaTex code is in the form of string in the latex_code string
        self.text_begin = text_begin  # location of \begin
        self.bbl_code = bbl_code
        
    def run(self):  # will be invoked by wrapper, shouldn't take arguments
        output = []
        text = self.latex_code
        text1 = self.bbl_code

        # use self
        str_line = '=' * 50
        output.append(str_line + '\n\tSyntax related comments\n' + str_line + '\n')
        output.append('Reference'+str(' '*21)+'Number'+str(' '*3)+'Comments\n')
        bibliography = self.extract_bibliography(text1)
        # Split the text by \bibitem{
        split_text = bibliography.split('\\bibitem{') 
        # Create a dictionary with keys and lists starting from 1
        my_dictionary = {item.split('}')[0]: [index + 1] for index, item in enumerate(split_text[1:])}
        for key in my_dictionary:
            my_dictionary[key].append(0)
        self.syntax(bibliography,output)
        
        output.append(str_line + '\n\tAcronym related comments\n' + str_line + '\n')
        output.append('Reference'+str(' '*21)+'Number'+str(' '*3)+'Comments\n')
        EE=[]
        self.acronym(bibliography,output,EE)
        
        output.append(str_line + '\n\tList of Electrical Engineering related Acronyms\n' + str_line + '\n')
        rs = ', '.join(EE)
        output.extend([rs,'\n'])
        
        output.append(str_line + '\n\tCitation related comments\n' + str_line + '\n')
        self.cite(text,output,my_dictionary)
        output.append('Reference'+str(' '*21)+'Number'+str(' '*5)+'No. of times cited\n')
        x=0
        
        for key in my_dictionary:
            if my_dictionary[key][0]<=9:
                x=10
            else:
                x=9
            output.extend([key+str(' '*(30-len(key)))+str(my_dictionary[key][0])+str(' '*x)+str(my_dictionary[key][1])+"\n"])
        output.extend(["\nTotal number of references = ",str(len(my_dictionary)),"\n"])
        
        return output

    def extract_bibliography(self, text):
        bibliography_pattern = re.compile(r'\\begin{thebibliography}(.*?)\\end{thebibliography}', re.DOTALL)
        match = bibliography_pattern.search(text)
        if match:
            return(match.group(1).strip())
        else:
            return(None)
    def cite(self,text,output,my_dictionary):
        # Use regular expression to find \cite{...}
        pattern = re.compile(r'\\cite{([^}]+)}')
        # Find all matches in the text
        matches = pattern.findall(text)
        
        # Iterate through each match
        for match in matches:
            # Split the match into sub-elements
            sub_elements = match.split(',')
            # Check if each sub-element is present in the other dictionary
            for sub_element in sub_elements:
                if sub_element.strip() in my_dictionary:
                    my_dictionary[sub_element.strip()][1]=my_dictionary[sub_element.strip()][1]+1
    
    def syntax(self,bibliography,output):
        split1=bibliography.split('\\bibitem')
        del(split1[0])
        #To separate bib_content into three parts
        for i in split1:
            split2=[]
            split2.append(i[:i.find("``")])
            split2.append(i[i.find("``")+2:i.find("''")])
            split2.append(i[i.find("''")+2:])
            refname=split2[0][1:split2[0].find('}')]
            
            split2[0]=split2[0][split2[0].find('}')+1:len(i)]
            split2[0]=split2[0].strip()
            split2[1]=split2[1].strip()
            split2[2]=split2[2].strip()
            if ("``" not in i and "''" in i) or ("''" not in i and "``" in i):
                output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        quotes are missing\n")
             
            elif "``" in i and "''" in i:
                #Author names check
                if '.' not in split2[0]:
                    output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        Author names should be in should be in short form like K.~Mehta or A.~N. Mishra\n")
                if '~' not in split2[0]:
                    output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        Author names should contain ~ like K.~Mehta or A.~N. Mishra\n")
                
                xi = None
                index_counter = 0
                while index_counter < len(split2[0]):
                    x = split2[0][index_counter]   
                    if x in ['\t', ' ', '~'] and index_counter + 1 < len(split2[0]):
                        if split2[0][index_counter + 1].isalpha() and split2[0][index_counter + 1].islower() and (index_counter + 2 < len(split2[0]) and split2[0][index_counter + 2] != 'n'):
                            output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+str(y)+"        Author names should be in should be in short form and capital like K.~Mehta\n")
                    index_counter += 1
                #comma check
                (ct,cc)=(0,0)
                for x in split2[0]:
                    if x=='~':
                        ct+=1
                    if x==',':
                        cc+=1
                if cc<ct:
                    
                    if split2[0][-1]!=',':
                        output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        comma is missing before opening quote\n")
                        cc+=1
                    if split2[1][-1]!=',':
                        output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        comma is missing before opening quote\n")
                    if 'and' in split2[0]:
                        y=split2[0].find('and')
                        if ct>2 and split2[0][y-2]!=',' :
                            output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        comma is missing before and\n")
                            cc+=1
                    if cc<ct and ct>2:
                        output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        comma is missing between author names\n")
            
            #journal,
            if 'Trans.' in split2[2]:
                #full form check
                if 'volume' in split2[2] or 'Volume' in split2[2]:
                    output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        volume should be in short form like vol.~\n")
                if 'number' in split2[2] or 'Number' in split2[2]:
                    output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        number should be in short form like no.~\n")
                if 'page number' in split2[2] or 'Page Number' in split2[2] or 'page number range' in split2[2]:
                    output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        page number should be in short form like pp. 11--22\n")
                if 'January' in split2[2] or 'February' in split2[2] or 'March' in split2[2] or 'April' in split2[2] or 'June' in split2[2] or 'July' in split2[2] or 'August' in split2[2] or 'September' in split2[2] or 'October' in split2[2] or 'November' in split2[2] or 'December' in split2[2]:
                    output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        month should be in short form like Jan. (except May)\n")
                #vol missing check
                if 'vol' not in split2[2]:
                    output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        volume is missing\n")
                else:
                    j=split2[2].rfind('vol')
                    if split2[2][j+3]!='.':
                        output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        full stop is missing after vol\n")
                    if split2[2][j+4]!='~' and split2[2][j+3]!='~':
                        output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        Warning:~ is missing after vol.\n")
                #no missing check
                if 'no' not in split2[2]:
                    output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        number is missing\n")
                else:
                    j=split2[2].rfind('no')
                    if split2[2][j+2]!='.':
                        output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        full stop is missing after no\n")
                    if split2[2][j+2]!='~' and split2[2][j+3]!='~':
                        output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        Warning:~ is missing after no.\n")
                if 'pp' not in split2[2]:
                    output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        pp is missing\n")
                else:
                    j=split2[2].rfind('pp')
                    if split2[2][j+2]!='.':
                        output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        full stop is missing after pp\n")
                    if '--' not in split2[2]:
                        output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        double hyphen should be used for page number range\n")
                #date missing check
                if 'Jan' not in split2[2] and 'Feb' not in split2[2] and 'Mar' not in split2[2] and 'Apr' not in split2[2] and 'May' not in split2[2] and 'Jun' not in split2[2] and 'Jul' not in split2[2] and 'Aug' not in split2[2] and 'Sep' not in split2[2] and 'Oct' not in split2[2] and 'Nov' not in split2[2] and 'Dec' not in split2[2]:
                    output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"     month is missing \n")
                else:
                    f=0
                    for m in ['Jan.','Feb.','Mar.','Apr.','May','Jun.','Jul.','Aug.','Sep.','Oct.','Nov.','Dec.']:
                        if m in split2[2]:
                            f=1
                            break
                    if f==0:
                        output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        full stop is missing after month in short form\n")
            #Conference check
            if 'Proc.' in split2[2]:
                if 'page number' in split2[2] or 'Page Number' in split2[2] or 'page number range' in split2[2]:
                    output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"         page number should be in short form like pp. 11--22\n")
                if 'January' in split2[2] or 'February' in split2[2] or 'March' in split2[2] or 'April' in split2[2] or 'June' in split2[2] or 'July' in split2[2] or 'August' in split2[2] or 'September' in split2[2] or 'October' in split2[2] or 'November' in split2[2] or 'December' in split2[2]:
                    output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"     month should be in short form like Jan. (except May)\n")
                if 'volume' in split2[2] or 'Volume' in split2[2]:
                    output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"         volume should be in short form like vol.~\n")
                if 'number' in split2[2] or 'Number' in split2[2]:
                    output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        number should be in short form like no.~\n")

                if 'Jan' not in split2[2] and 'Feb' not in split2[2] and 'Mar' not in split2[2] and 'Apr' not in split2[2] and 'May' not in split2[2] and 'Jun' not in split2[2] and 'Jul' not in split2[2] and 'Aug' not in split2[2] and 'Sep' not in split2[2] and 'Oct' not in split2[2] and 'Nov' not in split2[2] and 'Dec' not in split2[2]:
                    output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"     month is missing \n")
                else:
                    f=0
                    for m in ['Jan.','Feb.','Mar.','Apr.','May','Jul.','Aug.','Sep.','Oct.','Nov.','Dec.']:
                        if m in split2[2]:
                            f=1
                            break
                    if f==0:
                        output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        full stop is missing after month in short form\n")

                if 'pp' not in split2[2]:
                    output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        pp is missing\n")
                else:
                    j=split2[2].rfind('pp')
                    if split2[2][j+2]!='.':
                        output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        full stop is missing after pp\n")
                    if '--' not in split2[2]:
                        output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        double hyphen should be used for page number range\n")
                if 'vol' not in split2[2]:
                    pass
                else:
                    j=split2[2].rfind('vol')
                    if split2[2][j+3]!='.':
                        output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        full stop is missing after vol\n")
                    if split2[2][j+4]!='~' and split2[2][j+3]!='~':
                        output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        Warning:~ is missing after vol.\n")
                if 'no' not in split2[2]:
                    pass
                else:
                    j=split2[2].rfind('no')
                    if split2[2][j+2]!='.':
                        output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        full stop is missing after no\n")
                    if split2[2][j+2]!='~' and split2[2][j+3]!='~':
                        output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        Warning:~ is missing after no.\n")
            #Others check
            if 'Trans' not in split2[2] and'Proc.' not in split2[2]:
                if 'volume' in split2[2] or 'Volume' in split2[2]:
                    output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        volume should be in short form like vol.~\n")
                if 'number' in split2[2] or 'Number' in split2[2]:
                    output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        number should be in short form like no.~\n")
                if 'page number' in split2[2] or 'Page Number' in split2[2] or 'page number range' in split2[2]:
                    output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        page number should be in short form like pp. 11--22\n")
                if 'January' in split2[2] or 'February' in split2[2] or 'March' in split2[2] or 'April' in split2[2] or 'June' in split2[2] or 'July' in split2[2] or 'August' in split2[2] or 'September' in split2[2] or 'October' in split2[2] or 'November' in split2[2] or 'December' in split2[2]:
                    output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        month should be in short form like Jan. (except May)\n")
                if 'vol' not in split2[2]:
                    pass
                else:
                    j=split2[2].rfind('vol')
                    if split2[2][j+3]!='.':
                        output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        full stop is missing after vol\n")
                    if split2[2][j+4]!='~' and split2[2][j+3]!='~':
                        output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        Warning:~ is missing after vol.\n")
                if 'no' not in split2[2]:
                    pass
                else:
                    j=split2[2].rfind('no')
                    if split2[2][j+2]!='.':
                        output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        full stop is missing after no\n")
                    if split2[2][j+2]!='~' and split2[2][j+3]!='~':
                        output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        Warning:~ is missing after no.\n")
                if 'pp' not in split2[2]:
                    pass
                else:
                    j=split2[2].rfind('pp')
                    if split2[2][j+2]!='.':
                        output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        full stop is missing after pp\n")
                    if '--' not in split2[2]:
                        output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        double hyphen should be used for page number range\n")
                if 'Jan' not in split2[2] and 'Feb' not in split2[2] and 'Mar' not in split2[2] and 'Apr' not in split2[2] and 'May' not in split2[2] and 'Jun' not in split2[2] and 'Jul' not in split2[2] and 'Aug' not in split2[2] and 'Sep' not in split2[2] and 'Oct' not in split2[2] and 'Nov' not in split2[2] and 'Dec' not in split2[2]:
                    pass
                else:
                    f=0
                    for m in ['Jan.','Feb.','Mar.','Apr.','Mays','Jun.','Jul.','Aug.','Sep.','Oct.','Nov.','Dec.']:
                        if m in split2[2]:
                            f=1
                            break
                    if f==0:
                        output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        full stop is missing after month in short form\n")
    
    def acronym(self,bibliography,output,EE):
        #more ee acronyms can be added to this list in future if required
        ee_acronyms = [
        "PLD", "VHDL", "ASIC", "RTL", "GUI",
        "GSM", "CDMA", "LTE", "RFID", "ZIF",
        "MTBF", "QFN", "PFC", "UPS", "NAND",
        "IIR", "FIR", "EMC", "ECL", "PCI",
        "LAN", "CAN", "LIN", "JTAG", "GPIO",
        "RTOS", "HDL", "HMI", "PID", "HDD",
        "VLSI", "OSI", "VGA", "PCB", "USB",
        "DDR", "IOT", "ZIF", "SMT", "EEPROM",
        "ADC", "DAC", "DCM", "PLL", "DDS",
        "GPS", "DVI", "PWM", "RISC", "CISC",
        "MIPS", "SPICE", "ROM", "RAM", "FPGA",
        "DSP", "ISP", "QAM", "SDRAM", "SCADA",
        "LVDT", "RTOS", "ARM", "SIMD", "LED",
        "IOT", "VCO", "DCS", "BOM", "MOSFET",
        "HBT", "ESD", "CMOS", "ASIC", "PAM",
        "CRC", "IEEE", "OEM", "PCBA", "ICP",
        "VLSI", "APD", "APM", "GFCI", "MOSFET",
        "LSI", "PCMCIA", "FET", "NOR", "XOR",
        "ADC", "VGA", "DIP", "LCD", "VCO",
        "PLL", "RFM", "JFET", "LTE-A", "SIMO",
        "MIMO", "QPSK", "IRIG", "CMRR", "NEC",
        "CCD", "DRAM", "OLED", "VCO", "SDLC",
        "SIMD", "SPI", "ISO", "EEPROM", "SOC",
        "NAND", "SCPI", "UART", "USB-C", "WDM"]
        additional_acronyms = [
        "ASIC", "PCIe", "USB3", "HDMI", "DSPIC",
        "HDL", "RTOS", "CANopen", "LINbus", "UART",
        "I2C", "SPI", "CANFD", "HDLC", "TCP/IP",
        "UDP", "EEPROM", "BIOS", "EPROM", "HSM",
        "SBC", "ISO9001", "ISO14001", "ISO26262", "CANopen",
        "LINbus", "FMEA", "FMECA", "RCM", "RAMS",
        "SCR", "GTO", "IGBT", "MCT", "THD"]

        # Extend the original list with the additional acronyms
        ee_acronyms.extend(additional_acronyms)
        additional_acronyms_2 = [
        "PID", "ESC", "CANopen", "MISO", "MOSI",
        "RTOS", "FFT", "PFC", "SPICE", "ESD",
        "AGC", "ADC", "DAC", "PCBA", "CMSIS",
        "DMA", "CRC", "IIR", "FIR", "FPGA",
        "ASIC", "VHDL", "EEPROM", "SOC", "QFN",
        "GFCI", "MOSFET", "SCADA", "RFID", "ZIF",
        "HBT", "ESD", "CMOS", "PAM", "PLL",
        "DDS", "DVI", "PWM", "RISC", "CISC",
        "MIPS", "SDRAM", "LVDT", "ARM", "SIMD",
        "LED", "VCO", "DCS", "BOM", "IOT",
        "MIMO", "QPSK", "IRIG", "CMRR", "NEC",
        "CCD", "DRAM", "OLED", "VCO", "SDLC",
        "SPI", "ISO", "NOR", "XOR", "VGA",
        "DIP", "LCD", "RFM", "JFET", "LTE-A",
        "SIMO", "QAM", "DSPIC", "DCM", "PLL",
        "USB3", "HDMI", "CANFD", "HDLC", "TCP/IP",
        "UDP", "BIOS", "EPROM", "HSM", "SBC",
        "FMEA", "RCM", "RAMS", "SCR", "GTO",
        "IGBT", "MCT"]

        # Extend the original list with the second set of additional acronyms2
        ee_acronyms.extend(additional_acronyms_2)
        split1=bibliography.split('\\bibitem')
        del(split1[0])
        #output.extend(split1[0])
        for i in split1:
            split2=[]
            split2.append(i[:i.find("``")].strip())
            split2.append(i[i.find("``")+2:i.find("''")].strip())
            split2.append(i[i.find("''")+2:].strip())
            refname=split2[0][1:split2[0].find('}')]
            split2[0]=split2[0][split2[0].find('}')+1:]
            
            if "``" in i and "''" in i:
                # List of delimiters
                delimiters = [',', ' ', ':','\n','\t']
                # Construct a regular expression pattern with the delimiters
                pattern = '|'.join(map(re.escape, delimiters))
                # Split the string based on the delimiters using re.split()
                sp = re.split(pattern, split2[1])
                if '' in sp:
                    sp = [x for x in sp if x != '']
                #output.extend(["In reference number [",str(split1.index(i)+1),"],",str(sp)])
                for word in sp:
                    c=0
                    for w in word:
                        if w.isalpha() and w.isupper():
                            c+=1
                    if c>=2:
                        if word[0]!='{' and word[-1]!='}':
                            output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        Warning:acronym ",word," should be in curly braces\n")
                        elif word[0]!='{':
                            output.extend(refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        opening brace is missing before acronym ",word,"\n")
                        elif '}' not in word:
                            output.extend([refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        closing brace is missing after acronym ",word,"\n"])
                for word in sp:
                    delimiters1 = ['{', '}', '-','/']
                    # Construct a regular expression pattern with the delimiters
                    pattern1 = '|'.join(map(re.escape, delimiters1))
                    # Split the string based on the delimiters using re.split()
                    nw = re.split(pattern1, word)
                    if '' in nw:
                        nw = [x for x in nw if x != '']
                    for wd in nw:
                        c=0
                        for wdd in wd:
                            if wdd.isalpha() and wdd.isupper():
                                c+=1
                        if c>=2 and c!=len(wd):
                            output.extend([refname+str(' '*(30-len(refname)))+str(split1.index(i)+1)+"        Warning:acronym ",wd," should be in capitals\n"])
                        if wd.upper() in ee_acronyms and wd.upper() not in EE:
                            EE.append(wd.upper())

                

                                                                                                            
