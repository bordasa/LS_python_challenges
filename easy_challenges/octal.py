# Problem Overview
    #input: octal number as string
    #output: decimal number (instance method .to_decimal()) as num
    #rules: only 0-7 are valid numbers. Return 0 for invalid numbers

# Examples: see test suite

# Data Structure: strings and integers

# Algorithm:
    #1. Save input octal string
    #2. starting from the right, look at each digit char (reverse str?)
    #3. Check if it is a num between 0 and 7. If not, return 0
    #4. else: multiply 8**index and add to final result
    #5. Return result

# Code

class Octal:
    def __init__(self, octal_str):
        self.octal_str = octal_str
    
    def to_decimal(self):
        reversed_octal_str = self.octal_str[::-1]
        decimal_num = 0

        for i in range(len(self.octal_str)):
            if reversed_octal_str[i] not in "01234567":
                return 0
            
            decimal_num += (int(reversed_octal_str[i]) * 8**i)
        
        return decimal_num


            