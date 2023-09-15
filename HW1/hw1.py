#Name:  Matthew Roland
#ID:    98210287
#Email: mroland@unomaha.edu     

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

    def sortedAdd(self, value: int | float):
        pass
            

    def remove(self, idx):
        pass

    def findMax(self):
        max = self.head
        for prev,node,nxt in self.get_nodes():
            if max < node.data:
                max = node.data

        return max

    # print linkedlist in a reversed order
    def printReversedList(self):
        s = Stack()

        for p,node,n in self.get_nodes():
            print(f"NODE = {node}")
            s.push(node)

        for node in s.dump():
            print(node.data, end=' <- ')

        print("HEAD")
     
    # Extra functions
    def add(self, value: int, index=-1) -> tuple[int, Node]:
        newNodeIndex: int = 0
        newNode: Node = Node(value)

        if sum(1 for node in self.get_nodes()) == 0 :
            self.head = newNode
            return newNodeIndex
        
        

        return newNodeIndex

    def get_nodes(self) -> tuple[Node | None, Node, Node | None]:
        '''
        Generates a tuple of ( PreviousNode (or None), currentNode, nextNode (or None) ).
        '''
        previousNode: Node = None
        currentNode: Node = self.head
        while currentNode:
            yield (previousNode, currentNode, currentNode.next)
            previousNode = currentNode
            currentNode = currentNode.next 

if __name__ == '__main__':
    ## instantiating the linked list
    l = LinkedList()

    n1 = Node(999)
    n2 = Node(998)
    l.head = n1
    n1.next = n2

    # l.display()
    l.add(1)
    # l.display()
    # l.add(5)



    # for prev,current,nxt in l.get_nodes():
    #     print("GEN_NODES:", current.data)


    # Your testcase will be here.
     # This is a testcase example.
    # l.sortedAdd(5)
    # l.sortedAdd(2)
    # l.sortedAdd(9)
    # l.sortedAdd(1)
    # l.sortedAdd(7)

    # print(l.findMax())


    print('\n\n')
    import gc
    for obj in gc.get_objects(): 
        if isinstance(obj, Node): # Print all Node objects
            print("Node Objects:", obj, obj.data)
    #################################