from collections import defaultdict, deque
from typing import List

# Always focus on simplicity, if solution start becoming really complex, use occams razor

# Key to this problem is realizing that we can get the dependencies by comparing each word with
# each other word and seeing where the first chharacter differs. No need for recursive checking since 
# since it adds unnecessary complexity. But we then realize that comparing all pairwise words is also not
# necessary, we can just compare words beside each other. This is because this lexographic
# naturally create a chain of dependencies that impply all other dependencies ------> 

# TODO: i:e: lexigraphically ordering preserves the transitive property of sorting. if word[0] is less than word[2] and word[2] is less than word[10], word[0] is less than word[10].

# When doing topological sort, be careful about ensuring the in_degree array is properly created 
# to include all vertices that could possibly exist (not just ones we have edges ingoing/outgoint to),
# can be done by just always providing a fully populated adj list to topological sort


# O(T + V + E ) time,  O(V + E) space --> T is total characters, V is unique char, E is depedency edges
class Solution:
     
    def foreignDictionary(self, words: List[str]) -> str:
        
        # need to make sure to include all chars since topological sort will need it
        adj = {c:[] for word in words for c in word}

        # build the adj list , O(T) time for all characters , O(E) space for adjacency list
        for i in range(0, len(words) - 1):
            word1, word2 = words[i], words[i+1]
            check_length = min(len(word1), len(word2))
            different = False

            # find the differing char
            for j in range(check_length):
                if word1[j] != word2[j]:
                    adj[word1[j]].append(word2[j])
                    different = True
                    break
            
            # make sure prefixes with shorter length come before
            if not different and len(word1) > len(word2):
                return ""

           
        # topological sort
        def topological_sort(adj):
            in_degree = {c:0 for c in adj}
            order = []
            queue = deque([])
            
            # count the indegrees
            for u,neighbors in adj.items():
                # make sure in_degree is fully populated 
                for v in neighbors:
                    in_degree[v] += 1

            # append 0 indegree to queue
            for u,count in in_degree.items():
                if count == 0:
                    queue.append(u)
            
            while queue:
                cur = queue.popleft()
                order.append(cur)

                # update neighbors
                for v in adj[cur]:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        queue.append(v)

            # check if cycle
            return "".join(order) if len(order) == len(adj) else ""


        return topological_sort(adj)
        







