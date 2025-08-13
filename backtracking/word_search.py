from typing import List
# Problem imeddiately presents itslef as a backtracking problem. The difficulty is in seeing if a better solution exist. We start by realizing that there is no other way to check if there is a solution but by simulating the process of forming the word on the grid. No check for the frequency of the characters etc. exist that will allow us to determine if a solution exist.
# 
#  Then we realize that even if we don't resuse the previous checks for a square, we will just redo it 3 times at most since each grid square only has 3 adjecent squares. Therefore, DP will only reduce the work by a maximum factor of 3 and this, not affect the time complexity while increasing the space complexity. Backtracking is optimal here

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        pass