class Scrabble:
    SCORE_DICT = {'aeioulnrst': 1,
                  'dg': 2,
                  'bcmp': 3,
                  'fhvwy': 4,
                  'k': 5,
                  'jx': 8,
                  'qz': 10
                  }
    
    def __init__(self, word):
        self.word = word if word else ""
    
    def score(self):
        score = 0

        for char in self.word.lower():
            for letters, points in Scrabble.SCORE_DICT.items():
                if char in letters:
                    score += points

        return score


    @classmethod
    def calculate_score(cls, word):
       return cls(word).score()