import hw1
import pytest


class Test_hw1():
    def __init__(self):
        pass




if __name__ == "__main__":
    l = hw1.LinkedList()

    # Your testcase will be here.
    # This is a testcase example.
    l.sortedAdd(5)
    l.sortedAdd(2)
    l.sortedAdd(9)
    l.sortedAdd(1)
    l.sortedAdd(7)

    assert 9 == l.findMax()

    l.printReversedList()
    #################################