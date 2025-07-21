There is one way to improve space and time complexity (even runtime as well). This is to 

# Eliminate superflous calculations/work and extra space. This can be done by:

1) Reusing previous calculations/space. Common in problems where the brute force solution is quite obviously repeating work. Can make the brute force solution more optimal by resusing some of these calculations. ex: Most string sliding window problems, Dynamic Programming.

2) Using key insights to eliminate excessive work. ex: Binary search problems, we eliminate checking all values greater/less than the current value by taking advantage of the fact that the data is sorted.
