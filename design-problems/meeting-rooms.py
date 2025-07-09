'''
🔍 Problem: Meeting Rooms (Intervals/Greedy)
Scenario:
You are given an array of meeting time intervals intervals, where intervals[i] = [start_i, end_i], representing the start and end times of a meeting.

Question:
Determine the minimum number of conference rooms required to hold all the meetings without any overlaps.

🧾 Example:
Input:

python
Copy
Edit
intervals = [[0, 30], [5, 10], [15, 20]]
Output:

python
Copy
Edit
2
Explanation:
Two meetings overlap: one starts at 0 and ends at 30, another starts at 5. So we need two rooms.

✅ Constraints:
You may assume all meetings are represented by a pair of integers [start, end].

Meetings can start and end at the same time (i.e., inclusive-exclusive).

You should aim for O(N log N) time complexity.

'''
from heapq import heappop, heappush

def determine_required_num_meeting_rooms(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda x:x[0])
    heap = []
    required_rooms = 0
    
    for start, end in intervals:
        
        # remove all the old meetings that have already completed
        while heap and heap[0] <= start:
            heappop(heap)
        
        # add the new meeting to the heap
        heappush(heap, end)
        
        # update the required # of rooms
        required_rooms = max(required_rooms, len(heap))
    
    return required_rooms
    
    
if __name__ == "__main__":
    intervals = [[0, 30], [5, 10], [15, 20]]
    assert determine_required_num_meeting_rooms(intervals=intervals) == 2
    
