'''
🔍 Problem: Meeting Rooms II (Greedy + Heap)
Scenario:
You are given an array of meeting time intervals intervals, where intervals[i] = [start_i, end_i]. Each interval represents a meeting.

Question:
Return the minimum number of meeting rooms required so that no meetings overlap.

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

Meeting 1: [0, 30]

Meeting 2: [5, 10] → overlaps with 1

Meeting 3: [15, 20] → also overlaps with 1 (but after 2)

We need 2 rooms to accommodate them.
'''
import heapq

def meeting_rooms(meeting_rooms: list[list[int]]) -> int:
    rooms_needed = 0
    occupied_rooms = []
    meeting_rooms.sort()
    
    for start, end in meeting_rooms:
        # remove all the rooms that are no longer needed
        while occupied_rooms and occupied_rooms[0] <= start:
            heapq.heappop(occupied_rooms)
        
        # add current room end time to keep track of current rooms in use
        heapq.heappush(occupied_rooms, end)
        
        rooms_needed = max(rooms_needed, len(occupied_rooms))
    
    return rooms_needed
        

if __name__ == "__main__":
    intervals = [[0, 30], [5, 10], [15, 20]]
    assert meeting_rooms(intervals) == 2