#Name: Matthew Roland
#ID: 98210287
#Email: mroland@unomaha.edu

import re

# ===================================================================================================================================
# ============================================                                           ============================================
# ============================================              MAIN STACK CODE              ============================================
# ============================================                                           ============================================
# ===================================================================================================================================

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
        if value == None:
            raise IndexError("Stack is empty")
        self.__top_element = self.__top_element.previous_element()
        return value

    def dump(self):
        '''
        Empties stack and returns a generator of the stack
        '''
        while self.__top_element.previous_element():
            yield self.pop()
        return

    def burn(self):
        '''
        Just empties stack, Call when just to empty stack
        '''
        while self.__top_element.previous_element():
            self.pop()

    def top(self):
        return self.__top_element.view_element()

    def is_empty(self):
        '''
        Returns True if stack is empty, false otherwise.
        '''
        if self.__top_element.previous_element() == None and self.__top_element.view_element() == None: 
            return True # Previous element is None 
        else: 
            return False # Previous element is not None (ie: floor)
    
    def is_full(self):
        '''
        Returns True if stack is full, false otherwise.
        '''
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


# ===================================================================================================================================
# ============================================                                           ============================================
# ============================================           MAIN CALCULATOR CODE            ============================================
# ============================================                                           ============================================
# ===================================================================================================================================

