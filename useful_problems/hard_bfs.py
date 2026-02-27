from collections import deque
from sortedcontainers import SortedList
class Solution:
    def minOperations(self, s: str, k: int) -> int:
        # 
        # So this seems like some sort of mathematical problem
        # 
        # we want to see if it is possible to make the ones = N.
        #
        # We stop whenever the zeros is a multiple of k. Minimum steps to make zeros a multiple of k.
        #
        # greedy / dp problem, we can use 0/1 BFS to find min distance to get to the state where
        # balance = N. Key idea is to minimize edges though since we can potentially get N^2 edges.
        #
        # Key idea is not to chcek states we have visited before. We don't even consider going there
        # but how can we efficiently do this?
        #
        # We realize that 1) if k is even, we can only change the balance by an even number. 2) If k is odd
        # we can only change the balance by an odd number. Using this key fact and some visualization, 
        # we realize that if we are at a state A and we know the min state we can reach and the max state
        # we can reach from there, we can reach every state in between them that is of the correct parity.
        #
        # So much work for nlogn instead of n^2 smh
        #
        N = len(s)
        orig_ones = 0
        for ch in s:
            orig_ones += 1 if ch == "1" else 0

        evens , odds = SortedList(), SortedList()
        for i in range(N + 1):
            if i % 2 == 0:
                evens.add(i)
            else:
                odds.add(i)

        def bfs(start):
            # how to figure out min and max bounds?
            distances = [float('inf')] * (N + 1)

            if start % 2 == 0:
                evens.remove(start)
            else:
                odds.remove(start)

            q = deque([start])
            distances[start] = 0

            while q:
                cur_ones = q.popleft()
                cur_zeros = N - cur_ones
                if k % 2 == cur_ones % 2:
                    # they have the same parity, we can reach even states in between max and min
                    reachable = evens
                else:
                    # we can reach odd states in between max and min
                    reachable = odds
                
                max_ones_in_k = min(cur_ones, k)
                ones_not_in_k = cur_ones - max_ones_in_k

                lower = cur_ones + (k - max_ones_in_k) - max_ones_in_k

                min_ones_in_k = max(k - cur_zeros, 0)
                ones_not_in_k = cur_ones - min_ones_in_k

                upper = cur_ones + (k - min_ones_in_k) - min_ones_in_k 

                # now we need to explore and remove all states in between upper and lower
                l = reachable.bisect_left(lower)
                r = reachable.bisect_right(upper) - 1

                # remove all elements in the reachable state between our elements and add them to the
                # queue
                while l <= r:
                    popped = reachable.pop(l)
                    distances[popped] = distances[cur_ones] + 1
                    q.append(popped)
                    r -= 1

            return distances

        min_distances = bfs(orig_ones)
        return min_distances[N] if min_distances[N] != float('inf') else -1
                


            