
class SumOfMultiples:
    def __init__(self, *args):
        self.number_set = args if args else [3, 5]
    
    @classmethod
    def sum_up_to(cls, number):
        return SumOfMultiples().to(number)

    def to(self, number):
        multiples = []

        for num in range(number):
            for multiple in self.number_set:
                if num % multiple == 0:
                    multiples.append(num)
        
        multiples = set(multiples)

        return sum(multiples)

# print(SumOfMultiples.sum_up_to(20))