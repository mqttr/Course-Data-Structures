from stack import *
import random

class Test_Stack():
    def __init__(self):
        pass

    def test_necessary_operations(self):
        print("Testing push & pop...")
        s = Stack()
        l = []

        for i in range(10):
            ran = random.random()
            s.push(ran)
            l.append(ran)

        for ele in s.dump():
            assert l.pop() == ele
        

    def test_is_empty(self):
        print("Testing is_empty...")
        s = Stack()

        s.push(4)
        s.push(3)
        s.push(2)
        s.push(1)

        for x in s.peek_stack():
            pass
        assert False == s.is_empty()
        assert True == s.is_full()
        
        for x in s.dump():
            pass

        assert True == s.is_empty()
        s.push(None)
        assert False == s.is_empty()
        s.push(5)
        assert False == s.is_empty()
        s.pop()
        assert False == s.is_empty()

        s.dump()
        
        assert True == s.is_empty()



if __name__ == "__main__":
    Test_Stack().test_is_empty()
    Test_Stack().test_necessary_operations()