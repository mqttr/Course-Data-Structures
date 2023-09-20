#Name:  Matthew Roland
#ID:    98210287
#Email: mroland@unomaha.edu     
import random


class Element():
    def __init__(self, data: any, prev):
        self.__data = data
        self.__prev = prev

    def view_element(self):
        return self.__data
    
    def previous_element(self):
        return self.__prev

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

    #############   INTERNAL UTILITY FUNCTIONS   #############
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

    def _find_node_max(self) -> Node:
        """
        Returns the maximum value in the list
        """
        max = self.head
        node: Node
        for _,node,_ in self._get_nodes():
            if max.data < node.data:
                max = node

        return max  

    def _find_node_min(self) -> Node:
        """
        Returns the node with the minimum value in the list
        """
        min = self.head
        node: Node
        for _,node,_ in self._get_nodes():
            if min.data > node.data:
                min = node

        return min

    def _get_node_by_index(self, index: int) -> ((int, bool), (None | Node, Node, None | Node )):
        previousNode: Node = None
        currentNode: Node = None
        futureNode: Node = None

        if index < 0: # Standard negative indexing, if abs(index) greater than len(list) then add to end of list
            length = self.length()
            index = index + length

        genList = enumerate(self._get_nodes())
        for i, nodes in genList:
            previousNode, currentNode, futureNode = nodes
            if i == index:
                return ((index, True), (previousNode, currentNode, futureNode))

        return ((index, False), (previousNode, currentNode, futureNode))

    def _get_node_by_node(self, searchNode: Node):
        """
        Get a node and its aspects from the node object. Returns ((Node Index, in file: bool, ), (previous Node, current node, next node)) 
        """
        previousNode: Node = None
        currentNode: Node = None
        nextNode: Node = None

        genList = enumerate(self._get_nodes())
        for i, nodes in genList:
            previousNode, currentNode, nextNode = nodes
            if currentNode == searchNode:
                return ((i, True), (previousNode, currentNode, nextNode))

        return ((self.length(), False), (previousNode, currentNode, nextNode))

    def _remove_node(self, node: Node):
        listDetails, nodeDetails = l._get_node_by_node(node)
        newNodeIndex, inList = listDetails
        previousNode, currentNode, nextNode = nodeDetails

        if not inList: # Not in list -> therefore cannot be removed
            return False

        if previousNode == None:
            self.head = nextNode
            return True
        else:
            previousNode.next = nextNode
            return True

    def _add_node(self, newNode: Node, index=-1):
        """
        Adds a node to at the param index in the list, if the index is negative > length of the list, adds to end of list.

        :param value: integer value of the node
        :param index: default = -1, index of the new node, acceptes negative or positive values
        """
        newNodeIndex: int = 0
        newNode.next = None

        previousNode: Node
        currentNode: Node
        nextNode: Node

        if self.length() == 0 : # if Linked list is empty
            self.head = newNode
            newNode.next = None
            return newNodeIndex
        
        if index < 0: # Standard negative indexing, if abs(index) greater than len(list) then add to end of list
            index = index + self.length() + 1

        listDetails, nodeDetails = l._get_node_by_index(index)
        newNodeIndex, inList = listDetails
        previousNode, currentNode, nextNode = nodeDetails

        # print(i, previousNode, currentNode, futureNode)
        if not inList: # Place after the element at index ( At the end of the list )
            currentNode.next = newNode
            newNode.next = nextNode
            # newNodeIndex+=1
        else: # Place before the element at index ( In the list )
            if previousNode == None: 
                self.head = newNode
                newNode.next = currentNode
            else:
                previousNode.next = newNode
                newNode.next = currentNode
        
        return newNodeIndex

    #############   EXTERNAL USE FUNCTIONS   #############
    def length(self) -> int:
        """
        Returns the length of the list
        """
        return sum(1 for _ in self._get_nodes())

    def remove(self, index: int) -> bool:
        """
        Removes an object in the list by index, returns True if succeeds, else False if failure
        :param index: Int of the index of the node to be removed
        """
        inList: bool
        currentNode: Node

        ((_, inList), (previousNode, currentNode, nextNode)) = self._get_node_by_index(index)

        return self._remove_node(currentNode)
    
    def findMax(self) -> float | int:
        """
        Returns the maximum value in the list
        """
        maxNode = self._find_node_max()
        return maxNode.data
    
    def findMin(self) -> float | int:
        """
        Returns the minimum value in the list
        """
        minNode = self._find_node_min()
        return minNode.data

    def add(self, value: int | float, index=-1) -> int:
        """
        Adds a node to at the param index in the list, if the index is negative > length of the list, adds to end of list.

        :param value: integer value of the node
        :param index: default = -1, index of the new node, acceptes negative or positive values
        """
        newNode: Node = Node(value)

        newNodeIndex: int = self._add_node(newNode, index)

        return newNodeIndex


    def sortedAdd(self, value: int | float) -> bool:
        """
        Adds and sorts new Value; when adding a lot of values at once, it is recommended to use add() then sort().
        :param value: Value of the new node
        """
        try:
            self.add(value)
            self.sort() 
            return True
        except Exception:
            return False

    def sort(self) -> bool:
        """
        Sorts list by adding max of list to stack then dumping stack
        """
        try:
            s = Stack()
            node: Node

            for i in range(self.length()):
                maxNode = self._find_node_max()
                s.push(maxNode)
                self._remove_node(maxNode)

            # input(f"DISPLAY LIST: {self.display()}")

            for node in s.dump():
                self._add_node(node)
            return True
        except Exception:
            return False

    def shuffle(self):
        s = Stack()
        node: Node

        while self.head:
            randomIndex = random.randint(0, self.length()-1)
            ((_, _), (previousNode, currentNode, nextNode)) = self._get_node_by_index(randomIndex)
            self._remove_node(currentNode)
            currentNode.next = None
            s.push(currentNode)

        for node in s.dump():
            self._add_node(node)



if __name__ == '__main__':
    ## instantiating the linked list
    l = LinkedList()

    import gc

    for x in range(25):
        l.add(x)


    l.add(-5, 5)
    l.add(-5, 5)
    l.add(99.5, 10)
    l.display()
    l.add(66, -4)
    l.display()

    s1 = Stack()
    print('\n\nNODE OBJECTS: ')
    for obj in gc.get_objects(): 
        if isinstance(obj, Node): # Print all Node objects
            print("Node Objects:", obj, obj.data)
            s1.push(obj)

    l.sort()
    l.display()
    l.shuffle()
    l.display()
    l.sort()
    l.display()
    l.shuffle()
    l.display()
    l.shuffle()
    l.display()
    l.sort()
    l.display()

    # print("Max:", l.findMax())
    # print("Min:", l.findMin())


    s2 = Stack()
    print('\n\nNODE OBJECTS: ')
    for obj in gc.get_objects(): 
        if isinstance(obj, Node): # Print all Node objects
            print("Node Objects:", obj, obj.data)
            s2.push(obj)

    for x in range(l.length()):
        if s1.pop() == s2.pop():
            print(x, end=' ')
        else:
            print("NOT THE SAME!!!", end=' ')

        
    for dump in s1.dump():
        print("HEY YOU MISSED SOME")

    for dump in s2.dump():
        print("HEY YOU MISSED SOME")

    print()