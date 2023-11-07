# Name: Matthew Roland
# NUID: 98210287
# NETID: mroland

import sys
import time
from datetime import datetime
import random
import matplotlib.pyplot as plt
import math


class colors:
    '''
    Command prompt colors. 
    '''
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

readable = {
    1: {
            1:'pseudo randomly generated',
            2:'sorted',
            3:'reverse sorted',
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

class TimingValues():
    LASTSEND = time.time()
    FIRSTSEND = time.time()

class sorting():
    '''
    Class to contain all sorting algorithms.
    '''
    def bubble(data): # Class Notes
        temp = 0
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                
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
        y = sorting.merge(data[:mid])
        z = sorting.merge(data[mid:])
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

        def _quick_sort(arr, LEFT, RIGHT): 
            if LEFT < RIGHT:
                mid = math.floor((LEFT + RIGHT) / 2)
                pivot = arr[mid]
                leftIdx = LEFT
                rightIdx = RIGHT
                while(leftIdx <= rightIdx):
                    while arr[leftIdx] < pivot:
                        leftIdx += 1
                    while arr[rightIdx] > pivot:
                        rightIdx -= 1
                    if leftIdx <= rightIdx:
                        #swap(arr, leftIdx, rightIdx)
                        tm = arr[leftIdx]
                        arr[leftIdx] = arr[rightIdx]
                        arr[rightIdx] = tm
                        leftIdx += 1
                        rightIdx -= 1

                _quick_sort(arr, LEFT, leftIdx-1)
                _quick_sort(arr, leftIdx, RIGHT)
        

        return _quick_sort(inp, 0, len(inp)-1)


def log(msg: str, *colorargs) -> None:
    '''
    Prints a log with specific formating, colors can be enabled by setting ENABLECOLORS (bool) to true. Useful for manual timing.
    
    :param msg: Message to be printed out
    :param *colorargs: string variables from the colors class for command prompt colors.
    '''
    if colorargs and ENABLECOLORS:
        msg = ''.join(colorargs) + msg + colors.ENDC

    currentSend = time.time()
    print(f'  {datetime.fromtimestamp(currentSend).strftime('%Y-%m-%d %H:%M:%S'):<19} | {currentSend - TimingValues.LASTSEND:<10.5f} | {currentSend - TimingValues.FIRSTSEND:<10.5f}| {msg}')
    TimingValues.LASTSEND = currentSend

def graph(lengths: list) -> None:
    '''
    Creates a series of graphs and takes every step to create said graphs. Tests all algorithms with consistent inputs.

    :param lengths: A list of desired lengths for the 3 various input list states.
    '''
    log('Graphing Mode Initiated. This will take some time.', colors.HEADER)
    
    results = {
        1: { 1:[], 2:[], 3:[], },
        2: { 1:[], 2:[], 3:[], },
        3: { 1:[], 2:[], 3:[], },
        4: { 1:[], 2:[], 3:[], },
        5: { 1:[], 2:[], 3:[], },
        6: { 1:[], 2:[], 3:[], },
    }

    if not lengths:
        log('Using Default graphing settings as no input sizes were given.')   
        defaults = [ 10_000, 50_000, 100_000 ]
        lengths = defaults

    log('Lengths of inputs: ' + ', '.join(map(str, lengths)))

    randomData = []
    sortedData = []
    reverseSortedData = []

    for length in lengths:
        randomData.append(generate_input(1, length))
        sortedData.append(generate_input(2, length))
        reverseSortedData.append(generate_input(3, length))


    for algor in results.keys():
        for ran, sor, rev in zip(randomData, sortedData, reverseSortedData):
            results[algor][1].append(time_algorithm(algor, list(ran)))
            results[algor][2].append(time_algorithm(algor, list(sor)))
            results[algor][3].append(time_algorithm(algor, list(rev)))

    log('Creating figures...')

    oLabel = ['1', '2', '3']

    print(results)

    for x in range(len(lengths)):
        plt.figure(f'Figure {x} Length: {lengths[x]}')

        for i, result in enumerate(results.keys()):
            plt.subplot(int('23'+str(i+1)))
            plt.title(readable[3][result])

            plt.bar([0-0.3/2, 1-0.3/2, 2-0.3/2], [results[result][1][x], results[result][2][x], results[result][3][x]], 0.3, label=readable[3][result] )

            plt.xticks([0,1,2], oLabel, fontsize=15)


    log('Finished please enjoy')

    plt.tight_layout(w_pad=6)
    plt.show()

def time_algorithm(algorithm: int, data: list) -> float:
    '''
    Test the function given algorithm using the data list as input. This function does not create new list for a sort function call.

    :param int algorithm: 1 bubble 2 selection 3 insertion 4 shell 5 merge 6 quick
    :param list data: List of integers to be input for the given function

    :return: Returns the time the algorithm took using time.time()
    :rtype: float
    '''
    algorithms = {
        1:sorting.bubble,
        2:sorting.selection,
        3:sorting.insertion,
        4:sorting.shell,
        5:sorting.merge,
        6:sorting.quick,
    }

    log(f'Started {readable[3][algorithm]} sort of {len(data)} elements: {', '.join(map(str, data[:10]))}...', colors.OKCYAN)

    start = time.time()
    algorithms[algorithm](data)
    end = time.time()
    
    diff = end-start

    log(f'Completed {readable[3][algorithm]} sort after {diff} s')

    return diff

def main() -> None:
    '''
    Main function to validate information and call proper paths of testing. Uses stdin as input.
    '''
    if len(sys.argv) > 1 and sys.argv[1].lower() == 'graph':
        try:
            arg = list(map(int, sys.argv[2:]))
        except ValueError:
            log('Invalid Input: All arguments after "graph" must be integers.', colors.FAIL)
            exit(1)

        if len(arg) > 6:
            log('Number of inputs must be less than 6.')
            exit(1)

        graph(arg)
        exit(0)

    log('Normal Timing Mode Started')

    # Checking Length of Input
    if len(sys.argv[1:]) < 3:
        log('Not enough arguments', colors.FAIL, colors.BOLD)
        log('Arguments must be a series of 3 integers, or "graph" and optionally up to 6 list length integers')
        log('Exiting...', colors.FAIL, colors.BOLD)

        exit(1)
    elif len(sys.argv[1:]) > 3: 
        log('Too many arguments', colors.FAIL, colors.BOLD)
        log('Exiting...', colors.FAIL, colors.BOLD)

        exit(1)
    
    try:
        options = list(map(int , sys.argv[1:]))
    except:
        log('Invalid Input: Arguments must be integers.', colors.FAIL )
        log('Exiting...', colors.FAIL )
        exit(1)

    # Checking Content of Input
    INVALIDARGFLAG = False
    if options[0] not in range(1, 4):
        log('Out of Range: Input Value must be between 1 and 3, inclusive', colors.FAIL)
        INVALIDARGFLAG = True
    if not options[1] > 0:
        log('Out of Range: Count Value must be > 0', colors.FAIL)
        INVALIDARGFLAG = True
    if not options[2] in range(1, 7):
        log('Out of Range: Algorithm Count must be between 1 and 6, inclusive', colors.FAIL)
        INVALIDARGFLAG = True

    if INVALIDARGFLAG:
        log('Exiting...', colors.FAIL)
        exit(1)

    idontlikelists = generate_input(options[0], options[1])

    results = time_algorithm(options[2], list(idontlikelists))
    log(f'Results for {readable[3][options[2]]}: {results} seconds', colors.OKGREEN)

    return True

def generate_input(order: int, length: int) -> list:
    '''
    Generates a list with random, increasing, and decreasing order of length length 

    :param int order: List will be: 1: random, 2: sorted, 3: reverse sorted
    :param int length: Length of desired list
    
    :return: The randomly generated list
    :rtype: list of integers
    '''
    log(f'Started generating input length: {length} in {readable[1][order]} order')
    l: list
    if order == 1:
        l = random.sample(range(length), length)
    elif order == 2:
        l = list(range(length))
    elif order == 3:
        l = list(range(length-1, -1, -1))

    log('Finished generating input')
    return l

if __name__ == "__main__":
    log('Started application')

    ENABLECOLORS = False
    log('Colors disabled for v1')

    if ENABLECOLORS:
        print(colors.BOLD + colors.UNDERLINE +  f".{'Current Time':^20} | {'Δ Last Msg':^10} | {'Δ Start':^9} | {'Log Message':^30} ." + colors.ENDC)
    else:
        print(f" {'Current Time':^20} | {'Δ Last Msg':^10} | {'Δ Start':^9} | {'Log Message':^30}  ")
    
    main()