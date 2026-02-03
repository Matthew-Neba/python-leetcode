from collections import List
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        #    
        # dp + floyd warshall + coordinate compression + trie optimizations
        # 
        # We will use coordinate compression with a trie to make finding the transformation cost for a prefix more efficient
        # as well
        #
        #
        # Time Complexity O(V^3 + N^2), FLoyd Warshall + DP Dominate the Time Complexity
        # Space Complexity: O(V^2 + len(original) * maxlen + len(changed) * max_len)
        #

        # coordinate compression
        unique_ids = {}
        counter = 0
        def generate_id(s):
            nonlocal counter
            if s not in unique_ids:
                unique_ids[s] = counter
                counter += 1
            return unique_ids[s]

        for i,s in enumerate(original):
            generate_id(s)
        
        for i,s in enumerate(changed):
            generate_id(s)

        # Floyd Warshall
        def floyd_warshall(edges):
            dist = [[float("inf")] * len(unique_ids) for _ in range(len(unique_ids))]
            # no intermediary nodes
            for u,v,w in edges:
                dist[unique_ids[u]][unique_ids[v]] = min(dist[unique_ids[u]][unique_ids[v]], w)

            # loop through all intermediary nodes
            for middle in range(len(unique_ids)):
                for u in range(len(unique_ids)):
                    if dist[u][middle] == float("inf"): continue
                    for v in range(len(unique_ids)):
                        dist[u][v] = min(dist[u][v], dist[u][middle] + dist[middle][v])
            
            return dist
        
        # now create the trie for efficient prefix checking
        class Trie:
            def __init__(self):
                self.chars = [None] * 26
                self.word_ends_here = None
            
            def add(self, string):
                c_node = self
                for ch in string:
                    next_node = c_node.chars[ord(ch) - ord("a")]
                    if not next_node:
                        next_node = Trie()
                        c_node.chars[ord(ch) - ord("a")] = next_node
                    c_node = next_node
                
                # this node has a word ending here
                c_node.word_ends_here = unique_ids[string]

            def traverse_trie(self, next_ch):
                next_node = self.chars[ord(next_ch) - ord("a")]
                if next_node:
                    return (next_node, next_node.word_ends_here)
                else:
                    return (None, None)
        
        original_trie = Trie()
        changed_trie = Trie()

        for word in original:
            original_trie.add(word)

        for word in changed:
            changed_trie.add(word)

        min_costs = floyd_warshall(zip(original, changed, cost))

        # time for DP
        max_len = max(max(len(s) for s in original), max(len(s) for s in changed))
        N = len(source)
        dp = [float("inf")] * (N + 1)
        dp[N] = 0
        for i in range(N - 1, -1, -1):
            c_source = original_trie
            c_target = changed_trie

            # first let's handle skipping cur char if we can
            if source[i] == target[i]:
                dp[i] = min(dp[i] , dp[i + 1])

            # now lets try matching all we can, notice we can also bind this by the max_len word in words
            for j in range(i, min(N, i + max_len)):
                c_source , source_word_id = c_source.traverse_trie(source[j])
                c_target, target_word_id = c_target.traverse_trie(target[j])

                if source_word_id is not None and target_word_id is not None:
                    dp[i] = min(dp[i], min_costs[source_word_id][target_word_id] + dp[j + 1])
                
                # we cannot keep expanding, break
                if c_source == None or c_target == None:
                    break
        
        return dp[0] if dp[0] != float("inf") else -1

                







