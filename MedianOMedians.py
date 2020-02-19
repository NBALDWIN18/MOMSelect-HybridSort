import sys
import math
from math import ceil
from math import floor

'''
Parses a list of values from a file
:param filename: the name of the file to parse
:return: a list of values
'''
def ParseList(filename):
    fd = open(filename, 'r')
    values = []
    for line in fd.readlines():
        values+= line.split()

    try:
        values = [int(val) for val in values]
    except ValueError:
        print('Cannot convert string to int')
        exit()

    fd.close()
    return values

'''
Calculates the median of a list of values
:param arr: the list of values
:return: the value of the median
'''
def Median(arr):
    arr.sort()
    return arr[len(arr)//2]

'''
Partitions a list into two parts around a pivot
:param arr: the list
:param p: the pivot value
:return: the index of the pivot
'''
def Partition(a, p):
    l = 0           #The low index, confirmed index
    found =False    #Checks if the pivot has been found
    i = 0           #The index of the interation

    #For every value in the list
    while i < (len(a)):
        #If current element is less than pivot, swap it with confirmed location and increment l
        if a[i] < p:
            a[i],a[l] = a[l],a[i]
            l += 1
        #If the current element is the first pivot, move the pivot to the end
        elif a[i] == p and not found:
            found = True
            a[i],a[len(a)-1] = a[len(a)-1],a[i]
            i -= 1
        i += 1

    #Swap the pivot and the last confirmed value
    a[l],a[len(a)-1] = a[len(a)-1],a[l]
    return a, l

'''
Finds the value of the ith smallest value in the list
:param arr: the list of values
:param i: the position i being searched for
:param k: the block size
:return: the value of the ith smallest value in the list
'''
def median_of_medians(arr, i, k):
    arr_len = len(arr)

    #Brute force the median if there are few values
    if arr_len <= k**2:
        pivot = Median(arr)
    else:
        if len(arr)% k ==0:
            num_blocks = len(arr)/k
        else:
            num_blocks = (len(arr)//k)+1

        medians = []
        #Calculate medians for each block
        for j in range(num_blocks):
            medians.append(Median(arr[j*k:(j+1)*k]))

        #Get the median of the medians
        pivot = median_of_medians(medians, len(medians)//2, k)

    #Partition the list around the pivot
    arr, r = Partition(arr, pivot)
    r += 1

    #The value is in the left partition
    if r < i:
        return median_of_medians(arr[r:], (i-r),k)

    #The value is in the right partition
    elif r > i:
        return median_of_medians(arr[:r-1], i,k)

    #The value is the pivot
    else:
        return pivot

'''
Main function
:return: None
'''
def main():
    #Organize command line inputs
    file_name = sys.argv[1]
    k = int(sys.argv[2])
    i = int(sys.argv[3])

    #Parse Data
    arr = ParseList(file_name)

    #Perform MOMSelect
    print(median_of_medians(arr, i, k))

if __name__ == '__main__':
    main()
