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

    # init table of min edit distance between s and t
    # first row and first col corresponds to base case (edit distance btw null string and other string)
    # therefore, edit distance corresponds to length of non-null (sub) string 

    T = [[j for j in range(len(s) + 1)] if i == 0 else [i if j == 0 else None for j in range(len(s) +1)] for i in range(len(t) + 1)]
    
    # iteratively populate table by finding minimum of each possible action taken (in, del, match/mismatch) 
    for j in range(1, len(s) + 1):
        for i in range(1, len(t) + 1):
            if s[j-1] == t[i-1]:
                # match will not incur any penalty to edit distance
                # therefore, T[i-1][j-1] and not T[i-1][j-1] + 1
                T[i][j] = min(T[i-1][j-1], T[i-1][j] + 1, T[i][j-1] + 1)

            else:
                # mismatch will incur +1 penalty to edit distance
                T[i][j] = min(T[i-1][j], T[i][j-1], T[i-1][j-1]) + 1

    # return min edit distance between the 2 full strings
    return T[-1][-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
    # print(edit_distance('editing', 'distance'))
