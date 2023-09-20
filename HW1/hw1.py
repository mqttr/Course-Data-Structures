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

    #############   PRINTING FUNCTIONS  #############
    def display(self) -> None:
        '''
        Given function, iterates through the list and prints the list's data
        '''
        ## variable for iteration
        temp_node: Node = self.head

        ## iterating until we reach the end of the linked list
        while temp_node != None:
            ## printing the node data
            print(temp_node.data, end='->')

                ## moving to the next node
            temp_node = temp_node.next

        print('Null')

    def printReversedList(self) -> None:
        '''
        Display list from tail to head using a stack
        '''
        s = Stack()
        node: Node

        for _,node,_ in self._get_nodes():
            s.push(node)

        for node in s.dump():
            print(node.data, end='<-')

        print("HEAD")

    #############   Internal utlity functions   #############
    def _get_nodes(self) -> tuple[Node | None, Node, Node | None]:
        '''
        Generates a tuple of ( PreviousNode (or None), currentNode, nextNode (or None) ).
        '''
        previousNode: Node = None
        currentNode: Node = self.head
        while currentNode:
            yield (previousNode, currentNode, currentNode.next)
            previousNode = currentNode
            currentNode = currentNode.next       

    def length(self):
        return sum(1 for _ in self._get_nodes())

    def remove(self, index) -> bool:
        previousNode: Node
        nextNode: Node

        ((_, inList), (previousNode, _, nextNode)) = self._get_node_at_index(index)

        if not inList:
            return False

        if previousNode == None:
            self.head = nextNode
            return True
        else:
            previousNode.next = nextNode
            return True
    

    def findMax(self):
        """
        Returns the maximum value in the list
        """
        max = self.head
        node: Node
        for _,node,_ in self._get_nodes():
            if max.data < node.data:
                max = node

        return max.data
    
    def findMin(self):
        """
        Returns the minimum value in the list
        """
        min = self.head
        node: Node
        for _,node,_ in self._get_nodes():
            if min.data > node.data:
                min = node

        return min.data
     
    def _get_node_at_index(self, index):
        previousNode: Node
        currentNode: Node
        futureNode: Node

        if index < 0: # Standard negative indexing, if abs(index) greater than len(list) then add to end of list
            length = self.length()
            index = index + length

        genList = enumerate(self._get_nodes())
        for i, nodes in genList:
            previousNode, currentNode, futureNode = nodes
            if i == index:
                return ((index, True), (previousNode, currentNode, futureNode))

        return ((index, False), (previousNode, currentNode, futureNode))

    def add(self, value: int, index=-1) -> int:
        """
        Adds a node to at the param index in the list, if the index is negative > length of the list, adds to end of list.

        :param value: integer value of the node
        :param index: default = -1, index of the new node, acceptes negative or positive values
        """
        newNodeIndex: int = 0
        
        newNode: Node = Node(value)
        previousNode: Node
        currentNode: Node
        futureNode: Node

        if self.length() == 0 : # if Linked list is empty
            self.head = newNode
            return newNodeIndex
        
        if index < 0: # Standard negative indexing, if abs(index) greater than len(list) then add to end of list
            index = index + self.length() + 1

        listDetails, nodeDetails = l._get_node_at_index(index)
        newNodeIndex, inList = listDetails
        previousNode, currentNode, futureNode = nodeDetails

        # print(i, previousNode, currentNode, futureNode)
        if not inList: # Place after the element at index ( At the end of the list )
            currentNode.next = newNode
            newNode.next = futureNode
            # newNodeIndex+=1
        else: # Place before the element at index ( In the list )
            if previousNode == None: 
                self.head = newNode
                newNode.next = currentNode
            else:
                previousNode.next = newNode
                newNode.next = currentNode
        
        return newNodeIndex

    def sortedAdd(self, value: int | float):
        pass   

    def sort(self):
        pass

if __name__ == '__main__':
    ## instantiating the linked list
    l = LinkedList()

    for x in range(15):
        l.add(x)

    # l.add(-5, 5)
    # l.add(99, 10)
    # l.add(66, -4)

    l.display()

    print(f"Removed {l.remove(3)}")
    print(f"Removed {l.remove(0)}")
    print(f"Removed {l.remove(5)}")


    l.display()
    
    # for prev,current,nxt in l.get_nodes():
    #     print("GEN_NODES:", current.data)

    # l.sortedAdd(5)
    # l.sortedAdd(2)
    # l.sortedAdd(9)
    # l.sortedAdd(1)
    # l.sortedAdd(7)

    # print("Max:", l.findMax())
    # print("Min:", l.findMin())



    # print('\n\nNODE OBJECTS: ')
    # import gc
    # for obj in gc.get_objects(): 
    #     if isinstance(obj, Node): # Print all Node objects
    #         print("Node Objects:", obj, obj.data)