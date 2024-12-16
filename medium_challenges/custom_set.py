
class CustomSet:
    def __init__(self, elements = None):
        self._elements = []
        if elements:
            for element in elements:
                self.add(element)

    def is_empty(self):
        return len(self._elements) == 0

    def contains(self, num):
        return (num in self._elements)

    def is_subset(self, other_set):
        if not isinstance(other_set, CustomSet):
            return NotImplemented

        if self.is_empty():
            return True
        
        for element in self._elements:
            if element not in other_set._elements:
                return False
            
        return True

    def is_disjoint(self, other_set):
        if not isinstance(other_set, CustomSet):
            return NotImplemented

        if self.is_empty() or other_set.is_empty():
            return True
        
        for element in self._elements:
            if element in other_set._elements:
                return False
            
        return True

    def is_same(self, other_set):
        if not isinstance(other_set, CustomSet):
            return NotImplemented

        if len(self._elements) != len(other_set._elements):
            return False
        
        # for element in self._elements:
        #     if element not in other_set._elements:
        #         return False
        
        # return True
        return self.is_subset(other_set)
    
    def __eq__(self, other_set):
        return self.is_same(other_set)

    def add(self, element):
        if not self.contains(element):
            self._elements.append(element)

    def intersection(self, other_set):
        if not isinstance(other_set, CustomSet):
            return NotImplemented
        
        return CustomSet([element for element in self._elements
                          if other_set.contains(element)])

    def difference(self, other_set):
        if not isinstance(other_set, CustomSet):
            return NotImplemented
        
        return CustomSet([element for element in self._elements
                          if not other_set.contains(element)])

    def union(self, other_set):
        if not isinstance(other_set, CustomSet):
            return NotImplemented
        
        union_set = CustomSet(self._elements)

        for element in other_set._elements:
            union_set.add(element)
        
        return union_set

