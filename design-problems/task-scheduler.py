'''
🧠 Problem 4: Task Scheduler with Cooldown (Greedy + Heap)
Scenario:
You're given a list of CPU tasks, each represented by a capital letter A to Z.
Each task takes exactly 1 unit of time, but identical tasks must be separated by at least n units of cooldown time.

✅ Your Goal:
Return the minimum total time the CPU will take to finish all the given tasks, including idle time.

🧾 Example:
python
Copy
Edit
tasks = ["A","A","A","B","B","B"]
n = 2
Output:

Copy
Edit
8
Explanation:
One possible schedule: A → B → idle → A → B → idle → A → B
Total time: 8 units

'''
from collections import deque, Counter
import heapq

def minimum_time_to_complete_tasks(tasks: list[str], cooldown_period: int) -> int:
    if not tasks:
        return 0
    
    cooldown = deque([])
    heap = [(-freq, task) for task, freq in Counter(tasks).items()]
    heapq.heapify(heap)
    time = 0
    
    while heap or cooldown:
        if cooldown and cooldown[0][0] <= time:
            _, freq, task = cooldown.popleft()
            heapq.heappush(heap, (freq, task))
        
        if heap:
            freq, task = heapq.heappop(heap)
        
            if freq + 1 < 0:
                cooldown.append((time + cooldown_period + 1, freq + 1, task))
        time += 1
    
    return time
    
if __name__ == "__main__":
    tasks = ["A","A","A","B","B","B"]
    n = 2
    
    result = minimum_time_to_complete_tasks(tasks, n)
    
    assert result == 8
    
