'''
🔄 Problem: Sliding Window Rate Limiter
Design a rate limiter that allows up to N requests per user within the last T seconds.

You must reject any request that exceeds the limit within the sliding window.

Requirements:
Implement a class with the following method:

allow_request(user_id: str, timestamp: int) -> bool
Returns True if the request should be allowed.

Returns False if the request exceeds the limit within the last T seconds.

Class Signature:
python
Copy
Edit
class SlidingWindowRateLimiter:
    def __init__(self, max_requests: int, window_size: int):
        """
        :param max_requests: Maximum allowed requests per user in the time window
        :param window_size: Size of the sliding window in seconds
        """

    def allow_request(self, user_id: str, timestamp: int) -> bool:
        """
        :param user_id: Unique ID of the user making the request
        :param timestamp: Request timestamp in seconds (strictly increasing)
        :return: True if allowed, False if rate limit is exceeded
        """
Example:
python
Copy
Edit
rl = SlidingWindowRateLimiter(3, 10)
print(rl.allow_request("alice", 1))   # True
print(rl.allow_request("alice", 3))   # True
print(rl.allow_request("alice", 8))   # True
print(rl.allow_request("alice", 9))   # False (4th request in 10s window)
print(rl.allow_request("alice", 15))  # True (1st request after old ones expired)
Constraints:
Timestamps are strictly increasing per user.

Max 10⁴ users.

Use efficient time and space (ideally O(1) per request).


'''

from collections import deque

class SlidingWindowRateLimiter:
    def __init__(self, max_requests: int, window_size: int):
        """
        :param max_requests: Maximum allowed requests per user in the time window
        :param window_size: Size of the sliding window in seconds
        """
        self._max_requests = max_requests
        self._window_size = window_size
        self._user_requests = {}
        
    def allow_request(self, user_id: str, timestamp: int) -> bool:
        """
        :param user_id: Unique ID of the user making the request
        :param timestamp: Request timestamp in seconds (strictly increasing)
        :return: True if allowed, False if rate limit is exceeded
        """
        # check if we have a request channel set
        if user_id not in self._user_requests:
            self._user_requests[user_id] = deque([])
        
        # remove old requests that are outside the window
        while self._user_requests[user_id] and self._user_requests[user_id][0] < timestamp - self._window_size:
            self._user_requests[user_id].popleft()
        
        # check the number of accepted requests in the window, if we are at capacity or greater we do not add it to the queue and return false
        if len(self._user_requests[user_id]) >= self._max_requests:
            return False
        
        self._user_requests[user_id].append(timestamp)
        return True
    
        
if __name__ == "__main__":
    rl = SlidingWindowRateLimiter(3, 10)
    print(rl.allow_request("alice", 1))   # True
    print(rl.allow_request("alice", 3))   # True
    print(rl.allow_request("alice", 8))   # True
    print(rl.allow_request("alice", 9))   # False (4th request in 10s window)
    print(rl.allow_request("alice", 15))  # True (1st request after old ones expired)