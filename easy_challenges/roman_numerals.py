# Problem Overview:
    #input: a number
    #ouput: roman numeral equivalent

# Examples: see test suite

# Data Structures: Using a dictionary to store each numeral

# Algorithm:
    #1. iterate through numerals dict
    # 2. divmod(num, numerals_dict.key) = (quotient, remainder)
        #2a. add quotient * dict.value to result string
    # 3. Keep doing this until remainder == 0


class RomanNumeral:

    dict = { 
                      1000: 'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
                     }

    def __init__(self, number):
        self.number = number
    
    def to_roman(self):
        numerals = ""
        remainder = self.number

        while remainder > 0:
            for key, value in RomanNumeral.dict.items():
                multiplier, remainder = divmod(remainder, key)

                numerals += multiplier * value

        return numerals


