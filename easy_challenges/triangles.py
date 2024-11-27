# Problem Overview
# Input: 3 sides of a potential triangle
# Output: "equilateral", "isosceles", "scalene"
# Rules: 1. All sides must be > 0
        #2. sum of the lengths of any two sides > length of the third
        #3. Raise ValueError if lengths don't work

# Examples

# Data Structures: Set will tell me if there are same sides

# Algorithm:
    # 1. Check that all sides are > 0. If not, raise Value Error
    # 2. Check that s1 + s2 > s3. If not, raise Value Error
    # 3. Create a set using the sides. if len(set) = 1, 2, 3, choose type

# Code

class Triangle:
    def __init__(self, s1, s2, s3):
        self.sides = [s1, s2, s3]

        self.check_valid_sides(s1, s2, s3)

    @property
    def kind(self):
        match len(set(self.sides)):
            case 1:
                return "equilateral"
            case 2:
                return "isosceles"
            case 3:
                return "scalene"

    
    def check_valid_sides(self, s1, s2, s3):
        if (s1 <= 0 or s2 <= 0 or s3 <= 0):
            raise ValueError("All sides must be greater than 0.")
        
        if not (s1 + s2 > s3 and s2 + s3 > s1 and s3 + s1 > s2):
            raise ValueError("One or more side lengths are too short.")