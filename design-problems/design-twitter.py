'''
🐦 Problem 3: Twitter Clone (Design + Heap + Hashing)
Design a simplified version of Twitter that supports the following operations efficiently:

✅ Required API:
python
Copy
Edit
class Twitter:
    def postTweet(userId: int, tweetId: int) -> None
    def getNewsFeed(userId: int) -> List[int]
    def follow(followerId: int, followeeId: int) -> None
    def unfollow(followerId: int, followeeId: int) -> None
🧾 Behavior:
postTweet(userId, tweetId)
The user posts a tweet. Store it with a timestamp.

getNewsFeed(userId)
Return the 10 most recent tweet IDs in the user’s news feed.
Tweets must come from:

the user themselves

users they follow

Tweets should be ordered from most recent to oldest.

follow(followerId, followeeId)
Follower starts following followee.

unfollow(followerId, followeeId)
Follower stops following followee. (A user cannot unfollow themselves.)

✅ Constraints:
Tweet IDs are globally unique.

Use timestamps to keep tweet order.

Optimize getNewsFeed() — don't scan all tweets.

You may assume the system starts empty.

🧠 Design Tip:
Use a global timestamp counter (decrementing works for max-heaps).

For each user, store their tweets as (timestamp, tweetId).

For news feed, use a heap to merge tweets from multiple users.


'''
from collections import deque
import heapq
import time
from abc import ABC, abstractmethod

class Postable(ABC):
    @abstractmethod
    def get_id(self) -> int:
        pass
    
    @abstractmethod
    def get_time(self) -> int:
        pass    

class Tweet(Postable):
    def __init__(self, id: int, time: int):
        self._id = id
        self._time = time
    
    def get_time(self):
        return self._time

    def get_id(self):
        return self._id
    
    def __lt__(self, other):
        if isinstance(other, Postable):
            return self._time < other.get_time()
        raise NotImplementedError()
    
class Twitter:
    def __init__(self):
        self._follows = {}
        self._followers = {}
        self._posts = {}
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        # create the first post for the user
        if userId not in self._posts:
            self._posts[userId] = []
        
        # add the post to the users newsfeed
        post = Tweet(tweetId, -time.time())
        heapq.heappush(self._posts[userId], post)
        
    def getNewsFeed(self, userId: int) -> list[int]:
        if userId in self._posts or userId in self._follows:
            posts = []
        
            for post in self._posts[userId]:
                heapq.heappush(posts, post)
                if len(posts) > 10:
                    posts.pop()
            
            if userId not in self._follows:
                return [tweet.get_id() for tweet in posts]
            
            for follower_id in self._follows[userId]:
                for post in self._posts[follower_id]:
                    heapq.heappush(posts, post)
                    
                    if len(posts) > 10:
                        posts.pop()
                        
            return [tweet.get_id() for tweet in posts]
        
        return []
    
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self._follows:
            self._follows[followerId] = set()
        if followeeId not in self._followers:
            self._followers[followeeId] = set()
        if followerId not in self._posts:
            self._posts[followerId] = []
        if followeeId not in self._posts:
            self._posts[followeeId] = []
            
        self._follows[followerId].add(followeeId)
        self._followers[followeeId].add(followerId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self._follows:
            return
        if followeeId not in self._followers:
            return

        self._follows[followerId].remove(followeeId)
        self._followers[followeeId].remove(followerId)
        

if __name__ == "__main__":
    tw = Twitter()

    tw.postTweet(1, 101)
    tw.postTweet(1, 102)

    # User 1 should see their own tweets
    assert tw.getNewsFeed(1) == [102, 101]

    # User 2 follows User 1
    tw.follow(2, 1)

    # User 2 should see User 1’s tweets
    res = tw.getNewsFeed(2)
    assert res == [102, 101]

    tw.postTweet(2, 201)

    # User 2 now sees their own tweet and followed tweets
    assert tw.getNewsFeed(2) == [201, 102, 101]

    # User 2 unfollows User 1
    tw.unfollow(2, 1)

    # User 2 should now only see their own tweet
    assert tw.getNewsFeed(2) == [201]

    # Edge: user posts more than 10 tweets
    for i in range(11):
        tw.postTweet(1, 1000 + i)

    res = tw.getNewsFeed(1)
    # User 1 should only see their 10 most recent tweets
    assert tw.getNewsFeed(1) == [1010, 1009, 1008, 1007, 1006, 1005, 1004, 1003, 1002, 1001]