class Calculator:
    def __init__(self):
        self.primaryStack = Stack()
        self.secondaryStack = Stack()

    def convert(self, infixStr: str) -> list | str:
        '''
        Converts infix to postfix, returns list of postfix to keep multi length numbers
        :param infixStr: Standard mathematical writing style
        :return: Error message or postfix list
        '''
        # ============================================ Setup ============================================
        
        # use a stack to covert infix to postfix
        self.primaryStack.burn()
        self.secondaryStack.burn()
        
        postfix = [] # output
        
        # ============================================ Precleaning infix ============================================

        infixStr = infixStr.strip().replace(' ', '')
        
        if infixStr == '':
            return "Invalid Input: Input is empty"
        
        # Checking for balanced ()
        try:
            for char in infixStr:
                if char == "(":
                    self.primaryStack.push(char)
                elif char == ")":
                    self.primaryStack.pop()
        except IndexError:  
            self.primaryStack.burn()
            self.secondaryStack.burn()
            return "Invalid Input: Unbalanced Parentheses: Too many )"
        finally: 
            # Checking for leftover ()
            if self.primaryStack.is_full():
                self.primaryStack.burn()
                self.secondaryStack.burn()
                return "Invalid Input: Unbalanced Parentheses: Too few )"

            
        if infixStr[0] == "-":
            infixStr = "0" + infixStr
            
        
        infixStr = infixStr.replace('+-', '-')
        infixStr = infixStr.replace('-+', '-')
        infixStr = infixStr.replace('++', '+')    
            
        infixStr = re.sub(r"-(-\d+?)", "-(\g<1>)", infixStr)        # ...--...  -> ...-(-...)...

        infixStr = re.sub(r"\((-\d+?)", "((0\g<1>)", infixStr)      # ...(-x... -> ...((0-x)...
        
        infixStr = re.sub(r"(\d+?)\(", "\g<1>*(", infixStr)         # ...y(x... -> ...y*(x...
        
        infixStr = re.sub(r"\)(\d+?)", ")*\g<1>", infixStr)         # ...y)x... -> ...y)*x...
        
        infixStr = re.sub(r"\)\(", ")*(", infixStr)                 # ...)(...  -> ...)*(...
        

        for i, char in enumerate(infixStr):   
            if char == "0" or char == "1" \
                    or char == "2" or char == "3" \
                    or char == "4" or char == "5" \
                    or char == "6" or char == "7" \
                    or char == "8" or char == "9": 
                try:
                    if infixStr[i+1] == "(":
                        return f"Error: Put * between {char} and ("
                except IndexError:
                    pass
            elif char == ")":
                try:
                    if infixStr[i+1] == "0" or infixStr[i+1] == "1" \
                        or infixStr[i+1] == "2" or infixStr[i+1] == "3" \
                        or infixStr[i+1] == "4" or infixStr[i+1] == "5" \
                        or infixStr[i+1] == "6" or infixStr[i+1] == "7" \
                        or infixStr[i+1] == "8" or infixStr[i+1] == "9": 
                            return f"Error: Put * between ) and {char} "
                except IndexError:
                    break
            elif char == "(":
                try:
                    if infixStr[i+1] == "-":
                            return f"Error: Put 0 before -{infixStr[i+2]} as it is after a ("
                except IndexError:
                    break
                
            
        # ============================================ Preparing for infix to postfix ============================================
        # Creates proper stack with sparated operators and values are multiple 
        
        for char in infixStr:
            self.primaryStack.push(char)
        
        self.secondaryStack.burn()
        for char in self.primaryStack.dump():
            if char == "(" or char == ")" or char == "^" \
                        or char == "*" or char == "/" \
                        or char == "+" or char == "-":
                self.secondaryStack.push(char)
            elif char == "0" or char == "1" \
                        or char == "2" or char == "3" \
                        or char == "4" or char == "5" \
                        or char == "6" or char == "7" \
                        or char == "8" or char == "9": 
                if self.secondaryStack.is_full():
                    if "0" in self.secondaryStack.top() or "1" in self.secondaryStack.top() \
                            or "2" in self.secondaryStack.top() or "3" in self.secondaryStack.top() \
                            or "4" in self.secondaryStack.top() or "5" in self.secondaryStack.top() \
                            or "6" in self.secondaryStack.top() or "7" in self.secondaryStack.top() \
                            or "8" in self.secondaryStack.top() or "9" in self.secondaryStack.top(): 
                        self.secondaryStack.push(char + self.secondaryStack.pop())
                    else:
                        self.secondaryStack.push(char)
                else:
                    self.secondaryStack.push(char)
            else:
                self.primaryStack.burn()
                self.secondaryStack.burn()
                return f"Invalid Input: {char}"
            

        # print( [ x for x in self.secondaryStack.peek_stack()] )


        # ============================================ Infix to Postfix ============================================
        char: str
        for char in self.secondaryStack.dump():
            if "0" in char or "1" in char \
                    or "2" in char or "3" in char or "4" in char \
                    or "5" in char or "6" in char or "7" in char \
                    or "8" in char or "9" in char:         
            # if char == "0" or char == "1" \
            #             or char == "2" or char == "3" \
            #             or char == "4" or char == "5" \
            #             or char == "6" or char == "7" \
            #             or char == "8" or char == "9":
                postfix.append(char)
            elif char == "(": 
                self.primaryStack.push(char)
            elif char == ")":
                while self.primaryStack.top() != "(":
                    postfix.append(self.primaryStack.pop())
                self.primaryStack.pop() # removes the remaining (
            elif char == "^": 
                self.primaryStack.push(char)
            elif char == "*" or char == "/":
                while self.primaryStack.top() == "*" or self.primaryStack.top() == "/" or self.primaryStack.top() == "^":
                    postfix.append(self.primaryStack.pop())
                self.primaryStack.push(char)
            elif char == "+" or char == "-":
                while self.primaryStack.top() == "*" or self.primaryStack.top() == "/" or self.primaryStack.top() == "^" \
                        or self.primaryStack.top() == "+" or self.primaryStack.top() == "-": 
                    postfix.append(self.primaryStack.pop())
                self.primaryStack.push(char)
            else: 
                self.primaryStack.burn()
                self.secondaryStack.burn()
                return f"Invalid Input: {char} Allowed Inputs: 0-9, *, /, +, -, (, ), ^"

        for char in self.primaryStack.dump():
            postfix.append(char)

        self.primaryStack.burn()
        self.secondaryStack.burn()
        return postfix
    
        # You are not allowed to add additional functions e.g., precedence(), isOperator(), etc.
        # You are not allowed to create variables using a list or a dictionary like below. 
        #    priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        #    operators = ['(', ')', '-', '+', '*', '/', '^']
        # Keep the pseudo code (for loops) below with your code.
        # for c in infix:
        #     if c == ‘(’ stack.push(c)
        #     else if c == ‘)’
        #         while stack.isEmpty() == false && stack.peek() != ‘(‘
        #             poped_char = stack.pop() and postfix.append(poped_char)
        #     else if c == ‘+’ || c == ‘-’
        #         while stack.isEmpty() == false && stack.peek() == ‘/’ || ‘*’ || ‘+’ || ‘-’
        #             poped_char = stack.pop() and postfix.append(poped_char)
        #     else if c == ‘/’ || c == ‘*’
        #         while stack.isEmpty() == false && stack.peek() == ‘/’ || ‘*’
        #             poped_char = stack.pop() and postfix.append(poped_char)
        #     else
        #         stack.push(c)

        # while stack.isEmpty() == false
        #     poped_char = stack.pop() and postfix.append(poped_char)

        # return postfix

    # This Return double for division
    def evaluate(self, postfix: list) -> float | int:
        '''
        Returns the calculated value based off of the postfix provided. Float if division is used otherwise int .
        :param postfix: List of postfix values to keep values of more than 1 char in length
        '''
        # ============================================ Setup ============================================
        
        #Use stack of tokens
        self.primaryStack.burn()
        self.secondaryStack.burn()
        
        # ============================================ Fixing ============================================
        
        if not type(postfix) == type(list()):
            return "Calculations can only be done with postfix lists not strings"
        
        # ============================================ Calculating ============================================
        
        DIVFLAG = False
        for char in postfix:
            if char == '*' or char == '/' or char == '+' or char == '-' or char == '^':  # operators
                try:  
                    val2 = float(self.primaryStack.pop())
                    val1 = float(self.primaryStack.pop())
                except IndexError:
                    return "Error: Operators are wack"

                if char == '^':
                    self.primaryStack.push(val1**val2)     
                if char == '*':
                    self.primaryStack.push(val1*val2)     
                if char == '/':
                    DIVFLAG = True
                    try:
                        
                        self.primaryStack.push(val1/val2)     
                    except ZeroDivisionError:
                        return "Error: Divide by Zero Error"
                if char == '+':
                    self.primaryStack.push(val1+val2)     
                if char == '-':
                    self.primaryStack.push(val1-val2)   
            else:
                self.primaryStack.push(char)  

        try:
            answer = self.primaryStack.pop()
        except IndexError:
            return "Error: Bad Input"


        if self.primaryStack.is_full():
            return "Error: remaining values in stack"

        if DIVFLAG:
            self.primaryStack.burn()
            self.secondaryStack.burn()
            return float(answer)
        else:
            self.primaryStack.burn()
            self.secondaryStack.burn()
            return int(answer)

        # Keep the instructions below with your code.
        # implement as directed
        #• Repeat
        #• If operand, push onto stack
        #• If operator
        #   • pop operands off the stack
        #   • evaluate operator on operands
        #   • push result onto stack
        #• Until expression is read
        #• Return top of stack



