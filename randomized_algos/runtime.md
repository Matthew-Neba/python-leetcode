-   There are two main reasons why algorithms such as randomized quickselect/quicksort and other data structures based on randomized selection such as : treaps, skip lists have O(nlogn) expected runtime complexity.

1. Repeatedly multiplying n by any ratio r < 1 until n becomes 1 takes c \* log(n) steps where c is some constants. This is O(logn).

ex: let r = 9/10.  
we want to find x in this equations: n \* (9/10)^x = 1

n _ (9/10)^x = 1 ==>
n _ 9^x = 10^x ==>
log(n) + xlog(9) = xlog(10) ==>
log(n) = (log(10) - log(9))x ==>
x = log(n) / (log(10) - log(9)) ==>
x = O(logn)


2. We are able to tolerate some bad pivots/splits in these randomized algorithms as long as they are rare and are sprinkled between the good operations:

ex: Suppose the recurrence relation for a good split is T(N) = 2T(N/2) + O(N). We may ocasionally get a bad split with T(N) = T(N - 1) + O(n). But notice that if we are alternating between good and bad splits, it would just take us twice as long to get to 1, i.e: 2log(n) = O(logn) (note the recurrence relation 2T(N/2) is O(logn))
