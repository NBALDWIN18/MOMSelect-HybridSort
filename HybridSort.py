'''
Author: Nolan Baldwin
PID: A58626719
'''

import sys

#The names of the algorithms used
algs = {1:"Merge Sort", 2:"Quick Sort"}
#The depths of recursion covered
depth_covered = []

'''
Divides a list into 2 even parts
:param inpt: a list
:return: the index of the middle of the list
'''
def MergeSort(inpt):
    if len(inpt) >0:
        return len(inpt)//2

'''
Merges the two sides of the list
:param arr: the list to be merged
:param m: the pivot index
:return: a merged list
'''
def Merge(arr, m):
    i = 0           #index of front list
    j = m           #index of back list
    r = []          #new list
    n = len(arr)-1  #index of the back of the list

    for k in range(len(arr)):   #Loop through every value in the list

        if j > n:               #If all the values in the back are taken care of
            r.append(arr[i])
            i+=1            
        elif i >= m:            #If all the values in the front are taken care of
            r.append(arr[j])
            j += 1
        elif arr[i] < arr[j]:   #If front value is less than back value
            r.append(arr[i])
            i += 1
        else:
            r.append(arr[j])    #If back value is less than front value
            j += 1
    return r

'''
Partitions a list around an index
:param inpt: a list to be partitioned
:return: pivot index in the list
'''
def QuickSort(inpt):
    if len(inpt) >2:                #Handles big input sizes
        p = inpt[len(inpt)//2]        #Pivot is the middle value
        return Partition(inpt,p)
    elif len(inpt) ==2:             #Handles small inpt sizes
        if inpt[0] > inpt[1]:
            inpt[0],inpt[1] = inpt[1],inpt[0]
        return 1

'''
Partitions a list into two parts around a pivot
:param arr: the list 
:param p: the pivot value
:return: the index of teh pivot
'''
def Partition(arr, p):
    l = 0       #The low index, confirmed index
    i = 0       #The interation index

    arr[len(arr)//2],arr[len(arr)-1] = arr[len(arr)-1],arr[len(arr)//2]     #Swap pivot and last element

    while i < (len(arr)-1):     #For every value before the pivot
        #If current element is less than pivot, swap it with confirmed location and increment l
        if arr[i] <= p:
            arr[i],arr[l] = arr[l],arr[i]
            l += 1
        i += 1
    return l

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
Parses the config from the command line
:return: a list of config commands
'''
def ParseConfig():
    config = []
    #Loop through the remaining commands
    for i in range(3,len(sys.argv)):
        config.append(int(sys.argv[i]))

    #Error Checking
    for i in config:
        if i!=1 and i!=2:
            print(i,"is an invalid configuration")
            exit()
    if len(config) <1:
        print("No configuration found")
        exit()

    return config

'''
Write the sorted values to a file, with 1 value per line
:param filename: the name of the file
:param value: the sorted list
:return: None
'''
def WriteOutput(filename, values):
    fd = open(filename, 'w')
    for val in values:
        fd.write(str(val) + '\n')
    fd.close()
    
'''
Sort a list of values based on a user defined configuration
:param inpt: the inpt list
:param config: the configuration list
:param depth: the current depth of recursion
:return: the sorted list
'''
def HybridSort(inpt, config, depth=0):
    global depth_covered

    #Base case: inpt size < 2
    if len(inpt) > 1:
        #Choose algorithm
        if config[depth%len(config)] == 1:
            i = MergeSort(inpt)
        elif config[depth%len(config)] == 2:
            i = QuickSort(inpt)
        
        #Handle output
        if depth +1 not in depth_covered:
            print("Call " + str(depth+2),algs[config[(depth)%len(config)]],i,len(inpt)-i)
            depth_covered.append(depth+1)

        #Recursviely continue on the left and right sides
        left = HybridSort(inpt[:i], config, depth+1)
        right = HybridSort(inpt[i:], config, depth+1)

        #Merge the chunks of the list
        inpt = Merge(left+right,i)
    

    return inpt

'''
Main function
:return: None
'''
def main():
    #Organize command line inputs
    file_names = [sys.argv[1], sys.argv[2]]
    config = ParseConfig()

    #Organize input
    inpt = ParseList(file_names[0])

    #Perform HybridSort
    print("Call 1",algs[config[0]],len(inpt),0)
    otpt = HybridSort(inpt, config, 0)
    
    #Organize output
    WriteOutput(file_names[1], otpt)
    
if __name__ == '__main__':
    main()