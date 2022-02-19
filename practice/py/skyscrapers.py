# -------------------------------------------------------------------------------
# --------------------------- Enlightening solutions ----------------------------
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# -------------------------------- My solution ----------------------------------
# -------------------------------------------------------------------------------
# Craft the number in binary, then count the 1s.
# Before I just use bin() how would I do this..
def solve_puzzle(clues):
    return 0  

test1 = ( 
    2, 2, 1, 3,  
    2, 2, 3, 1,  
    1, 2, 2, 3,  
    3, 2, 1, 3 
    )
#       2   2   1   3
#   3 |   |   |   |   | 2
#   1 |   |   |   |   | 2
#   2 |   |   |   |   | 3
#   3 |   |   |   |   | 1
#       3   2   2   1
expect1 = (
    ( 1, 3, 4, 2 ),       
    ( 4, 2, 1, 3 ),       
    ( 3, 4, 2, 1 ),
    ( 2, 1, 3, 4 )
)

test2 = ( 
    0, 0, 1, 2,   
    0, 2, 0, 0,   
    0, 3, 0, 0, 
    0, 1, 0, 0 
    )
#       0   0   1   2
#   0 |   |   |   |   | 0
#   0 |   |   |   |   | 2
#   1 |   |   |   |   | 0
#   0 |   |   |   |   | 0
#       0   0   3   0
expect2 = ( 
    ( 2, 1, 4, 3 ), 
    ( 3, 4, 1, 2 ), 
    ( 4, 2, 3, 1 ), 
    ( 1, 3, 2, 4 )
)

print(f"Tested: {solve_puzzle(test1)}\nExpect: {expect1}")
print(f"Test 2: {solve_puzzle(test2)}\nExpect: {expect2}")


# -------------------------------------------------------------------------------
# -------------------------------- The Prompt ----------------------------------
# -------------------------------------------------------------------------------
# In a grid of 4 by 4 squares you want to place a skyscraper in each square with only some clues:
#     * The height of the skyscrapers is between 1 and 4
#     * No two skyscrapers in a row or column may have the same number of floors
#     * A clue is the number of skyscrapers that you can see in a row or column from the outside
#     * Higher skyscrapers block the view of lower skyscrapers located behind them
# Can you write a program that can solve this puzzle?


# To understand how the puzzle works, this is an example of a row with 2 clues. 
# Seen from the left side there are 4 buildings visible while seen from the right side only 1:

#   4 |   |   |   |   | 1

# There is only one way in which the skyscrapers can be placed. From left-to-right all four buildings 
# must be visible and no building may hide behind another building:
#   4 | 1 | 2 | 3 | 4 | 1

# Example of a 4 by 4 puzzle with the solution:
#               1   2
#     |   |   |   |   |
#     |   |   |   |   | 2
#   1 |   |   |   |   |
#     |   |   |   |   |
#               3

#               1   2
#     | 2 | 1 | 4 | 3 |
#     | 3 | 4 | 1 | 2 | 2
#   1 | 4 | 2 | 3 | 1 |
#     | 1 | 3 | 2 | 4 |
#               3

# Task:
# Finish:
#   function solvePuzzle(clues)
# Pass the clues in an array of 16 items. This array contains the clues around the clock, index:
#   	0	1	 2	 3	  
#  15	  	  	  	  	 4
#  14	  	  	  	  	 5
#  13	  	  	  	  	 6
#  12	  	  	  	  	 7
#   	11	10	 9	 8	  

# If no clue is available, add value `0`
# Each puzzle has only one possible solution
# `SolvePuzzle()` returns matrix `int[][]`. The first indexer is for the row, the second indexer for the column. 
# https://www.codewars.com/kata/5671d975d81d6c1c87000022