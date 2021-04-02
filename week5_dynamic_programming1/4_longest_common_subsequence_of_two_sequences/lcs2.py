#Uses python3

import sys

def lcs2(a, b):
    """Compute the length of a longest common subsequence of two sequences.

    Task
    Given two sequences 𝐴 = (𝑎1,𝑎2,...,𝑎𝑛) and 𝐵 = (𝑏1,𝑏2,...,𝑏𝑚), find the length
    of their longest common subsequence, i.e., the largest non-negative integer 𝑝
    such that there exist indices 1 ≤ 𝑖1 < 𝑖2 <···< 𝑖𝑝 ≤ 𝑛 and 1 ≤ 𝑗1 < 𝑗2 < ··· < 𝑗𝑝 ≤ 𝑚,
    such that 𝑎𝑖1 = 𝑏𝑗1, ... , 𝑎𝑖𝑝 = 𝑏𝑗𝑝.

    Input Format
    First line: 𝑛 
    Second line: 𝑎1, 𝑎2, . . . , 𝑎𝑛 
    Third line: 𝑚
    Fourth line: 𝑏1, 𝑏2, . . . , 𝑏𝑚

    Constraints
    1 ≤ 𝑛,
    𝑚 ≤ 100 
    −10^9 < 𝑎𝑖, 𝑏𝑖 < 10^9  
    
    Output Format 
    Output 𝑝."""


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
