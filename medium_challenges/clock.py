class Clock:
    def __init__(self, hour, min=0):
        self._hour = hour
        self._min = min
    
    @property
    def hour(self):
        return self._hour
    
    @hour.setter
    def hour(self, hour):
        while hour < 0:
            hour += 24
        while hour >= 24:
            hour -= 24
        
        self._hour = hour

    @property
    def min(self):
        return self._min
    
    @min.setter
    def min(self, min):
        while min < 0:
            self.hour -= 1
            min += 60
        while min >= 60:
            self.hour += 1
            min -= 60
        
        self._min = min

    def __str__(self):
        return f"{self.hour:02d}:{self.min:02d}"
    
    @classmethod
    def at(cls, hour, min=0):
        return Clock(hour, min)
    
    def __add__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        
        new_clock = Clock(self.hour, self.min)
        new_clock.min += other
        return new_clock
    
    def __sub__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        
        new_clock = Clock(self.hour, self.min)
        new_clock.min -= other
        return new_clock
    
    def __eq__(self, other_clock):
        if not isinstance(other_clock, Clock):
            return NotImplemented
        
        if str(self) == str(other_clock):
            return True
        return False

clock = Clock(1, 30)
print(clock)
clock2 = clock - 40 - 60
print(clock2)
# print(Clock.at(9, 10))