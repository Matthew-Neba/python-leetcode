5 Basic DP Patterns:

1. Unbounded Knapsack (loop over all coins to use for each possible target),

# O(n x target) time complexity, O(target) space complexity

2. 0/1 Knapsack (build table starting from no coins and a target of 0, to all targets we can reach if we can use all coins. Incrementally update the table for each coin we use),

# O(n x target) time complexity , O(target) space complexity

3. Palindromic Problems (expand outwards starting from each possible palindromic center) ,

# O(n^2) time complexity, O(1) space complexity

4. LCS (Longest Common Subsequence) This type of DP/varitaions of it are based on the idea of ensuring indexes of strings have some property (For LCS, the property was the indexes of both strings must belong to the LCS. For Edit Distance, the property was both stritngs having the same characters at all thier indexes)

# O(n x m) time complexity and O(n x m) space complexity --> Space can be optimzied to O(min(m,n))

5. String DP. This type of DP is multidimensional based on the number of input strings. It relies on memoizing results of strings based on the indexes of the strings. For ex, for two strings (i,j) is used as keys for the DP table. Ex: distinct subsequences, Interleaving string.

# O(n x m x ... x k) time complexity and O(n x m x .... x k) space complexity , where n,m, ... , k are the indexes for the input strings

6. Interval DP problems, use where order of elements matters (ex: burst ballons)

# O(n^3) time complexity for three nested loops (start, end, split), O(n^2) space complexity (to store all possible subarray splits)
