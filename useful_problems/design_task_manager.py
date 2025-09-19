from typing import List
#
# Heap with the ability to edit/delete items, lazy heap pattern
# 
from heapq import heapify, heappush, heappop
class TaskManager:

    # O(n) time, O(n) space, n is # of tasks
    def __init__(self, tasks: List[List[int]]):
        self.min_heap = []
        self.task_map = {}

        for userId, taskId, priority in tasks:
            self.min_heap.append((-priority, -taskId, userId))
            self.task_map[taskId] = [priority, userId]

        # make sure the heap is properly initialized
        heapify(self.min_heap)
        
    # O(log(n + m)) time, O(1) space , where m is total amount of updates
    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_map[taskId] = [priority, userId]
        heappush(self.min_heap, (-priority, -taskId, userId))


    # O(log(n + m)) time, O(1) space , where m is total amount of updates
    def edit(self, taskId: int, newPriority: int) -> None:
        self.task_map[taskId][0] = newPriority
        userId = self.task_map[taskId][1]
        heappush(self.min_heap, (-newPriority, -taskId, userId))
        
    # O(1) time, O(1) space
    def rmv(self, taskId: int) -> None:
        del self.task_map[taskId]


    # O(log(n + m)) time, O(1) space , where m is total amount of updates
    def execTop(self) -> int:
        while self.min_heap:
            # check if the top entry has not been edited/deleted, peek at the heap
            priority, taskId, userId = self.min_heap[0]
            priority, taskId = -priority, -taskId

            # ensure not deleted and then not edited
            if taskId in self.task_map and self.task_map[taskId][0] == priority:
                userId = self.task_map[taskId][1]
                heappop(self.min_heap)
                del self.task_map[taskId]
                return userId
            else:
                heappop(self.min_heap)

        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()