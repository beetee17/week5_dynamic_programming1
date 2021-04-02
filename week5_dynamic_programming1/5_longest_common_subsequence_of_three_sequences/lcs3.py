#Uses python3

from itertools import permutations
import sys



def lcs3(a, b, c):
    """"""


    
    # Approach to problem: find all lcs of a and b 
    # s1, s2... = lcs(a, b), lcs(a, b, c) = max_len(lcs(s1, c), lcs(s2, c),....)
    # does not work as too time consuming
    # instead, simply extend 2D lcs table to 3D matrix

    T = [[[0 for k in range(len(c) + 1)] for j in range(len(b) + 1)] for i in range(len(a) + 1)]

    # iteratively populate matrix by finding max at each square
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            for k in range(1, len(c) + 1):
                if a[i-1] == b[j-1] and b[j-1] == c[k-1]:
                    # extend subsequence if matching characters
                    T[i][j][k] = T[i-1][j-1][k-1] + 1

                else:
                    # get max of 3 possiblities
                    T[i][j][k] = max(T[i-1][j][k], T[i][j-1][k], T[i][j][k-1])
                                  
    # print(T)
    return T[-1][-1][-1]



# def lcs3(a, b, c):
#     m = len(a)
#     l = len(b)
#     n = len(c)
#     subs = [[[0 for k in range(n+1)] for j in range(l+1)] for i in range(m+1)]

#     for i, x in enumerate(a):
#         for j, y in enumerate(b):
#             for k, z in enumerate(c):
#                 if x == y and y == z:
#                     subs[i+1][j+1][k+1] = subs[i][j][k] + 1
#                 else:
#                     subs[i+1][j+1][k+1] = max(subs[i+1][j+1][k], 
#                                               subs[i][j+1][k+1], 
#                                               subs[i+1][j][k+1])
#     return subs[-1][-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))

    ## STRESS TEST
    # from itertools import combinations
    # a = [3,1,2,5,7]
    # b = [3,2,6,7]
    # c = [3,1,2,6,7]
    # answer = 0
    # largest_subseq = []
    # for i in range(1, min(len(a), len(b), len(c)) + 1):
    # # enumerate all subsequences of a,b and c of length i
    #     for x in combinations(a, i):
    #         for y in combinations(b, i):
    #             for z in combinations(c, i):
    #                 if x == y and y == z:
    #                     # if the sequence is common for a,b and c, update the answer
    #                     largest_subseq = list(x)
    #                     answer = i
            
    # print(answer, largest_subseq)

