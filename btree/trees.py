class Node():
    def __init__(self, key):
        self.key = key
        self.left: Node = None
        self.right: Node = None

class BinaryTree():
    def __init__(self):
        self.root: Node = None

    def insert(self, key: int):
        if not self.root:
            self.root = Node(key)
            return self.root
        
        nodes = self.get_all_nodes()

        node: Node
        for node in nodes:
            if node.key == key:
                return node
            
        
        shallowestAdoptingNode = self.get_shallowest_node(self.get_adopting_nodes())

        # print("shallowestAdoptingNode", shallowestAdoptingNode.key, end=' ')

        if shallowestAdoptingNode:
            newNode = Node(key)
            if shallowestAdoptingNode.left == None:
                shallowestAdoptingNode.left = newNode
                return newNode
            if shallowestAdoptingNode.right == None:
                shallowestAdoptingNode.right = newNode
                return newNode


        return False


    # def __insert(node: Node, key):    :(
    #     if not node.left: 
    #         node.left = Node(key)
    #         return node.left
    #     if not node.right:
    #         node.right = Node(key)
    #         return node.right
        
    #     result = BinaryTree.__insert(node.left, key)
    #     if result:
    #         return result
    #     result = BinaryTree.__insert(node.right, key)
    #     if result:
    #         return result


    def delete(self, id: int | Node):
        if not type(id) == Node:
            deleteNode: Node = self.get_node(id)
        else:
            deleteNode: Node = id

        if deleteNode == None:
            return True
        
        parent = self.get_parent(deleteNode)
        if parent == None: 
            if (deleteNode.left == None):
                self.root = deleteNode.right
                return True
            elif (deleteNode.right == None):
                self.root = deleteNode.left
                return True
            else:
                switchingNode = deleteNode.right
                while switchingNode.left:
                    switchingNode = switchingNode.left
                self.swap(deleteNode, switchingNode)
                self.delete(deleteNode)
                return True
                
        if (deleteNode.left == None) or (deleteNode.right == None):
            if parent.left == deleteNode:
                if deleteNode.left == None:
                    parent.left = deleteNode.right
                else:
                    parent.left = deleteNode.left
            if parent.right == deleteNode:
                if deleteNode.left == None:
                    parent.right = deleteNode.right
                else:
                    parent.right = deleteNode.left
            return True
        else:
            switchingNode = deleteNode.right
            while switchingNode.left:
                switchingNode = switchingNode.left
            self.swap(deleteNode, switchingNode)
            self.delete(deleteNode)
            return True
        
    def swap(self, first: Node | int, second: Node | int) -> bool:
        if not type(first) == Node:
            first = self.get_node(first)
        if not type(second) == Node:
            second = self.get_node(second)
        
        if not (type(first) == Node and type(second) == Node):
            return False
        
        firstParent = self.get_parent(first)
        secondParent = self.get_parent(second)

        firstLeft = first.left
        firstRight = first.right

        secondLeft = second.left
        secondRight = second.right
        
        first.left = secondLeft
        first.right = secondRight

        second.left = firstLeft
        second.right = firstRight

        if (firstParent.left, secondParent.left) == (first, second):
            firstParent.left = second
            secondParent.left = first
        if (firstParent.right, secondParent.left) == (first, second):
            firstParent.right = second
            secondParent.left = first
        if (firstParent.left, secondParent.right) == (first, second):
            firstParent.left = second
            secondParent.right = first
        if (firstParent.right, secondParent.right) == (first, second):
            firstParent.right = second
            secondParent.right = first

        return True

        
    def get_height(self, key: int):
        node = self.get_node(key)

        if node == None:
            return None

        return BinaryTree.__get_height(node, 0)-1

    def __get_height(node: Node, height):
        if node == None:
            return height
        
        heightLeft = BinaryTree.__get_height(node.left, height+1)
        heightRight = BinaryTree.__get_height(node.right, height+1)

        return max(heightLeft, heightRight)

    def get_node(self, key: int) -> Node | None:
        for node in self.get_all_nodes():
            if node.key == key:
                return node
        return None

    def get_parent(self, child: Node | int) -> Node | None:
        if not type(child) == Node:
            child = self.get_node(child)

        for parent in self.get_all_nodes():
            if parent.left == child or parent.right == child:
                return parent
            
        return None

    def get_depth(self, key: int) -> int | None:
        if self.root == None:
            return None
        
        node = self.get_node(key)

        if not node == None:
            return BinaryTree.__get_depth(self.root, node, 0)
        else:
            return None

    def print_nodes(self):
        for node in b.get_all_nodes():
            print(node.key, end=' ')
            if node.left:
                print(node.left.key, end=' ')
            else: 
                print('None', end=' ')
            if node.right:
                print(node.right.key, end=' ')
            else:
                print('None', end=' ')
            print()

    def get_shallowest_node(self, *args: list[Node]) -> Node | None:
        nodes = []
        if args:
            nodes = args[0]
        else:
            nodes = self.get_all_nodes()

        depths = []
        node: Node
        for node in nodes:
            depths.append( (node, self.get_depth(node.key)) )

        minimum = min(depths, key = lambda t: t[1])

        if depths:
            return minimum[0]
        else:
            return None

    def get_deepest_node(self, *args: list[Node]) -> Node | None:
        nodes = []
        if args:
            nodes = args[0]
        else:
            nodes = self.get_all_nodes()

        depths = []
        node: Node
        for node in nodes:
            depths.append( (node, self.get_depth(node.key)) )

        maximum = max(depths, key = lambda t: t[1])

        if depths:
            return maximum[0]
        else:
            return None

    def __get_depth(node: Node, findNode: int, depth: int) -> int | None:
        if node == findNode:
            return depth
        if node == None:
            return 0

        result = BinaryTree.__get_depth(node.left, findNode, depth+1)
        if result: return result
        result = BinaryTree.__get_depth(node.right, findNode, depth+1)
        if result: return result

    def get_all_leaves(self) -> list[Node]:
        leaves = []

        nodes = self.get_all_nodes()

        node: Node
        for node in nodes:
            if not (node.left or node.right):
                leaves.append(node)
        
        return leaves
        
    def get_adopting_nodes(self) -> list[Node]:
        adoptingNodes = []
        nodes = self.get_all_nodes()

        node: Node
        for node in nodes:
            if node.left == None or node.right == None:
                adoptingNodes.append(node)

        return adoptingNodes

    def get_all_nodes(self) -> list[Node]:
        nodes = []

        if self.root == None:
            return nodes
        
        nodes = BinaryTree.__get_all_nodes(self.root, nodes)
        return nodes
        
    def __get_all_nodes(node: Node, nodes: list) -> list[Node]:
        if node == None:
            return nodes
        
        BinaryTree.__get_all_nodes(node.left, nodes)
        BinaryTree.__get_all_nodes(node.right, nodes)
        nodes.append(node)

        return nodes

    # ------------------------ PRINTING TREES ------------------------

    def in_order(self) -> None: 
        BinaryTree.__in_order(self.root)
        print()
    def pre_order(self) -> None: 
        BinaryTree.__pre_order(self.root)
        print()
    def post_order(self) -> None: 
        BinaryTree.__post_order(self.root)
        print()


    def __in_order(node: Node) -> None:
        if node == None: return    

        BinaryTree.__in_order(node.left)
        print(node.key, end=' ')

        BinaryTree.__in_order(node.right)

    def __pre_order(node: Node) -> None:
        if node == None: return

        print(node.key, end=' ')
        BinaryTree.__pre_order(node.left)
        BinaryTree.__pre_order(node.right)

    def __post_order(node: Node) -> None:
        if node == None: return

        BinaryTree.__post_order(node.left)
        BinaryTree.__post_order(node.right)
        print(node.key, end=' ')


