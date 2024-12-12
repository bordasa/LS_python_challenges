#PEDAC
#Problem Overview
    #Input: a leter
    #Output: a diamond
        #line 1: "A\n"
        #line 2: " A \nB B\n A\n"
        #line 3: "  A  \n B B \nC   C\n B B \n  A  \n"
#Examples: see unit tests
#Data Structure: lists and strings
#Algorithm:
    #1. Get input letter
    #2. Make diamond_letters_list
    #3. Use diamond_letters_list to make each line
    #4. Save each line into a list of lines
    #5. join the list


class Diamond:

    @classmethod
    def make_letters_list(cls, letter):
        return [chr(ascii_val) 
                        for ascii_val in range(ord('A'), ord(letter)+1)]
    
    @classmethod
    def make_line(cls, letter, max_width, prev_line_len):
        if letter == "A":
            side_padding = " " * (max_width // 2)
            
            return f"{side_padding}{letter}{side_padding}\n"
        
        center_padding = " " * prev_line_len
        side_padding = " " * ((max_width - prev_line_len - 2) // 2)

        return f"{side_padding}{letter}{center_padding}{letter}{side_padding}\n"

    @classmethod
    def calc_prev_line_width(cls, line_list):
        if line_list:
            line = line_list[-1].strip(" \n")
            return len(line)
        return 0

    @classmethod
    def make_diamond(cls, letter):
        letters_list = cls.make_letters_list(letter)
        
        top_half_line_list = []
        max_width = 2 * len(letters_list) - 1

        for letter in letters_list:
            prev_line_width = cls.calc_prev_line_width(top_half_line_list)
            line = cls.make_line(letter, max_width, prev_line_width)
            top_half_line_list.append(line)
        
        bottom_half_line_list = top_half_line_list[-2::-1]
        full_line_list = top_half_line_list + bottom_half_line_list

        return ('').join(full_line_list)

# print(Diamond.make_diamond('Z'))