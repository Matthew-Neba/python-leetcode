-   Always process all nodes in queue when doing bfs

-   Always make sure a node is processed before adding it to queue for bfs or dfs, this many mean doing some pre-processing for the start nodes. Like adding them to the visited set before adding them to the queue. Helps to manage queue size

- Generally, a fully populated adj list should be provided to topological sort (i.e: all vertices porovided by the problem should be keys in the adjacency list)

-   If need to know details about path, dfs is almost always better than bfs

-   Alot of graph problems can be simplifgied with inversion. ex: pacific atlantic ocean, islands and treasure# common with graphing problems. ex: pacific atlantic ocean, islands and treasure

-  Generally, do not return values when doing recursive dfs on graphs. We cannot use recursive dfs expecting to return something like in trees since cyle exists. You can have A depends on B which depends on C which depends on A. DFS can only be used for marking for graphs