class BST(BinaryTree):
    def __init__(self):
        self.root: Node = None

    def insert(self, key: int):
        if self.root == None: 
            self.root = Node(key)
            return self.root
        
        k = Node(key) # Will be cleaned up by garbage collector if unused
        n = self.root

        while True:
            if n.key == key:
                return n
            if key < n.key:
                if n.left: 
                    n=n.left
                    continue
                else:
                    n.left = k
                    return k
            elif key > n.key:
                if n.right: 
                    n=n.right
                    continue
                else:
                    n.right = k
                    return k
                

if __name__ == "__main__":
    b = BinaryTree()
    b.insert(8)
    b.insert(4)
    b.insert(16)
    # b.insert(2)
    # b.insert(6)
    # b.insert(18)
    # b.insert(20)
    # b.insert(1)

    for x in b.get_all_nodes():
        print(x.key, end=' ')
        if x.left:
            print(x.left.key, end=' ')
        else: 
            print('None', end=' ')
        if x.right:
            print(x.right.key, end=' ')
        else:
            print('None', end=' ')
        print()

    b.delete(8)
    print()
    for x in b.get_all_nodes():
        print(x.key, end=' ')
        if x.left:
            print(x.left.key, end=' ')
        else: 
            print('None', end=' ')
        if x.right:
            print(x.right.key, end=' ')
        else:
            print('None', end=' ')
        print()


    # print(b.get_deepest_node(b.get_all_leaves()).key)

    # import gc
    # for obj in gc.get_objects():
    #     if isinstance(obj, Node):
    #         if obj.key: print(obj.key, end=' ')
    #         if obj.left: print(obj.left.key, end=' ')
    #         if obj.right: print(obj.right.key, end=' ')
    #         print()