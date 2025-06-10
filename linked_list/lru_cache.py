from collections import deque

# can use dummy nodes to simplify this question. Key to solving this problem in reduced lines of code. Greatly simplifies insertion and deletion into the doubly linked list.

class DoublyNode:
    def __init__(self, key, prev = None, next = None):
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):  
        self.capacity = capacity
        self.lookup = {}
        self.dummyHead = DoublyNode(0)
        self.dummyTail = DoublyNode(0)

        # link up dummy head and tail
        self.dummyHead.next = self.dummyTail
        self.dummyTail.prev = self.dummyHead
        
    def queue_remove(self, queueNode):
        queueNode.prev.next = queueNode.next
        queueNode.next.prev = queueNode.prev
        
    def queue_append(self, queueNode):
            # append after the dummy head
            temp = self.dummyHead.next
            self.dummyHead.next, queueNode.prev = queueNode , self.dummyHead
            queueNode.next, temp.prev = temp, queueNode

    def get(self, key: int) -> int:
        if key in self.lookup:
            # reset position of the key in the queue
            value, queueNode = self.lookup[key]

            self.queue_remove(queueNode)
            self.queue_append(queueNode)

            return value
           
        return -1
        

    def put(self, key: int, value: int) -> None:

        # check if key exists in table, update it in this case
        if key in self.lookup:
            # get the queue node
            _ , queueNode = self.lookup[key]

            self.queue_remove(queueNode)
            self.queue_append(queueNode)

            self.lookup[key] = (value, queueNode)
            return

        # check if the lru_cache is not at max capacity
        if len(self.lookup) < self.capacity:

            # create queue node and insert into queue
            insertNode = DoublyNode(key)
            self.queue_append(insertNode)

            # insert into hashtable
            self.lookup[key] = (value, insertNode)
            return
            
        else:
            # the lru_cache is at max capacity, need to kick out oldest element
            
            # find oldest element from queue
            del_key = self.dummyTail.prev.key

            # remove oldest element from queue
            self.queue_remove(queueNode)

            # remove oldest element from dict
            del self.lookup[del_key]

            # create queue node and insert into queue
            insertNode = DoublyNode(key)
            self.queue_append(insertNode)

            # insert into hashtable
            self.lookup[key] = (value, insertNode)

            return

