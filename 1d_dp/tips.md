- Ultimately for DP ask in this order: 
1) Are the subproblems independent?  (ex: Burst Ballons)
2) Are we generating the smallest possible number of total subproblems ? (ex: House Robber)
3) Can we reduce the amount of times we call each subproblem ? (ex: Longest Palindromic String)


-   To determine the time complexity of dp, two steps:
1. First consider the time it takes to solve one subproblem given all the others are solved
2. Then, multiply that number by all the subproblems we will need.


-   DP -------> optimal non-overlapping substructure pattern
-   Greedy ---> optimal non-overlapping substructure pattern + greedy local choice

-   There is often a dichotomy between greedy and dp solutions. Some solutions that seem
    solvable by dp can actually be solved more efficiently by the greedy solution instead.

