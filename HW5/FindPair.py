import sys
import random

import algor

def findPair(arr, type):
    n = len(arr)
    return None



def printArray(arr):
    n = len(arr)

    for i in range(0,  n):
        print(str(arr[i]) + ' ', end=' ')

    print('\n')

def main(sys_arg: list[int]) -> None:
    if not len(sys_arg) == 3:
        raise IndexError

    # The parameters from the execution will be used as prameters for the generateRandomNumbers function below.
    # You must receive parameters, i.e., N, K, Algorithm from the command lines like below.
    # Python3 SortingArray.py 10000 500 0
    N = sys_arg[0]           # how many random numbers
    K = sys_arg[1]           # Sum of two numbers looking for
    Algorithm = sys_arg[2]   # Your algorithm 0, 1, 2

    arr = generate_random_numbers(N)

    if len(arr) < 100:
        print('Generated numbers')
        printArray(arr)

    # Timer Start
    pair = findPair(arr, Algorithm)

	#Timer end
	#Print elapsed time for searching.

def generate_random_numbers(sample_size: int, range_size: int) -> list:
    '''
    Generates a list with random, increasing, and decreasing order of the length 'cnt' 

    :param int order: List will be: 1: random, 2: sorted, 3: reverse sorted
    :param int cnt: Length of desired list
    
    :return: The randomly generated list
    :rtype: list of integers
    '''
    l: list = random.sample(range(range_size), sample_size)
    return l

if __name__ == '__main__':
    if not len(sys.argv[1:]) == 3:
        print("3 arguments required. Not all arguments are present.")
        exit(1)

    global_system_arguments = []
    for arg in sys.argv[1:]:
        try:
            global_system_arguments.append(int(arg))
        except:
            print(f"All arguments must be integers. Could not change \"{arg}\" argument into an integer.")
            exit(1)

    FLAG_EXIT = False
    if not global_system_arguments[0] > 0:
        print("Random Numbers argument must be greater than 0.")
        FLAG_EXIT = True
    if not global_system_arguments[1] > 0:
        print("Sum argument must be greater than 0.")
        FLAG_EXIT = True
    if not global_system_arguments[2] in [0, 1, 2]:
        print("Algorithm argument must be: 0, 1, or 2.")
        FLAG_EXIT = True

    if FLAG_EXIT == True:
        exit(1)

    main(global_system_arguments)