-   Hiezholzer's Algorithm is based on 3 key concepts.

1.  Every eulerian path/circuit graph must have exactly one start and end point. The start point is the node with in_degree = out_degree + 1. The end point is the node with out_degree = in_degree + 1. (note: this can be zero if we have only even degree edges, in this case, we have a Eulerian cycle) . All other edges must be balanced (in_degree == out_degree)

2.  We need to find the end node before we know how exactly to build any of our paths/accomodate around it. This is because the end node must be visited last.

3.  Once we find the end node ( done by starting from the start node and continuosly taking paths until we reach the dead end), we can see that all the unvisted edges left all form cyles (since their degrees are all balanced). Therefore, we can work backwards from that end node and build all other paths.
