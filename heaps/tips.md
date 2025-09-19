-   The ultimate clue for heaps is when we need to obtain a minimum/maximum anytime during a problem. Or when we need to
    perform order statistics (K-smallest, median, etc.)

-   A clue to use heaps is when dealing with dynamic/online datasets.

-   When thinking of sorting data, consider using heaps first. Heaps are more efficient if we would just like a subset of the sorted data. ex: first 4 elements, last 3 elements.

- Careful heap state management is crucial for constrained optimization problems. We just need to find the most efficient way
to ensure the heap has the elements we would like at the current step. We can also sort differnet elements with different priorities


-Tips on finding maximums: If we have a fixed range of values, then can always obtain maximum or minimum in constant time. Can also get top k maximum elements with bucket sort variation (can be done for any k if we have only non negative values/can be modified as such by some function) in O(m) time where m is the maximum value in the array. Can also finally use a heap for nlogk if we want top K elements and don't have a fixed range. Now if we want the K'th element (or top K elements), we can also use quick select for the average time complexity of O(n) but worse case of O(n^2).

1) Dynamic data/Streams --> Heaps
2) Small Fixed bound on the values --> Bucket sort
3) Static data --> Quick select can work
