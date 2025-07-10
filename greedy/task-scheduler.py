'''
🧮 DSA Problem: Task Scheduler with Cooldown
Prompt:
You are given a list of tasks, where each task is represented by a capital letter (e.g., 'A', 'B', etc.). Each task takes 1 unit of time to execute. However, the same task must be separated by at least n units of time (cooldown).

Return the minimum time it would take to finish all the tasks, even if some intervals are idle.

Function Signature:

python
Copy
Edit
def leastInterval(tasks: List[str], n: int) -> int:
Example:

python
Copy
Edit
Input: tasks = ['A','A','A','B','B','B'], n = 2
Output: 8
Explanation: A → B → idle → A → B → idle → A → B
⏱️ Implement when ready. Say “done” when finished for the first follow-up.
'''
from collections import Counter, deque
import heapq 

class CoolDownScheduler:
    def __init__(self, n: int):
        self._period = n
        self._runnable = []
        self._cooldown = deque([])
        self._elapsed_time = 0
        self._tasks = {}
        
        
    def add_task(self, task: str) -> int:
        if task not in self._tasks:
            self._tasks[task] = [-1, self._elapsed_time]
        else:
            self._tasks[task][0] -= 1
            
        # remove from the cool down queue
        while self._cooldown and self._cooldown[0][0] < self._elapsed_time:
            next_time, freq, task = self._cooldown.popleft()
            heapq.heappush(self._runnable, (freq, task))
        
        # increment the time    
        self._elapsed_time += 1
        
        # check if we have a runnable item
        if self._runnable:
            _, running_task = heapq.heappop(self._runnable)
            
            if self._tasks[running_task][0] < 0:
            
                self._tasks[running_task][0] + 1    
                self._tasks[running_task][1] = self._elapsed_time + self._period
                
                self._cooldown.append((self._tasks[running_task][1], self._tasks[running_task][0], running_task))
            else:
                del self._tasks[running_task]
        
        return self._tasks[task][1] if task in self._tasks else self._elapsed_time
                
        
        
        
            
if __name__ == "__main__":
    s = CoolDownScheduler(2)
    print(s.add_task('A'))  # returns 0
    print(s.add_task('A'))  # returns 3 (must wait 2 units between same task)
    print(s.add_task('B'))  # returns 1
    print(s.add_task('A'))  # returns 6