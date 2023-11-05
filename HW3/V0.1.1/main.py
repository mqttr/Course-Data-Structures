# Name: Matthew Roland
# NUID: 98210287
# NETID: mroland

import sys
import time
from datetime import datetime
import random
import matplotlib.pyplot as plt

import sorting
from colors import *

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

def log(msg: str, *args) -> None:
    if args:
        msg = ''.join(args) + msg + colors.ENDC

    currentSend = time.time()
    print(f'  {datetime.fromtimestamp(currentSend).strftime('%Y-%m-%d %H:%M:%S'):<19} | {currentSend - TimingValues.LASTSEND:<10.5f} | {currentSend - TimingValues.FIRSTSEND:<10.5f}| {msg}')
    TimingValues.LASTSEND = currentSend

def graph(lengths) -> None:
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

    print(results)

def time_algorithm(algorithm: int, data: list) -> float:
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

    log(f'Completed {readable[3][algorithm]} sort')

    return end-start

def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1].lower() == 'graph':
        try:
            graph(list(map(int, sys.argv[2:])))
        except ValueError:
            log('Invalid Input: All arguments after "graph" must be integers.', colors.FAIL)
        exit(0)

    log('Normal Timing Mode Started')

    # Checking Length of Input
    if len(sys.argv[1:]) < 3:
        log('Not enough arguments', colors.FAIL, colors.BOLD)
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
    l = []
    if order == 1:
        l = random.sample(range(length), length)
    elif order == 2:
        for x in range(length):
            l.append(x)
    elif order == 3:
        for x in range(length-1, -1, -1):
            l.append(x)

    log('Finished generating input')
    return l

if __name__ == "__main__":
    print(colors.BOLD + colors.UNDERLINE +  f".{'Current Time':^20} | {'Δ Last Msg':^10} | {'Δ Start':^9} | {'Log Message':^30} ." + colors.ENDC)
    log('Started application')
    main()