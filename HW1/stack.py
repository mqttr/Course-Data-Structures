class Element():
    def __init__(self, data: any, prev):
        self.__data = data
        self.__prev = prev

    def view_element(self):
        return self.__data
    
    def previous_element(self):
        return self.__prev
    
    def __str__(self):
        return str(self.__data)


class Stack():
    def __init__(self):
        __floor = Element(None, None)
        self.__top_element = __floor

    def push(self, data: any) -> bool:
        '''
        Adds value to stack.
        '''
        # try:
        #     self.stack.append(value)
        #     return True
        # except:
        #     return False
        
        newElement = Element(data, self.__top_element)
        self.__top_element = newElement
        
        return

    def pop(self):
        '''
        Pops and returns value from stack. Returns None if stack empty
        '''
        elementRemoved = self.__top_element
        self.__top_element = elementRemoved.previous_element()
        del elementRemoved
        return elementRemoved.view_element()

    def dump(self):
        pass

    def top(self):
        return 

    def is_empty(self):
        return 
    
    def is_full(self):
        return not self.is_empty()
    


    # 'peeks' the entire stack and returns generator
    def __str__(self):
        pass


if __name__ == "__main__":
    s = Stack()


    s.push(5)

    # Print all known elements
    import gc
    for obj in gc.get_objects():
        if isinstance(obj, Element):
            print(obj)