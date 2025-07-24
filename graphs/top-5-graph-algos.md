-BFS and DFS need O(V) space due to the need to "remember" which nodes still need to be fully explored. ex: In BFS and DFS, need to fully explore the subtrees of each child of the current node. But if we start exploring one child, we need to remember to come back and explore the other children. This memory is why BFS and DFS are not O(1)

-BFS: impolemented with a queue, iterative ✅ 
-DFS: implemented recursively usually, sometimes iteratively with a stack ✅ 

-Djikstras ✅

-Prim ✅

<!--? TODO: -Union Find:  -->

-Topological Sort ✅
