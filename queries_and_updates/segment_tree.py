"""
Segment trees are for handling range queries with point updates over operations that:

1) Can be broken down into the same operation over a smaller range

Big idea here is that for k = all powers of 2 <= N, divide the array into segments of length k. Compute the operation over every one of those segments. We will represent this structure as a tree where the leaf layer are for operations over
segments of length 2^0 = 1. Every layer we go up, we have the operation ofver subarrays of lengths of subsequent powers of 2.

ex: 
operation: sum

array = [1 9 4 5 6 3 10 23 ]
idx:     0 1 2 3 4 5 6  7

                      61
len = 8:            [0-7]
                19           42
len = 4:       [0-3]        [4-7]

             10    9       9     33
len = 2:    [0-1] [2-3]   [4-5] [6-7]

             1   9   4   5   6   3   10  23
len = 1:    [0] [1] [2] [3] [4] [5] [6] [7]


Notice that since there are 2(n) - 1 nodes in the tree, building it takes O(2n) space. Also note that once we have the lower layers,we can build each node in constant time as well. O(n) time, O(n) space for building the segment tree. Note that the height of the tree is also log(n).

Now, if we would like to do a range query, notice that we can traverse the tree from root down. If we see that any of the children contains an index in the range query, we further traverse that node to try and obtain the value of the operation over those indexes. Note that it can be shown that if we carefully traverse the tree ( 1) stopping when we know children can no longer contain elements of the range query, 2) returning the value of the node when the range of the node is fully contained in the range query), then we can perform a range query in log(n) time.

Now for updating an index, we just start from the leaf node corresponding to that index and propagate the update upwards. Notice that since the height of the tree is log(n), we can do a point update in log(n) time.
"""

#
# Segment tree implementation for "+" operation
#
# O(n) time , O(n) space to build the tree
# O(logn) query time, O(logn) point update time
#
class SegmentTree:
    def __init__(self, arr):
        # find first power of 2 larger than n to pad array (use identity values for the given operation).
        # Implementation depends on a complete binary tree (for array representation of a tree) which needs a power of 2 nodes
        # at leaf layer
        self.size = 1
        while self.size < len(arr):
            self.size *= 2
        
        # 0 is the identity for sum operations
        self.tree = [0] * (2 * self.size)

        # initialize leaf layers ,(note 2 * size nodes in array, we store leaf nodes in last half of array)
        for i in range(len(arr)):
            self.tree[self.size + i] = arr[i]

        # initialize internal nodes (ignore 0'th node since we have exactly 2*size - 1 nodes in tree (even though 2*size positions in the array))
        for i in range(self.size -1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i + 1]

    def update(self, idx, val):
        # start at the leaf
        cur_pos = idx + self.size
        self.tree[cur_pos] = val

        while cur_pos > 1:
            # go to current node's parent
            cur_pos //= 2
            # update value of the parent node
            self.tree[cur_pos] = self.tree[2*cur_pos] + self.tree[2*cur_pos + 1]

    def query(self,node, node_low, node_high, query_low, query_high):
        
        # case 1: interval of this node does not contain any value from query range
        if (node_low > query_high or node_high < query_low):
            return 0
        #case 2: interval of this node contains all values from range
        if (node_low >= query_low and  node_high <= query_high ):
            return self.tree[node]  

        #case 3: interval of this node contains some but not all values from range
        split_interval_point = (node_low + node_high) // 2

        left_child_contribution = self.query(2*node, node_low, split_interval_point , query_low, query_high)
        right_child_contribution = self.query(2*node + 1 , split_interval_point+ 1 , node_high, query_low, query_high)
        
        return left_child_contribution + right_child_contribution

        
# fully recursive segment tree:
class SegmentTree2:
    def __init__(self, arr):
        N = len(arr)
        
        # find nearest power of two >= n, (segment tree works on complete binary trees)
        self.size = 1
        while self.size < len(arr):
            self.size *= 2
        
        # 0 is the identity for the sum operation
        self.tree = [0] * (2 * self.size)

        # build the leaf nodes
        for i in range(N):
            self.tree[self.size + i] = arr[i]

        # build the rest of the tree
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i + 1]
        
    def update(self, update_idx, val, cur_idx, node_l, node_r):
        if update_idx <= node_l and update_idx >= node_r:
            # update this node (base case)
            self.tree[cur_idx] = val
            return

        # (idx is outside of the range of this node) current node is not affected
        if update_idx < node_l or update_idx > node_r:
            return
        
        # update children first
        midpoint = (node_l + node_r) // 2

        self.update(update_idx, val, cur_idx * 2, node_l, midpoint)
        self.update(update_idx, val, cur_idx*2 + 1, midpoint + 1, node_r)

        self.tree[cur_idx] = self.tree[cur_idx * 2] + self.tree[cur_idx*2 + 1]

    def query(self,query_l, query_r, cur_idx, node_l, node_r):
        # check if node fully contained in query
        if query_l <= node_l and query_r >= node_r:
            return self.tree[cur_idx]

        # check if outside this node
        if query_r < node_l or query_l > node_r:
            return 0
        
        midpoint = (node_l + node_r) // 2
        
        left_contribute = self.query(query_l, query_r, cur_idx * 2, node_l, midpoint)
        right_contribute = self.query(query_l, query_r, cur_idx*2 + 1, midpoint + 1, node_r)

        return left_contribute + right_contribute

    def query_public(self, query_l, query_r):
        return self.query(query_l, query_r, 1, 0, self.size - 1)

    def update_public(self, update_idx, val):
        return self.update(update_idx, val, 1, 0 , self.size - 1)

    
