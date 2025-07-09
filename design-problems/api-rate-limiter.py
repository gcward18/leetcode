'''
 Problem 5: API Rate Limiter (Sliding Window / Token Bucket)
Scenario:
You're building a service that limits the rate of requests per user.
Each user can make at most N requests per T seconds.

✅ Required API:
python
Copy
Edit
class RateLimiter:
    def allowRequest(userId: str, timestamp: int) -> bool
🧾 Behavior:
allowRequest(userId, timestamp)
Returns True if the request should be allowed at timestamp seconds, otherwise False.

Example:
python
Copy
Edit
rl = RateLimiter(limit=3, window=10)

rl.allowRequest("alice", 1)   # True
rl.allowRequest("alice", 2)   # True
rl.allowRequest("alice", 3)   # True
rl.allowRequest("alice", 4)   # False  → limit hit within window

rl.allowRequest("alice", 12)  # True   → oldest request at time 1 is out of 10s window
🧠 Design Goals:
You may implement this using:

Sliding Window approach (store timestamps per user)

Or Token Bucket / Leaky Bucket model (advanced)

✅ Constraints:
Assume up to 1 million users

Assume frequent calls to allowRequest()

Target: O(1) or amortized O(log K) where K is requests per user
'''

from collections import deque

class RateLimiter:
    def __init__(self, limit: int, window: int):
        self._limit = limit
        self._window = window
        self._requests = {}
        
    def allowRequest(self, userId: str, timestamp: int) -> bool:
        if userId not in self._requests:
            self._requests[userId] = deque([])
        
        while self._requests[userId] and self._requests[userId][0] <= timestamp - self._window:
            self._requests[userId].popleft()
        
        if len(self._requests[userId]) < self._limit:
            self._requests[userId].append(timestamp)
            return True
        return False

if __name__ == "__main__":
    rl = RateLimiter(limit=3, window=10)

    print(rl.allowRequest("alice", 1))   # True
    print(rl.allowRequest("alice", 2))   # True
    print(rl.allowRequest("alice", 3))   # True
    print(rl.allowRequest("alice", 4))   # False  → limit hit within window

    print(rl.allowRequest("alice", 12))  # True   → oldest request at time 1 is out of 10s 