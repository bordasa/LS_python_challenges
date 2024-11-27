# Problem Overview
    # input: a string and a list of other strings
    # output: a list of matching anagrams
        #Rules: No match and multiple matches are possible
            # Cannot be the same word (even with different case)
            # Case doesn't matter for actual anagrams

# Examples: See test suite

# Data Structure: character dictionaries for comparison

# Algorithm:
    #1. store the input string
    #2. create a count dict for the input string
    #3. for each element in list: create count dict
        #3a. check that the anagram is not the same as the input string
        #3b. if count dict == input count dict, then add to results list
    #4. return list of anagrams

class Anagram:
    def __init__(self, word):
        self.word = word
        self.input_count_dict = self.create_count_dict(self.word)
    
    def create_count_dict(self, word):
        count_dict = {}

        for char in word.lower():
            count_dict.setdefault(char, 0)
            count_dict[char] += 1
        
        return count_dict
    
    def is_anagram(self, other_word):
        if self.word.lower() == other_word.lower():
            return False
        
        other_word_count_dict = self.create_count_dict(other_word)

        return self.input_count_dict == other_word_count_dict
        
    def match(self, word_list):
        return [word for word in word_list if self.is_anagram(word)]
