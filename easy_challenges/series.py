class Series:
    def __init__(self, num_string):
        self.num_list = [int(num) for num in num_string]
    
    def slices(self, num_slices):
        serieses = []
        if num_slices > len(self.num_list):
            raise ValueError("Slice is longer than the digit series")
        
        for idx in range(len(self.num_list)):
            if len(self.num_list[idx:]) >= num_slices:
                serieses.append(self.num_list[idx: idx + num_slices])
        
        return serieses
