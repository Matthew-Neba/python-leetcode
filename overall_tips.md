<!-- TODO: ALWAYS begin all problems by thinking of the problem generally. Do not think of any appraoches like sliding window, backtracking, dfs, etc. Start from a high level. Play around with the problem, think of the brute force solution. Always break down problems into thier essential components. Then after this, start optimizing.  -->

# Ways to Optimize Problems:

1. Reusing previous calculations/space. Common in problems where the brute force solution is quite obviously repeating work. Can make the brute force solution more optimal by resusing some of these calculations. ex: Most string sliding window problems, Dynamic Programming.

2. Using key insights to eliminate excessive work. ex: Binary search problems, we eliminate checking all values greater/less than the current value by taking advantage of the fact that the data is sorted.

3. Inverting/Exchanging problems for equivalent ones can often simplify the solution or make it more efficient.

4. In Big-O analysis, be aware of constants in the problem that can trim the time complexity. ex: maximum frequency of elements
   , but we only have 26 unique elements. Here time complexity of this maximum operation is O(26) = O(1). Just be more careful when doing Big O Analysis, monotonic stack questions may also at first seem to not be O(n) when they are indeed O(n).

-   When finding the minimum or maximum number of operations, it helps to first identify the essential actions and then see what other essential additional actions can be done simultaneously while performing the current essential action

-   Keep your solution’s time and space complexity roughly ≤ 10⁶ for LeetCode and ≤ 10⁷ for platforms like CodeForces; no need to memorize exact constraints. Ex: if n <= 10^3 , cannot have time or space complexity of O(n^3). This is because O(n^3) = O((10^3)^3) = O(n^9) > 10^6. O(n^2) works though since O(n^2) = O((10^3)^2) = O(10^6).
