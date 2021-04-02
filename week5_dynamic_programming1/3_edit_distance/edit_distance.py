# Uses python3
def edit_distance(s, t):
    """The edit distance between two strings is the minimum number of operations (insertions, deletions, and substitutions of symbols) 
    to transform one string into another. It is a measure of similarity of two strings. Edit distance has applications, for example, 
    in computational biology, natural language processing, and spell checking. Your goal in this problem is to compute the edit 
    distance between two strings.

    The goal of this problem is to implement the algorithm for computing the edit distance between two strings.

    Input Format
    Each of the two lines of the input contains a string consisting of lower case latin letters 

    Constraints
    The length of both strings is at least 1 and at most 100.

    Output Format
    Output the edit distance between the given two strings."""

    T = [[0 for j in range(len(s))] if i == 0 else [0 if j == 0 else None for j in range(len(s))] for i in range(len(t))]

    for j in range(1, len(s)):
        for i in range(1, len(t)):
            if t[j-1] == s[i-1]:
                T[i][j] = T[i-1][j-1]
            else:
                T[i][j] = min(T[i-1][j], T[i][j-1], T[i-1][j-1]) + 1

    # backtrack, and implement such that mismatch is +1 to edit distance
    print(T)
    return T[-1][-1]


if __name__ == "__main__":
    # print(edit_distance(input(), input()))
    print(edit_distance('editing', 'distance'))
