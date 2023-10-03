#!python
#!/usr/bin/python3.11

#Name: Matthew Roland
#ID: 98210287
#Email: mroland@unomaha.edu

import string
import stack

class Caculator:
    def __init__(self):
        self.stack = stack.Stack()
        self.tempStack = stack.Stack()

    def convert(self, infixStr: str):
        '''
        Converts infix to postfix, returns list of postfix to keep multi length numbers
        '''
        # use a stack to covert infix to postfix
        self.stack.dump()
        postfix = [] # output
        infixStr = infixStr.strip().replace(' ', '')

        # Checking for balanced ()
        try:
            for char in infixStr:
                if char == "(":
                    self.stack.push(char)
                elif char == ")":
                    self.stack.pop()
            # Checking for leftover ()
        except IndexError:   
            return "Invalid Input: Unbalanced Parentheses: Too many )"
        finally: 
            if self.stack.is_full():
                return "Invalid Input: Unbalanced Parentheses: Too few )"
            
            self.stack.dump() # Stack should never be full here, but just to make sure :)


        for char in infixStr:
            self.stack.push(char)
        
        self.tempStack.dump()
        lInfix = []
        for char in self.stack.dump():
            if char == "(" or char == ")" or char == "^" \
                        or char == "*" or char == "/" \
                        or char == "+" or char == "-":
                self.tempStack.push(char)
            elif char == "0" or char == "1" \
                        or char == "2" or char == "3" \
                        or char == "4" or char == "5" \
                        or char == "6" or char == "7" \
                        or char == "8" or char == "9": 
                if self.tempStack.is_full():
                    if  "0" in self.tempStack.top() or "1" in self.tempStack.top()\
                            or "2" in self.tempStack.top() or "3" in self.tempStack.top() \
                            or "4" in self.tempStack.top() or "5" in self.tempStack.top() \
                            or "6" in self.tempStack.top() or "7" in self.tempStack.top() \
                            or "8" in self.tempStack.top() or "9" in self.tempStack.top(): 
                        self.tempStack.push(char + self.tempStack.pop())
                    else:
                        self.tempStack.push(char)
                else:
                    self.tempStack.push(char)
            else:
                return f"Invalid Input: {char}"

            # if char == "0": pass
            # elif char == "1": pass
            # elif char == "2": pass
            # elif char == "3": pass
            # elif char == "4": pass
            # elif char == "5": pass
            # elif char == "6": pass
            # elif char == "7": pass
            # elif char == "8": pass
            # elif char == "9": pass

        # Input fixer:
        # x(y) = (x*y)
        # replace regex: \(\d+\) to \s\d+\s

        for x in self.tempStack.peek_stack():
            print(x, end=' | ')
        print()

        # Infix to Postfix
        char: str
        for char in self.tempStack.dump():
            if char == "0" or char == "1" \
                        or char == "2" or char == "3" \
                        or char == "4" or char == "5" \
                        or char == "6" or char == "7" \
                        or char == "8" or char == "9":
                postfix.append(char)
            elif char == "(": 
                self.stack.push(char)
            elif char == ")":
                while self.stack.top() != "(":
                    postfix.append(self.stack.pop())
                self.stack.pop() # removes the remaining (
            elif char == "^": 
                self.stack.push(char)
            elif char == "*" or char == "/":
                while self.stack.top() == "*" or self.stack.top() == "/" or self.stack.top() == "^":
                    postfix.append(self.stack.pop())
                self.stack.push(char)
            elif char == "+" or char == "-":
                while self.stack.top() == "*" or self.stack.top() == "/" or self.stack.top() == "^" or self.stack.top() == "+" or self.stack.top() == "-": 
                    postfix.append(self.stack.pop())
                self.stack.push(char)
            else: 
                return f"Invalid Input: {char} Allowed Inputs: 0-9, *, /, +, -, (, ), ^"

        for char in self.stack.dump():
            postfix.append(char)

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
        #Use stack of tokens
        self.stack.dump()
        
        DIVFLAG = False
        for char in postfix:
            if char == '*' or char == '/' or char == '+' or char == '-' or char == '^':  # operators
                val2 = float(self.stack.pop())
                val1 = float(self.stack.pop())

                if char == '^':
                    self.stack.push(val1**val2)     
                if char == '*':
                    self.stack.push(val1*val2)     
                if char == '/':
                    DIVFLAG = True
                    self.stack.push(val1/val2)     
                if char == '+':
                    self.stack.push(val1+val2)     
                if char == '-':
                    self.stack.push(val1-val2)   
            else:
                self.stack.push(char)  

        answer = self.stack.pop()

        if DIVFLAG:
            return float(answer)
        else:
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
    ## instantiating the linked list
    cal = Caculator()

    #input = ; # Get input from a user

    # inp = input("Input: ")
    inp = "12*2"


    postfix = cal.convert(inp)
    print("postfix: ", postfix)
    input()
    ans = cal.evaluate(postfix)
    print("infix: ", ans)


# 12 4 3 9 18 7 2 17 13 1 5 6