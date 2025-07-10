'''
Problem Title: Meeting Room Scheduler (Greedy / Interval Merge)
Prompt:
You are given an array of meeting time intervals where each interval is represented as [start, end].
Determine the minimum number of meeting rooms required to hold all the meetings without conflicts.

Example:

python
Copy
Edit
Input: intervals = [[0, 30], [5, 10], [15, 20]]
Output: 2
Function Signature:

python
Copy
Edit
def minMeetingRooms(intervals: List[List[int]]) -> int:
'''

import heapq

def minMeetingRooms(meetings: list[list[int]]) -> int:
    indexed_intervals = sorted([(s, e, i) for i, (s, e) in enumerate(meetings)])
    result = [0] * len(meetings)
    ongoing = []
    available_rooms = []
    room_count = 0
    
    for i, start, end in indexed_intervals:
        # free up ongoing meetings
        while ongoing and ongoing[0][0] <= start:
            _, free_room = heapq.heappop(ongoing)
            heapq.heappush(available_rooms, free_room)
        
        if available_rooms:
            room = heapq.heappop(available_rooms)
        else:
            room = room_count
            room_count += 1
        
        result[i] = room
        heapq.heappush(ongoing, (end, room))
        
    return result

if __name__ == "__main__":
    intervals = [[0, 30], [5, 10], [15, 20]]
    result = minMeetingRooms(intervals)
    assert result == [0, 1, 1]