if __name__ == '__main__':
    def test_all(c: Calculator): # Test
        print()
        
        def e(inp: str):
            try:
                return eval(inp.replace('^', '**'))
            except Exception as e:
                return e
            
        
        # "4(6)" acts weird for eval()
        tests = [
            "1--4", 
            "53**3",
            "53^3",
            "1+4",
            "(5 + 9) * ((2 - 4 * 2) / 2) + 2^9 ",
            "5/2*5/2+1 ",
            "(5+4 *",
            "(1 + 2) * 3 * ((6 * 6) + 1)",
            "5/3",
            "",
            "-",
            "*",
            "()",
            "t",
            "t*",
            "1*",
            ")",
            "*(4+3)",
            "*(4+)",
            "5++43",
            "5+-43",
            "5-+43",
            "10/5/3",
            "53+",
            "53+t",
            "53/t",
            "53/0",
        ]

        labels = [
            'Iter',
            'input',
            'eval()',
            'result',
            'postfix',
        ]
        form = '|{:<5.5}|{:<25.25}|{:<8.8}|{:<35.35}|{:<35.35}|'.format
        
        print(form(*['-'*100 for x in labels]))
        print(form(*labels))
        print(form(*['-'*100 for x in labels]))
        
        for i,t in enumerate(tests):
            try:
                baseEval = e(t)
            except Exception as ex:
                baseEval = "ERR " + ex
            
            try:
                postfix = c.convert(t)
            except Exception as ex:
                postfix = "ERR " + ex
                
            try:
                result = c.evaluate(postfix)
            except Exception as ex:
                result = ex
                
            printout = [
                str(i+1),
                str(t),
                str(baseEval),
                str(result),
                str(postfix),
            ]
            
            print(form(*printout))
            # print(printout)
            
        print(form(*['-'*100 for x in labels]))
        print("\n\nBe Aware of any inputs such as '5**3', eval() does 5^3 (like in python), We should not worry about 5**3 to my knowledge\n\n")
    
    
    
    # instantiating the linked list
    calc = Calculator()
    test_all(calc)