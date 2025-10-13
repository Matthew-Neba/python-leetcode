-   Sorting + Heaps are the bread and butter of intervals. Sometimes can use the Sweep Line algorithm as well.

-   When dealing with merging intervals/overlapping intervals, using the min and max function can simplify the code alot. Always try and use it.

-   The Sweep line algorithm is applicable to alot of these intervals type questions. This is because we can model the start and end points of the inteval as events, along with any of the constraints of the specific question. Then we just need to visit(sweep) all these events in thier sorted order and use the results to answer the problem. Remember to sort the intevals though since the sweep line algorithm depends on this.

-   Sorting by (start, end) tuple is often used in these interval problems. Allows to check if there are any conflict in O(n) time by checking the next higher interval (O(logn) + O(n) tehcnically since accounting for the sorting cost). If not, checking for any conflicts would be O(n^2). Also allows for alot of these greedy interval algorithms to work. Like the meeting_rooms_2 algorithm and the min interval to include each query.