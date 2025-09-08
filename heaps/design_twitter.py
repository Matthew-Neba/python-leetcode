from typing import List
from typing import defaultdict
from heapq import heappush, heappop, heapify

class Twitter:
    """
     Dynamic elements and order statistics, can use a heap or buckets sort. Values are not
     bounded so use a heap. Note we only need to store the top 10 tweets for every user,
     since we only need to potentially return the top 10 elements

     1) Use a min heap for each user to store thier 10 most recent posts

     2) On post tweet, update this heap to contain the top 10 most recent

     3) For get news feed, get all the users tweets that this user follows plus thier tweets
     and use a min heap to get the top 10 tweets

     4) Follow will be a dict mapping each user to thier followers

    """
    def __init__(self):
        self.followers = defaultdict(set)
        # create a dictionary of heaps
        self.posts = defaultdict(list)
        self.time = 0

        
    def postTweet(self, userId: int, tweetId: int) -> None:
        posts = self.posts
        self.time += 1

        heappush(posts[userId], (self.time,tweetId))
        if len(posts[userId]) > 10:
            heappop(posts[userId])


    def getNewsFeed(self, userId: int) -> List[int]:
        # max size of 10
        post_heap = [post for post in self.posts[userId]]
        heapify(post_heap)

        for followee in self.followers[userId]:
            # Current user, they were already considered
            if followee == userId:
                continue 

            cur_posts = self.posts[followee]
            for post in cur_posts:
                heappush(post_heap, post)
            
                if len(post_heap) > 10:
                    heappop(post_heap)
        
        post_heap.sort(reverse=True)
        return [pair[1] for pair in post_heap]


    def follow(self, followerId: int, followeeId: int) -> None:
        following = self.followers[followerId]
        following.add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        following = self.followers[followerId]
        if followeeId not in following:
            return

        following.remove(followeeId)



