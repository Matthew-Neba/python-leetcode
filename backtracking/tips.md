-   Backtracking is a last resort apart, it is just a smarter brute-force with early exits. Use it when no other better solution exists (DP, Greedy, Mathematical, etc.)

-   The hard part about backtracking if figuring out when it is the optimal solution. Quick and Dirty Method: 

1) If the solution space is exponential, then backtracking is most likely optimal. Just then need to find the most optimal way to check the constraints of the backtracking problem if there are any. This can sometimes be done by just simulating the backtracking and seeing if there are approximately exponential leaf nodes in the decision tree. 

2) If a problems seems to be NP, ie: easy to verify but very hard so solve, mostlikely use backtracking. ex: Wordsearch


-   Backtracking Algorithm is just a way to explore decision trees. We generally use the path variable to keep track of the current value of the decision tree node. We usually also use another variable to check what choices we have left to make (sometimes no variable needed for this, ex: Word Search).

-   Make sure to undo all changes to variables that are shared between the decision tree nodes when doing backtracking

-   We use the base case to check when we should stop exploring the decision tree or when we have reached a leaf node in the tree (i.e: considered all possible choices). 

-   General template:
    def backtrack(path, choices):

        if base_case_condition(path):
            res.append(path[:])  # Make a copy
            return

        for choice in choices:
            if is_valid(choice, path):
                path.append(choice)     # Make choice
                backtrack(path, updated_choices)        # Explore further
                path.pop()                       # Undo choice, necessary to undo effects to all shared variables between nodes
