-   Backtracking is a last resort apart, it is just a smarter brute-force with early exits. Use it when no other better soluution exists (DP, Greedy, Mathematical, etc.)

-   Backtracking Algorithm is just a way to explore decision trees

-   We generally use the path variable to keep track of the current value of the decision tree node. We usually also use another variable to check what choices we have left to make (sometiems no variable needed for this, ex: Word Search).

-   We use the base case to check when we should stop exploring the decision tree or when we have reached a leaf node in the tree (i.e: considered all possible choices).

-   General template:
    def backtrack(path, choices):

        if base_case_condition(path):
            res.append(path[:])  # Make a copy
            return

        for choice in choices:
            if is_valid(choice, path):
                path.append(choice)  # Make choice
                backtrack(path, updated_choices)     # Explore further
                path.pop()                           # Undo choice
