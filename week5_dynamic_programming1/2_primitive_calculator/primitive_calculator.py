# Uses python3
import sys

def optimal_sequence(n):
    """You are given a primitive calculator that can perform the following three operations
     with the current number 𝑥: multiply 𝑥 by 2, multiply 𝑥 by 3, or add 1 to 𝑥. Your 
     goal is given a positive integer 𝑛, find the minimum number of operations needed to 
     obtain the number 𝑛 starting from the number 1.

    Task
    Given an integer 𝑛, compute the minimum number of operations needed to obtain the 
    number 𝑛 starting from the number 1
    
    Output Format
    In the first line, output the minimum number 𝑘 of operations needed to get 𝑛 from 1. 
    In the second line output a sequence of intermediate numbers. That is, the second 
    line should contain positiveintegers 𝑎0, 𝑎2, ... , 𝑎𝑘−1 such that 𝑎0 = 1, 𝑎𝑘−1 = 𝑛 and 
    for all 0 ≤ 𝑖 < 𝑘−1, 𝑎𝑖+1 is equal to either 𝑎𝑖 + 1, 2𝑎𝑖, or 3𝑎𝑖. If there are many such 
    sequences, output any one of them. """
    
    


    # initialise array where index are numbers from 0 to n, and values are
    # minimum no. of steps needed to reach the index
    # n from 0 to 3 are known base cases
    array = [0, 0, 1, 1] 

    if n == 1:
        return [1]

    array += [None for i in range(4, n + 1)]

    # populate array with minimum steps
    for j in range(4, n+1):

        # adding one is always a possibility
        possibilities = [array[j-1] + 1] 

        if j % 2 == 0:
            # look at value/2 and add 1 to its steps
            possibilities.append(array[int(j/2)] + 1)

        if j % 3 == 0:
            # look at value/3 and add 1 to its steps
            possibilities.append(array[int(j/3)] + 1)

        # the overall minimum would yield thee true min steps for that value
        array[j] = min(possibilities)

    seq = [n]
    i = len(array) - 1
    while i > 0:
        possible = [array[i-1]]
        new_i = i - 1
        curr_best = array[i-1]
        if i % 2 == 0:
            if array[int(i/2)] < curr_best:
                new_i = i/2

        if i % 3 == 0:
            if array[int(i/3)] < curr_best:
                new_i = i/3

        i = int(new_i)
        seq.append(i)

    # Slice notation in short:

    # [ <first element to include> : <first element to exclude> : <step> ]
    # When reversing (i.e. if <step> is -1), it helps me to think 
    # <first element to include, moving from right to left>
    
    return seq[-2::-1]  

    
    


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')




# from time import time
# for i in range(2, 100):
#     start = time()
#     sequence = optimal_sequence(i)
#     print(time() - start)
#     print(i, len(sequence) - 1)
#     print(sequence)