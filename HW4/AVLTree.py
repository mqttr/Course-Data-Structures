# Matthew Roland
# NUID: 98210287
# NETID: mroland

class AvlNode:
    def __init__(self, key: int) -> None:
        self.left: AvlNode | None = None
        self.right: AvlNode | None = None
        self.key: int = key
        self.height: int = 0

class AVLTree:
    def __init__(self):
        self.root = None

    def print_tree(self, key="key", left="left", right="right"):
        def display(root, key=key, left=left, right=right):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            # No child.
            if getattr(root, right) is None and getattr(root, left) is None:
                line = '%s' % getattr(root, key)
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child.
            if getattr(root, right) is None:
                lines, n, p, x = display(getattr(root, left))
                s = '%s' % getattr(root, key)
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if getattr(root, left) is None:
                lines, n, p, x = display(getattr(root, right))
                s = '%s' % getattr(root, key)
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = display(getattr(root, left))
            right, m, q, y = display(getattr(root, right))
            s = '%s' % getattr(root, key)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

        if self.root is None:
            print ("Tree is empty")
            return

        lines, *_ = display(self.root, key, left, right)
        for line in lines:
            print(line)

    ###########################################
    # You need to implement functions from here
    def isEmpty(self):
        if self.root is None:
            return True
        return False

    def insert(self, key):
        def __insert(key: int, node: AvlNode ) -> tuple[bool, AvlNode]:
            """
            Recursively inserts key into tree. Returns tuple[New Node Added: Bool, Node]
            """
            if node == None:
                return None
            
            # Add new node
            if key < node.key and node.left is None:
                new_node = AvlNode(key)
                node.left = new_node
                return (True, new_node)
            elif key > node.key and node.right is None:
                new_node = AvlNode(key)
                node.right = new_node
                return (True, new_node)
            elif key == node.key:
                return (False, node)

            # Traverse to child node
            results = []
            if key < node.key and node.left is not None:
                results.append(__insert(key, node.left))
            elif key > node.key and node.right is not None:
                results.append(__insert(key, node.right))

            for result in results:
                if not result == None:
                    return (True, result[1])    
                
            return (False, None)

        if type(key) is not int:
            return None
        if self.isEmpty():
            new_node = AvlNode(key)
            self.root = new_node
            return new_node

        result, new_node = __insert(key, self.root)

        if not result: # No new noded added, return node, no need to refactor
            return new_node

        self.balance_node(new_node)
        self.update_all_height()

        return result

    def balance_node(self, new_node: AvlNode) -> bool:
        if self.isEmpty():
            return True
        
        self.__balance_node(self.root.left, new_node)
        self.__balance_node(self.root.right, new_node)

        node = self.root

        if self.height_by_node(node.left) - self.height_by_node(node.right) in (-1, 0, 1):
            return
        
        if node.left is not None:
            if self.isChild(node.left.left, new_node): # LL
                self.root = self.rotate_with_left_child(node)
            elif self.isChild(node.left.right, new_node): #LR
                self.root = self.double_rotate_with_left_child(node)
        if node.right is not None:
            if self.isChild(node.right.right, new_node): #RR
                self.root = self.rotate_with_right_child(node)
            elif self.isChild(node.right.left, new_node): #RL
                self.root = self.double_rotate_with_right_child(node)

    def __balance_node(self, node: AvlNode, new_node: AvlNode) -> bool:
        if node == None:
            return

        self.__balance_node(node.left, new_node)
        self.__balance_node(node.right, new_node)

        if self.height_by_node(node.left) - self.height_by_node(node.right) in (-1, 0, 1):
            return
        
        # ROTATION TIME no you don't get any more comments
        parent = self.get_parent(node)
        if self.isChild(parent.left, new_node):
            if node.left is not None:
                if self.isChild(node.left.left, new_node): # LL
                    parent.left = self.rotate_with_left_child(node)
                elif self.isChild(node.left.right, new_node): #LR
                    parent.left = self.double_rotate_with_left_child(node)
            if node.right is not None:
                if self.isChild(node.right.right, new_node): #RR
                    parent.left = self.rotate_with_right_child(node)
                elif self.isChild(node.right.left, new_node): #RL
                    parent.left = self.double_rotate_with_right_child(node)        
        elif self.isChild(parent.right, new_node):
            if node.left is not None:
                if self.isChild(node.left.left, new_node): # LL
                    parent.right = self.rotate_with_left_child(node)
                elif self.isChild(node.left.right, new_node): #LR
                    parent.right = self.double_rotate_with_left_child(node)
            if node.right is not None:
                if self.isChild(node.right.right, new_node): #RR
                    parent.right = self.rotate_with_right_child(node)
                elif self.isChild(node.right.left, new_node): #RL
                    parent.right = self.double_rotate_with_right_child(node)

    def contains(self, key: int) -> bool:
        if type(key) is not int or self.isEmpty():
            return False

        node = self.root
        while True:
            if node is None:
                return False
            if node.key == key:
                return True
            
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right

    def height_by_node(self, node: AvlNode):
        if node == None or type(node) is not AvlNode:
            return -1
        else:
            return self.height(node.key)

    def height(self, key: int):
        """
        Returns height of node with key value of key, or -1 if not found.
        """
        def __height(node: AvlNode, height):
            if node == None:
                return height
            
            heightLeft = __height(node.left, height+1)
            heightRight = __height(node.right, height+1)

            return max(heightLeft, heightRight)
        

        if not self.contains(key) or self.isEmpty(): 
            return -1

        true_node: AvlNode
        node = self.root
        while True:
            if key < node.key:
                node = node.left
                continue
            if key > node.key:
                node = node.right
                continue
            if key == node.key:
                true_node = node
                break

        return __height(true_node, 0)-1

    def update_all_height(self, node: AvlNode | bool | None = True) -> None:
        """
        Updates the height attribute of all nodes in a tree, or subnodes of parameter node
        """
        if self.isEmpty(): return
        if node == True: 
            node: AvlNode = self.root
        elif node is None: 
            return

        node.height = self.height(node.key)
        self.update_all_height(node.left)
        self.update_all_height(node.right)

    def depth(self, key: int) -> int:
        """
        Returns depth of node with key value of key, returns -1 if not found.

        :return: Depth of node with key value of key, or -1
        """
        def __depth(node: AvlNode, key: int, depth: int) -> int | None:
            if node == None:
                return None

            results = []
            if key == node.key:
                return depth
            if key < node.key:
                results.append(__depth(node.left, key, depth+1))
            if key > node.key:
                results.append(__depth(node.right, key, depth+1))

            for result in results:
                if result is not None:
                    return result
                

        if self.isEmpty():
            return -1
        if not self.contains(key):
            return -1
        
        return __depth(self.root, key, 0)
        
    def findMin(self, node: AvlNode = None) -> int | None:
        """
        Find minimum value of tree or of child nodes
        """
        result = self.findMin_node(node)

        if type(result) is AvlNode:
            return result.key

    def findMax(self, node: AvlNode = None) -> int | None:
        """
        Find minimum value of tree or of child nodes
        """
        def __findMax(curr: AvlNode) -> int:
                    while curr.right:
                        curr = curr.right
                    return curr.key


        if self.isEmpty():
            return None
        
        if node is None or type(node) is not AvlNode:
            node = self.root
            return __findMax(node)
        else: 
            return __findMax(node)

    def compare(self, x, y):
        if x < y:
            return -1
        elif x > y:
            return 1
        else:
            return 0

    def rotate_with_left_child(self, k2: AvlNode) -> AvlNode:
        #LL rotation
        #Write your code here
        #You need to adjust return value
        k1 = k2.left
        k2.left = k1.right
        k1.right = k2
        k2.height = self.height(k2)
        k1.height = self.height(k1)
        return k1

    def rotate_with_right_child(self, k2: AvlNode) -> AvlNode:
        #RR rotation
        #Write your code here
        #You need to adjust return value
        k1 = k2.right
        k2.right = k1.left
        k1.left = k2
        k2.height = self.height(k2)
        k1.height = self.height(k1)
        return k1

    def double_rotate_with_left_child(self, k3: AvlNode) -> AvlNode:
        # LR rotation
        #Write your code here
        #You need to adjust return value
        k3.left = self.rotate_with_right_child(k3.left)
        return self.rotate_with_left_child(k3)

    def double_rotate_with_right_child(self, k3: AvlNode) -> AvlNode:
        """
        RL rotation 
        """
        # RL rotation
        #Write your code here
        #You need to adjust return value
        k3.right = self.rotate_with_left_child(k3.right)
        return self.rotate_with_right_child(k3)


    def findMin_node(self, node: AvlNode = None) -> AvlNode | None:
        if self.isEmpty(): return None

        if node is None or type(node) is not AvlNode:
            node = self.root

        while node.left:
            node = node.left
        return node

    def get_node(self, key: int) -> AvlNode:
        if self.isEmpty(): return

        nodes = self.get_nodes()
        node: AvlNode
        for node in nodes:
            if node.key == key:
                return node

    def get_nodes(self) -> AvlNode:
        def __get_nodes(node: AvlNode, nodes: list) -> list[ AvlNode ]:
            if node == None:
                return
            
            __get_nodes(node.left, nodes)
            nodes.append(node)
            __get_nodes(node.right, nodes)

            return nodes

        if self.isEmpty():
            return None

        return __get_nodes(self.root, [])

    def isChild(self, parent_node: AvlNode, child_node: AvlNode) -> bool:
        if parent_node is None or child_node is None:
            return False
        
        if parent_node == child_node:
            return True
        
        results = []
        results.append(self.isChild(parent_node.left, child_node))
        results.append(self.isChild(parent_node.right, child_node))

        for result in results:
            if result is True:
                return True
        return False

    def get_parent(self, child_node: AvlNode, current_node: AvlNode = False) -> AvlNode | bool:
        """
        Gets parent of node, returns parent node, False if not found or tree is empty, Returns True if child_node is root
        """
        if self.isEmpty() or child_node is None or current_node is None:
            return False
        
        if child_node == self.root:
            return True
        
        if current_node is False:
            current_node = self.root

        if current_node.left == child_node or current_node.right == child_node:
            return current_node
        
        results = []
        results.append(self.get_parent(child_node, current_node.left))
        results.append(self.get_parent(child_node, current_node.right))
        for result in results:
            if type(result) is AvlNode:
                return result


