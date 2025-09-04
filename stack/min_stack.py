class MinStack:
    # key to this problem is realizing that we can only add and remove items from the top of 
    # the stack, therefore, we don't need to have a data sturcture like a heap to retain
    # the min from all elements in our data structure. We only need to get the min from the elements below
    # the top of the stack. Can use another stack to store these minimums.

    # O(1) for all operations, O(n) for the class
    def __init__(self):
        self.stack = []
        self.min_arr = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        # need to now edit the min_arr
        if self.min_arr:
            self.min_arr.append(min(self.min_arr[-1], val))
        else:
            self.min_arr.append(val)
        

    def pop(self) -> None:
        self.stack.pop()

        # need to now edit the min_arr
        self.min_arr.pop()
        
        
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_arr[-1]
        
