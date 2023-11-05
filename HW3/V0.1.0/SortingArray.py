# Name: Matthew Roland
# NUID: 
# NETID: mroland

import sys
import random
import time

import matplotlib.pyplot as plt 

class TimingValues():
    FIRSTSEND = time.time()
    LASTSEND = time.time()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class SortFuncs():
    def bubble(data): # Class Notes
        temp = 0
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                # if out of order, swap!
                
                if data[j] > data[j+1]:
                    temp = data[j]
                    data[j] = data[j+1]
                    data[j+1] = temp

        return data

    def selection(data): # https://www.askpython.com/python/selection-sort-in-python
        n = len(data)
        for i in range(n - 1):
            min = i
            for j in range(i + 1, n):
                if(data[j] < data[min]):
                    min = j
            data[i], data[min] = data[min], data[i]

        return data

    def insertion(data): # https://www.programiz.com/dsa/insertion-sort

        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            
            # Compare key with each element on the left of it until an element smaller than it is found
            # For descending order, change key<array[j] to key>array[j].        
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j = j - 1
            
            # Place key at after the element just smaller than it.
            data[j + 1] = key
        
        return data

    def shell(data): # https://www.geeksforgeeks.org/shellsort/ 
        n = len(data)
        gap=n//2
        
        while gap>0: 
            j=gap 
            # Check the array in from left to right 
            # Till the last possible index of j 
            while j<n: 
                i=j-gap # This will keep help in maintain gap value 
                
                while i>=0: 
                    # If value on right side is already greater than left side value 
                    # We don't do swap else we swap 
                    if data[i+gap]>data[i]: 
    
                        break
                    else: 
                        data[i+gap],data[i]=data[i],data[i+gap] 
    
                    i=i-gap # To check left side also 
                                # If the element present is greater than current element  
                j+=1
            gap=gap//2

        return data

    def merge(data): # https://stackoverflow.com/questions/18761766/mergesort-with-python


        if len(data) < 20:
            return sorted(data)
        result = []
        mid = int(len(data) / 2)
        y = SortFuncs.merge(data[:mid])
        z = SortFuncs.merge(data[mid:])
        i = 0
        j = 0
        while i < len(y) and j < len(z):
            if y[i] > z[j]:
                result.append(z[j])
                j += 1
            else:
                result.append(y[i])
                i += 1
        result += y[i:]
        result += z[j:]
        
        return result

    def quick(inp): # Quick sort wrapper to make all function calls to all sorting algorithms the same

        def _quick_sort(array, start, end): # https://stackabuse.com/quicksort-in-python/ 
            def _partition(array, start, end):
                pivot = array[start]
                low = start + 1
                high = end

                while True:
                    # If the current value we're looking at is larger than the pivot
                    # it's in the right place (right side of pivot) and we can move left,
                    # to the next element.
                    # We also need to make sure we haven't surpassed the low pointer, since that
                    # indicates we have already moved all the elements to their correct side of the pivot
                    while low <= high and array[high] >= pivot:
                        high = high - 1

                    # Opposite process of the one above
                    while low <= high and array[low] <= pivot:
                        low = low + 1

                    # We either found a value for both high and low that is out of order
                    # or low is higher than high, in which case we exit the loop
                    if low <= high:
                        array[low], array[high] = array[high], array[low]
                        # The loop continues
                    else:
                        # We exit out of the loop
                        break

                array[start], array[high] = array[high], array[start]

                return high


            if start >= end:
                return

            p = _partition(array, start, end)
            _quick_sort(array, start, p-1)
            _quick_sort(array, p+1, end)

            return array
        

        return _quick_sort(inp, 0, len(inp)-1)


def graph(arg):
    _, length, algor = arg
    order = [1, 2, 3]
    orderLabels = ['1', '2', '3']

    results = {
        1:None,
        2:None,
        3:None,
    }

    for o in order:
        results[o] = main([o, length, algor])

    print_logged(results) 
    print([x for x in results.values() ])

    plt.figure(figsize=(12,5))

    plt.subplot(231)
    plt.title('Size 1')
    plt.bar([0-0.3/2, 1-0.3/2, 2-0.3/2], [x for x in results.values()], 0.3, label='Algor 1', color=(1, 0, 0))
    plt.bar([0+0.3/2, 1+0.3/2, 2+0.3/2], [x*2 for x in results.values()], 0.3, label='Algor 2', color=(0, 1, 0))
    plt.xticks([0,1,2], orderLabels, fontsize=15)

    plt.subplot(233)
    plt.title('Size 2')
    plt.bar([0-0.3/2, 1-0.3/2, 2-0.3/2], results.values(), 0.3, color=(1, 0, 0))
    plt.bar([0+0.3/2, 1+0.3/2, 2+0.3/2],[x*2 for x in results.values()], 0.3, color=(0, 1, 0))
    plt.xticks([0,1,2], orderLabels, fontsize=15) 

    plt.figlegend(loc='upper right', ncol=1, labelspacing=0.5, fontsize=14, bbox_to_anchor=(1, 0.9))
    plt.tight_layout(w_pad=6)
    plt.show()


