from collections import defaultdict, deque
from typing import List
class Solution:
    def minJumps(self, nums: List[int]) -> int:
        # 
        # Immediately thinking of some DP idea, perhaps with some grouping
        #
        # Reminds me of jump game ix
        #
        # We can use a 0/1 BFS idea where we augment the graph for every index to all other 
        # prime teleportations from that index. Similar to the grid teleportation traversal problem.
        #
        # no need for sieve here, can do trial division to see if num is prime
        #
        # Key idea is that a number n must have <= log(n) prime divisors. So, we can 
        # build the adjacenchy matrix safely, it can have at most nlog(n) nodes.
        #
        N = len(nums)

        augmented_adj = defaultdict(list)
        is_prime = [0] * N
        def get_divisors(i):
            x = nums[i]
            prime = True
            cur = 2
            while cur * cur <= x:
                if x % cur == 0:
                    augmented_adj[cur].append(i)
                    prime = False
                
                while x % cur == 0:
                    x //= cur
                    
                cur += 1

            augmented_adj[x].append(i)
            is_prime[i] = prime and x > 1

        for i in range(N):
            get_divisors(i)
        
        # now we can do the bfs
        def bfs():
            distances = [float('inf')] * N
            q = deque([0])
            distances[0] = 0

            while q:
                cur_pos = q.popleft()  # use popleft for proper BFS

                for next_pos in [cur_pos - 1, cur_pos + 1]:
                    if 0 <= next_pos < N and distances[next_pos] == float('inf'):
                        distances[next_pos] = distances[cur_pos] + 1
                        q.append(next_pos)

                if is_prime[cur_pos]:
                   while augmented_adj[nums[cur_pos]]:
                        tel_pos = augmented_adj[nums[cur_pos]].pop()
                        if distances[tel_pos] == float('inf'):
                            distances[tel_pos] = distances[cur_pos] + 1
                            q.append(tel_pos)

            return distances

        min_distances = bfs()
        return min_distances[N - 1]

        