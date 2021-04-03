# Uses python3
import sys


def get_change(m):
    """As we already know, a natural greedy strategy for the change problem does 
    not work correctly for any set of denominations. For example, if the available 
    denominations are 1, 3, and 4, the greedy algorithm will change 6 cents using 
    three coins (4 + 1 + 1) while it can be changed using just two coins (3 + 3). 
    Your goal now is to apply dynamic programming for solving the Money Change 
    Problem for denominations 1, 3, and 4.

    Input Format
    Integer money

    Output Format
    The minimum number of coins with denominations 1, 3, 4 that changes money.
    
    Constraints
    1 ≤ money ≤ 10^3 """

    # don't waste time
    if m == 0:
        return 0

    coins = [0, 1, 3, 4]

    # initialise matrix where rows are coin denominations and cols are money amounts from 0 to m
    # an additionnal row for 0 coins is used to allow for comparison with a base denomination
    # for the first coin

    # This doesn't do what you hoped.
    # table = [[0]* (m+1)] * len(coins)
    # It reuses list objects multiple times. As you can see when you made a change to one cell, 
    # which was in a reused list object.
    table = [ [0 for j in range(m+1)] for i in range(len(coins))]

    
    for j in range(1, m+1): 
        # skips 0 money as that can be 'formed' with no coins
        # any amounts > 0 cannot be formed with a 0 coin --> 10e9 is a placeholder for infinity
        table[0][j] = 10e9 


    # iterate through all amounts, skipping 0, until m is reached and poplate the table
    for amt in range(1, m+1):

        # iterate through each denomination
        for i in range(1, len(coins)):

            if amt >= coins[i]:
                # if the amount is more than the current coin 
                # there are >= 2 ways to form the amount
                # the amount can be formed without using any more of the current coin
                # or it can be formed using one more of the current coin
                # i.e. check how the (amount - coin) was formed and add 1
                # compare the two ways and return the minimum
                table[i][amt] = min(table[i-1][amt], table[i][amt - coins[i]] + 1)
            
            else:
                # the amount is less than the current coin
                # impossible to use any more of the current coin
                table[i][amt] = table[i-1][amt]


    # return the last value of the entire table which corresponds to the min no. of coins to form m
    return table[-1][-1]

if __name__ == '__main__':
    m = int(sys.stdin.read())

    print(get_change(m))
    