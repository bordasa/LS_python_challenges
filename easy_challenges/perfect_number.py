# Problem Overview
    #Input: integer
    #Output: classification "deficient", "perfect", "abundant"
        #Rules: -No negative numbers

# Examples: see test suite

# Data Structure: List of the divisors

# Algorithm:
    #1. Save input number
    #2. Find all positive factors of the number (divisors). Not the num
    #3. Find sum of the factors
    #4. Compare sum to the input number. return classification

# Code

class PerfectNumber:

    @classmethod
    def classify(cls, num):
        if num <= 0:
            raise ValueError("Input must be a positive integer")
        
        divisors = []

        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
                
        aliquot_sum = sum(divisors)

        if aliquot_sum > num:
            return "abundant"
        elif aliquot_sum < num:
            return "deficient"
        else:
            return "perfect"