class Menu:
    def __init__(self, tree: AVLTree):
        self.tree: AVLTree = tree

    def __int_input(self, msg: str) -> int | None:
        while True:
            usr_input = input(msg).strip().replace(" ", "")
            try: 
                return int(usr_input)
            except:
                print("Only integer keys are allowed.")

            if usr_input == "":
                print("Blank input returning to main menu...")
                return

    def print_menu(self): # 0 
        print(
            "------------ AVL Tree ------------",
            "0. Show menu",
            "1. Insert a new key",
            "2. Check if a key exists",
            "3. Find the node's height",
            "4. Find the node's depth",
            "5. Find the min value",
            "6. Find the max value",
            "7. Print tree",
            "8. Exit",
            "9. Delete an existing key",
            sep='\n'
        )

    def insert(self): # 1
        key = self.__int_input("Input a new key: ")
        if key == None: return  

        if self.tree.contains(key):
            print(f"{key} already exists in the tree.")
            return
        
        self.tree.insert(key)
        print(f"{key} is added to the tree.")

    def exists(self): # 2
        key = self.__int_input("Check to see if a key is in the tree: ")
        if key == None: return

        if self.tree.contains(key):
            print(f"{key} exists in the tree.")
        else:
            print(f"{key} does not exist in the tree.")

    def height(self): # 3
        key = self.__int_input("Key to get the height of node: ")
        if key == None: return  

        if not self.tree.contains(key):
            print(f"{key} does not exist in the tree.")

        print(f"{key}'s height is {self.tree.height(key)}.")

    def depth(self): # 4
        key = self.__int_input("Key to get the height of node: ")
        if key == None: return  

        if not self.tree.contains(key):
            print(f"{key} does not exist in the tree.")

        print(f"{key}'s depth is {self.tree.depth(key)}.")

    def min(self): # 5
        if self.tree.isEmpty():
            print("The tree is empty.")
            return
        print(f"{self.tree.findMin()} is the minimum value of the tree.")

    def max(self): # 6

        if self.tree.isEmpty():
            print("The tree is empty.")
            return
        print(f"{self.tree.findMax()} is the maximum value in the tree.")

    def print_tree(self): # 7
        self.tree.print_tree()

    def exit(self): # 8
        print("Final tree:")
        self.print_tree()
        print("Exiting...")
        exit(0)


def main():
    tree = AVLTree()

    for x in range(10):
        tree.insert(x)

    menu = Menu(tree)
    menu.print_menu()
    while True:
        usr_input = input().strip()
        print()
        match usr_input:
            case "0":
                menu.print_menu()
            case "1":
                menu.insert()
            case "2":
                menu.exists()
            case "3":
                menu.height()  
            case "4":
                menu.depth()
            case "5":
                menu.min()
            case "6":
                menu.max()
            case "7":
                menu.print_tree()  
            case "8":
                menu.exit()
            case "":
                pass
            case _:
                print("Unknown command; use 0 to see options.")


if __name__ == '__main__':
    main()