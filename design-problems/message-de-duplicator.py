'''
📨 Problem: Message Deduplicator
Design a system that processes incoming messages with IDs, ensuring that duplicate messages are ignored if they were seen in the last time_window seconds.

Requirements:
Your system should support:

1. should_process(message_id: str, timestamp: int) -> bool
If the message ID has not been seen in the last time_window seconds, return True and record it.

If it has been seen in that window, return False.

Class Signature:
python
Copy
Edit
class MessageDeduplicator:
    def __init__(self, time_window: int):
        """
        :param time_window: Number of seconds a message ID should be remembered.
        """

    def should_process(self, message_id: str, timestamp: int) -> bool:
        """
        :param message_id: Unique ID of the incoming message
        :param timestamp: Time in seconds
        :return: True if the message should be processed, False if it’s a duplicate within the time window
        """
Example:
python
Copy
Edit
dedup = MessageDeduplicator(10)
print(dedup.should_process("abc", 1))   # True
print(dedup.should_process("abc", 5))   # False
print(dedup.should_process("abc", 12))  # True (window expired)
print(dedup.should_process("xyz", 15))  # True
print(dedup.should_process("xyz", 20))  # False
Constraints:
All timestamps are strictly increasing.

You may assume at most 10⁴ messages per time window.

'''

from collections import deque

class MessageDeduplicator:
    def __init__(self, time_window: int):
        """
        :param time_window: Number of seconds a message ID should be remembered.
        """
        self._time_window = time_window
        self._message_cache = {}

    def should_process(self, message_id: str, timestamp: int) -> bool:
        """
        :param message_id: Unique ID of the incoming message
        :param timestamp: Time in seconds
        :return: True if the message should be processed, False if it’s a duplicate within the time window
        """
        if message_id in self._message_cache:
            expiration_time = self._message_cache[message_id]
            
            if expiration_time < timestamp:
                self._message_cache[message_id] = timestamp + self._time_window
                return True
            return False
        
        self._message_cache[message_id] = timestamp + self._time_window
        return True


if __name__ == "__main__":
    dedup = MessageDeduplicator(10)
    print(dedup.should_process("abc", 1))   # True
    print(dedup.should_process("abc", 5))   # False
    print(dedup.should_process("abc", 12))  # True (window expired)
    print(dedup.should_process("xyz", 15))  # True
    print(dedup.should_process("xyz", 20))  # False