def main(arg):
    _print_readable(arg)

    print_logged("Started Generating Input List")
    generatedList = _generate_input(order=arg[0], length=arg[1])
    print_logged("Completed Generation")
    
    start, end  = time_sort_algorithm(arg[2], generatedList)
    print_logged(f"Start {start:.6f} End {end:.6f} Delta {end-start:.6f}")
    
    return end-start

def time_sort_algorithm(algor: int, inputList: list):
    if algor == 1:
        print_logged("Started Sorting")
        sortStart = time.time()
        SortFuncs.bubble(inputList)
        sortEnd = time.time()
    elif algor == 2:
        print_logged("Started Sorting")
        sortStart = time.time()
        SortFuncs.selection(inputList)
        sortEnd = time.time()
    elif algor == 3:
        print_logged("Started Sorting")
        sortStart = time.time()
        SortFuncs.insertion(inputList)
        sortEnd = time.time()
    elif algor == 4:
        print_logged("Started Sorting")
        sortStart = time.time()
        SortFuncs.shell(inputList)
        sortEnd = time.time()
    elif algor == 5:
        print_logged("Started Sorting")
        sortStart = time.time()
        SortFuncs.merge(inputList)
        sortEnd = time.time()
    elif algor == 6:
        print_logged("Started Sorting")
        sortStart = time.time()
        SortFuncs.quick(inputList)
        sortEnd = time.time()
    else:
        return None
    
    return (sortStart, sortEnd)

def _print_readable(arg) -> None:
    humanReadableArguments = {
        1: {
            1:'pseudo randomly generated',
            2:'sorted',
            3:'reverse sorted',
        },
        2: {
            1:str(arg[1]),
        },
        3: {
            1:'Bubble', 
            2:'Selection', 
            3:'Insertion', 
            4:'Shell', 
            5:'Merge', 
            6:'Quick', 
        },
    }

    option: dict
    for option in humanReadableArguments.keys():
        for value in humanReadableArguments[option].keys():
            humanReadableArguments[option][value] = bcolors.OKCYAN + humanReadableArguments[option][value] + bcolors.ENDC


    print_logged('Timing {} Sort \
with {} list \
containing {} values.'.format(humanReadableArguments[3][arg[2]], humanReadableArguments[1][arg[0]], humanReadableArguments[2][1]))

def print_logged(st: str) -> None:
    currentSend = time.time()
    print(f'TIME: {currentSend:<20.6f} SINCE LAST CALL: {currentSend - TimingValues.LASTSEND:<20.6f} TOTAL PROGRAM RUN: {currentSend - TimingValues.FIRSTSEND:<20.6f}{st}')
    TimingValues.LASTSEND = currentSend

def _generate_input(order: int, length: int) -> list:
    '''
    Generates a list with random, increasing, and decreasing order of length length 

    :param int order: List will be: 1: random, 2: sorted, 3: reverse sorted
    :param int length: Length of desired list
    
    :return: The randomly generated list
    :rtype: list of integers
    '''

    l = []
    if order == 1:
        l = random.sample(range(length), length)
        return l
    if order == 2:
        for x in range(length):
            l.append(x)
        return l
    if order == 3:
        for x in range(length-1, -1, -1):
            l.append(x)
        return l

def _die(cause: int, *arg: tuple[str]):
    print('Usage: py SortingArray.py [input: 1-3] [count: >0] [sorting algorithm: 1-6]')

    match cause:
        case 0:
            print('Unknown Error')
        case 1:
            print('Not enough input parameters')
        case 2:
            print('Not all inputs are integers')
        case 3:
            print(f'{arg[0].title()} value is out of range')

    exit()

def _validate_input(arguments):
    DIEFLAG = False

    try:
        a = [ int(x) for x in arguments ]
    except ValueError:
        _die(2)

    if not a[0] in range(1, 4):
        DIEFLAG = True
        print('Input value is out of range')
    if not a[1] > 0:
        DIEFLAG = True
        print('Count value is out of range')
    if not a[2] in range(1, 7):
        DIEFLAG = True
        print('Sorting algorithm value is out of range')

    if DIEFLAG:
        _die(-1)

    return a

if __name__ == "__main__":

    print_logged("Program Started")

    if len(sys.argv) == 5:
        if sys.argv[1] == "graph":

            arguments = _validate_input(sys.argv[2:5])

            graph(arguments)
            exit()
    

    if not len(sys.argv) == 4:
        _die(1)

    arguments = _validate_input(sys.argv[1:4])
    main(arguments)