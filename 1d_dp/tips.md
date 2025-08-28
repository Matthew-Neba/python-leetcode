- Ultimately for DP ask in this order: 
1) Are the subproblems independent?  (ex: Burst Ballons)
2) Are we generating the smallest possible number of total subproblems ? (ex: House Robber)
3) Can we reduce the amount of times we call each subproblem ? (ex: Longest Palindromic String)

- Drawing the decision tree and seeing the repeated subproblem calls can significantly help with this. Visualizing the subproblems can help to see where calls are repeated

-   To determine the time complexity of dp, two steps:
1. First consider the time it takes to solve one subproblem given all the others are solved
2. Then, multiply that number by all the subproblems we will need.


-   DP -------> optimal non-overlapping substructure pattern
-   Greedy ---> optimal non-overlapping substructure pattern + greedy local choice

-   There is often a dichotomy between greedy and dp solutions. Some solutions that seem
    solvable by dp can actually be solved more efficiently by the greedy solution instead.

5 Basic 1D DP Patterns:
1) Unbounded Knapsack (loop over all coins to use for each possible target), 
# O(n*target) time complexity, O(target) space complexity

2) 0/1 Knapsack (build table starting from no coins and a target of 0, to all targets we can reach if we can use all coins. Incrementally update the table for each coin we use), 
# O(n*target) time complexity , O(target) space complexity

3) Palindromic Problems (expand outwards starting from each possible palindromic center) ,
# O(n^2) time complexity, O(1) space complexity

4) LCS (Longest Common Subsequence) (finding the longest sequence common to two strings while maintaining relative order)
# O(n * m) time complexity and O(n * m) space complexity

5) Interval DP problems, use where order of elements matters (ex: burst ballons)
# O(n^3) time complexity for three nested loops (start, end, split), O(n^2) space complexity (to store all possible subarray splits)
