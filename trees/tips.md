<!-- !ABOVE ALL ELSE: -->
Recursion is not magic. It is just a tool to easily write the solution to problems that naturally break down into subproblems of the same kind. Begin by reasoning out the optimal solution and apply recursion if you can see the recursive pattern.
-   When doing recursion, be careful about handling the case where the root/children are Null as the base case. This can lead to confusion. If possible, use root being Null as the base case

- Some problems use a specific recursion pattern for trees. The pattern is we are looking for the best value/metric that can be calculated for every single node in the tree. However, we can resuse the work from a node to help it's parent node. K'th smallest integer in BST and Binary Tree Maximum Path Sum are examples of this. DO NOT USE NESTED RECURSION FOR THESE PROBLEMS.

- Remember that using global variables in recursion is like using that global variable as an implicit parameter to the recursive function


** Recursion Framework **:

Assumptions (Trust the Recursion):

1)   Correct Parameters: Assume the current function receives correct parameters.

2)   Correct Subproblem Solving: Assume recursive calls correctly solve their respective subproblems.

3)   Correct Return Values: Assume recursive calls return the correct results.


What You Must Ensure (Your Responsibilities):

1)   Break Down to Base Case:
    Make sure every recursive path eventually reaches a base case and stops.

2)  Pass Correct Parameters to Recursive Calls:
    Ensure the recursive calls are made with the correct(correct as in maintaining the same structure as the original problem)

3) Solve the Current Problem:
Use the results from the recursive calls to compute the result for the current function call.

4) Return the Correct Value:
Return the result that corresponds to the correct answer for the current parameters.
