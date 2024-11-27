# Problem Overview
    # Input: 2 DNA strands of varying length
    # Output: Hamming distance (number of point mutation)
    # Rules: If 2 different lengths, use the shorter length

# Examples:

# Data Structures: strings will be fine

# Algorithm
    #1. Get 2 strands
    #2. Compare each strand 1 char at a time
    #3. Track the differences (count)
    #4. stop when 1 strand is done
    #5. Return total count

class DNA:
    def __init__(self, strand):
        self.strand = strand
    
    def hamming_distance(self, other_dna):
        i= 0
        differences = 0

        while i < len(self.strand) and i < len(other_dna):
            if self.strand[i] != other_dna[i]:
                differences += 1
            
            i += 1
        
        return differences
    