'''
🔁 Follow-Up 2: Online Room Allocator
Scenario: Meetings now arrive one by one in real-time, and you need to allocate a room for each new meeting as it arrives.

Design a class:

python
Copy
Edit
class MeetingRoomAllocator:
    def __init__(self):
        pass

    def addMeeting(self, start: int, end: int) -> int:
        """
        Returns the assigned room number for this new meeting.
        """
Requirements:
Meetings arrive unsorted and one at a time.

You must assign the lowest available room.

Reuse freed-up rooms as soon as possible.

Assume start values are non-decreasing (real-time stream).

Example:
python
Copy
Edit
allocator = MeetingRoomAllocator()
print(allocator.addMeeting(0, 30))  # 0
print(allocator.addMeeting(5, 10))  # 1
print(allocator.addMeeting(15, 20)) # 1 (room 1 is free again)
Implement when ready — say “done” to proceed.
'''
from abc import ABC, abstractmethod
import heapq

class Schedulable(ABC):
    @abstractmethod
    def get_end_time(self):
        return 
    @abstractmethod
    def get_start_time(self):
        return
    
class Meeting(Schedulable):
    def __init__(self, start_time: int, end_time: int, room_number: int):
        self._start_time = start_time
        self._end_time = end_time
        self._room_number = room_number
    
    def get_room_number(self):
        return self._room_number
    
    def get_end_time(self):
        return self._end_time
    
    def get_start_time(self):
        return self._start_time

    def __lt__(self, other):
        if isinstance(other, Schedulable):
            return self._end_time < other.get_end_time()

class MeetingRoomAllocator:
    def __init__(self):
        self.ongoing = []
        self.room_count = 0
        self.available_rooms = []

    def addMeeting(self, start: int, end: int) -> int:
        """
        Returns the assigned room number for this new meeting.
        """ 
        while self.ongoing and self.ongoing[0].get_end_time() <= start:
            meeting = heapq.heappop(self.ongoing)
            heapq.heappush(self.available_rooms, meeting.get_room_number())
        
        if self.available_rooms:
            room = heapq.heappop(self.available_rooms)
        else:
            room = self.room_count
            self.room_count += 1
        
        heapq.heappush(self.ongoing, Meeting(start, end, room))
        return room
        
if __name__ == "__main__":
    allocator = MeetingRoomAllocator()
    print(allocator.addMeeting(0, 30))  # 0
    print(allocator.addMeeting(5, 10))  # 1
    print(allocator.addMeeting(15, 20)) # 1 (room 1 is free again)
