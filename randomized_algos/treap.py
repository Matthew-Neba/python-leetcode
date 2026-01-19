import random 

class TreapNode:
    def __init__(self, val):
        self.val = val
        self.priority = random.uniform(0,1)
        self.left = None
        self.right = None
    
    def rotate_right(self, cur_node):
        x = cur_node.left
        y = x.right
        x.right = cur_node
        cur_node.left = y
        # x is the new root
        return x

    def rotate_left(self, cur_node):
        x = cur_node.right
        y = x.left
        x.left = cur_node
        cur_node.right = y

        # x is the new root
        return x

    # this function returns the new root of the tree
    def insert(self, root, new_val):
        if not root:
            return TreapNode(new_val)
        # equal is so that we put same elements to the left
        if new_val <= root.val:
            root = self.insert(root.left, new_val)
            if root.left.priority > root.priority:
                # TODO: rotate right
        else:
            root = self.insert(root.right, new_val)
            if root.right.priority > root.priority:
                # TODO rotate left
        


    def remove(self):
        pass

    def search(self):
        pass
    
