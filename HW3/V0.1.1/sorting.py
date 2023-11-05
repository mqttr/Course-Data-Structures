import math

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
    y = merge(data[:mid])
    z = merge(data[mid:])
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

if __name__ == "__main__":
    import random

    l = []
    for x in range(200):
        l.append(random.random())
    print(l)
    l = merge(l)
