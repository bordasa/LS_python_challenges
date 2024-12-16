#PEDAC
#Problem: Create a linked list implementation. LIFO
    #Needs: For Element class:
        # getter property datum
        # instance method is_tail()
        # getter property next which is an element
        # initialize with or without the next

    # For SimpleLinkedList()
        # can instantiate as empty
        # instance method is empty
        # property size checks num of elements, 
        #   peek() looks at last element added-- the head. No arg.
        #   push() adds an element to the list-- the head. arg = datum
        #   pop() removes the head of the list
        # property getter head
        # class method SimpleLinkedList.from_list([]) - Can handle None/ []
        #       from list builds list from end to start (idx 0 is the head)
        # instance method to_list() converts it back
        # instance method reverse() creates new list

class Element:
    def __init__(self, data, next = None):
        self._datum = data
        self._next = next

    def is_tail(self):
        return self._next == None
    
    @property
    def datum(self):
        return self._datum
    
    @property
    def next(self):
        return self._next
    
    # @next.setter
    # def next(self, other_element):
    #     if not isinstance(other_element, Element):
    #         raise TypeError('Next element must be of class Element.')
        
    #     self._next = other_element

class SimpleLinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    @property
    def size(self):
        return self._size

    @property
    def head(self):
        return self._head

    def is_empty(self):
        return self.size == 0
    
    def peek(self):
        if self.head:
            return self.head.datum
        else:
            return None
    
    def push(self, data):
        old_head = self.head
        self._head = Element(data, old_head)
        self._size += 1
    
    def pop(self):
        if self.head:
            old_head = self.head
            self._head = self.head.next
            self._size -= 1
            return old_head.datum
        else:
            return None

    @classmethod
    def from_list(cls, lst):
        new_linked_list = SimpleLinkedList()
        
        if lst:
            for data in lst[::-1]:
                new_linked_list.push(data)
        
        return new_linked_list
    
    def to_list(self):
        elements_list = []
        pointer = self.head

        while pointer:
            elements_list.append(pointer.datum)
            pointer = pointer.next
        
        return elements_list
    
    def reverse(self):
        # elements_list = self.to_list()
        # elements_list.reverse()
        # return SimpleLinkedList.from_list(elements_list)
        if self.size:
            curr_element = self.head
            prev_element = None

            while curr_element:
                temp_element = curr_element.next
                curr_element._next = prev_element
                prev_element = curr_element
                curr_element = temp_element
            
            self._head = prev_element
        
        return self




                
