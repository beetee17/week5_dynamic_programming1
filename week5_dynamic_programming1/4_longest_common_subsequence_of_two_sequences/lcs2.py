#Uses python3

import sys

def lcs2(a, b):
    """Compute the length of a longest common subsequence of two sequences.

    Task
    Given two sequences ๐ด = (๐1,๐2,...,๐๐) and ๐ต = (๐1,๐2,...,๐๐), find the length
    of their longest common subsequence, i.e., the largest non-negative integer ๐
    such that there exist indices 1 โค ๐1 < ๐2 <ยทยทยท< ๐๐ โค ๐ and 1 โค ๐1 < ๐2 < ยทยทยท < ๐๐ โค ๐,
    such that ๐๐1 = ๐๐1, ... , ๐๐๐ = ๐๐๐.

    Input Format
    First line: ๐ 
    Second line: ๐1, ๐2, . . . , ๐๐ 
    Third line: ๐
    Fourth line: ๐1, ๐2, . . . , ๐๐

    Constraints
    1 โค ๐,
    ๐ โค 100 
    โ10^9 < ๐๐, ๐๐ < 10^9  
    
    Output Format 
    Output ๐."""

    # BASE CASE: when i = 0 --> update table with lcs of a[:j] and null string
    # Vice versa when j = 0
    T = [[0 for j in range(len(a) + 1)] for i in range(len(b) + 1)] 
    
    # iteratively populate table by finding max at each square
    for j in range(1, len(a) + 1):
        for i in range(1, len(b) + 1):
            if b[i-1] == a[j-1]:
                # extend subsequence if matching characters
                T[i][j] = T[i-1][j-1] + 1

            else:
                # get max of 2 previous possibilities
                T[i][j] = max(T[i-1][j], T[i][j-1])

    s = backtrack(T, a, b)
    print(s)
    # return max length of subsequence between the 2 sequences
    return T[-1][-1]


def backtrack(T, a, b, S = []):

    # backtracking (works to find single lcs only)

    s = []
    i, j = len(b), len(a) 

    while i > 0 and j > 0:
        print(i,j)
        if b[i-1] == a[j-1]:
            s.append(a[j-1])
            i -= 1
            j -= 1
        else:
            if T[i-1][j] > T[i][j-1]:
                i -= 1
            elif T[i][j-1] > T[i-1][j]:
                j -= 1

            else:
                backtrack(T, a[:j], b[:i-1], S)
                print("branching out")
                j -= 1

    s = s[::-1]
    S.append(s)
    return s


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
