#Name:  Matthew Roland
#ID:    98210287
#Email: mroland@unomaha.edu     

# You are not allowed to modify this class
class Node:
    def __init__(self, data):
        ## data of the node
        self.data = data

        ## next pointer
        self.next = None

# You can modify this class as you want
class LinkedList:
    def __init__(self):
        ## initializing the head with None
        self.head = None
        self.n = 0

    def display(self):
        ## variable for iteration
        temp_node: Node = self.head

        ## iterating until we reach the end of the linked list
        while temp_node != None:
            ## printing the node data
            print(temp_node.data, end='->')

                ## moving to the next node
            temp_node = temp_node.next

            print('Null')

    ##############################################
    ## Implement functions belows
    ##############################################
    # add new node and sort the list
    # You can change the return values (from void to any) for each function as you want 
    # you can add functions as you want 

    def sortedAdd(self, value):
        newNode: Node = Node(value)
        self.add(value, index=1)

    def gen_nodes(self) -> tuple[Node | None, Node, Node | None]:
        '''
        Generates a tuple of ( PreviousNode (or None), currentNode, nextNode (or None) ).
        '''
        currentNode = self.head
        previousNode = currentNode
        while currentNode:          
            yield (previousNode, currentNode, currentNode.next)
            previousNode = currentNode
            currentNode = currentNode.next 
        
        return

    def remove(self, idx):
        try:
            pass
        except IndexError:
            return

    # find the maximum values in the list
    def findMax(self):
        # return max_value in the list
        for node in self.gen_nodes():
            pass

        return node.data

    # print linkedlist in a reversed order
    def printReversedList(self):
        s = Stack()

        for p,node,n in self.gen_nodes():
            print(f"NODE = {node}")
            s.push(node)

        for node in s.dump():
            print(node.data, end=' <- ')

        print("NULL")
     
    # Extra functions
    def add(self, value, index=-1) -> tuple[int, Node]:
        currentNode = None
        for i, (previousNode, currentNode, nextNode) in enumerate(self.gen_nodes()):
            if i == index:
                break
        
        insertNode = Node(value)
        if currentNode == None:
            self.head = insertNode
        elif nextNode == None:
            currentNode.next = insertNode
        else:
            previousNode.next = insertNode
            insertNode.next = currentNode      

        return (index, currentNode)

        

class Element():
    def __init__(self, data: any, prev):
        self.__data = data
        self.__prev = prev

    def view_element(self):
        return self.__data
    
    def previous_element(self):
        return self.__prev
    
    # def __str__(self):
    #     return str(self.__data)

class Stack():
    def __init__(self):
        __floor = Element(None, None)
        self.__top_element: Element = __floor

    def push(self, data: any) -> bool:
        '''
        Adds data to stack.
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
        value = self.__top_element.view_element()
        self.__top_element = self.__top_element.previous_element()
        return value

    def dump(self):
        '''
        Empties stack and returns generator of the stack
        '''
        while self.__top_element.previous_element():
            yield self.pop()
        return

    def top(self):
        return self.__top_element.view_element()

    def is_empty(self):
        if self.__top_element.previous_element() == None and self.__top_element.view_element() == None: 
            return True # Previous element is None 
        else: 
            return False # Previous element is not None (ie: floor)
    
    def is_full(self):
        return not self.is_empty()
    


    # Non-stack-esque functions
    def peek_stack(self):
        '''
        Seeks through the stack and returns a generator.
        '''
        ele = self.__top_element
        while ele.previous_element():
            yield ele.view_element()
            ele = ele.previous_element()
        
        return 

if __name__ == '__main__':
    ## instantiating the linked list
    l = LinkedList()

    l.add(5)
    l.add(10)
    l.add(15)
    l.add(3, index=1)
    for prev,current,nxt in l.gen_nodes():
        print("GEN_NODES:", current.data)

    l.printReversedList()

    # Your testcase will be here.
     # This is a testcase example.
    # l.sortedAdd(5)
    # l.sortedAdd(2)
    # l.sortedAdd(9)
    # l.sortedAdd(1)
    # l.sortedAdd(7)

    # print(l.findMax())


    # print('\n\n')
    import gc
    for obj in gc.get_objects(): 
        if isinstance(obj, Node): # Print all Node objects
            print("Node Objects:", obj.data)
    #################################