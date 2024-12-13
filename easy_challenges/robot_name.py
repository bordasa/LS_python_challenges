import random

class Robot:
    _names = set()

    def __init__(self):
        self._name = None
    
    @property
    def name(self):
        if not self._name:
            self._name = Robot.assign_name()
        
        return self._name
    
    @classmethod
    def is_name_valid(cls, name):
        return name not in Robot._names

    @classmethod
    def suggest_random_name(cls):
        letters = [chr(num) for num in range(ord('A'), ord('Z') + 1)]
        nums = [num for num in range(10)]

        name_part1 = random.choice(letters) + random.choice(letters)
        name_part2 = ''
        for _ in range(3):
            name_part2 += str(random.choice(nums))
        
        full_name = name_part1 + name_part2

        return full_name
    
    @classmethod
    def assign_name(cls):
        while True:
            name = cls.suggest_random_name()

            if cls.is_name_valid(name):
                Robot._names.add(name)
                return name
        
    def reset(self):
        Robot._names.discard(self._name)
        self.__init__()

# robot = Robot()
# print(robot.name)
# robot2 = Robot()
# robot2.reset()
# robot.reset()
# print(Robot.NAMES)