'''
Get Minimum Boxes
FULLTIME
Alex is shipping the last container of the day, trying to load
all n boxes into the container with their sizes represented in 
the array boxes . The container may not have enough capacity for 
all the boxes. So some of the boxes may have to be removed. The
boxes in the container must satisfy the condition 
max(boxes) ≤ capacity * min(boxes) .


Given the array, boxes , and capacity , find the minimum number 
of boxes that need to be removed.


Function Description

Complete the function getMinimumBoxes in the editor.

getMinimumBoxes has the following parameters:

int[] boxes : an array of integers representing the sizes of the boxes
int capacity : the capacity index of the container

Returns

int: the minimum number of boxes that need to be unloaded


Example 1 :

min(boxes) = 1
capacity = 2
max(boxes) <= capacity * min(boxes)
4 <= 2 * 1 False
[1, 2, 3, 4]
    i
          j
          
Input: boxes = [1, 4, 3, 2], capacity = 2
Output: 1
Explanation:

This satisfies the required condition. Hence the answer is 1.


Example 2 :

[1, 6, 40, 200, 3000]
        l  
           r
                
200 <= 5 * 210  1050
Input: boxes = [3000, 1, 6, 40, 210], capacity = 5
Output: 4
Explanation:
Only 1 of the boxes can be loaded into the container.

[2, 3, 5, 20, 25, 40, 80, 200, 400, 500]
                          l  
                                     r
capacity = 4
400 <= 4 * 200
max_len = 4

'''

import time
class Solution:
    def minBoxes(self, boxes, capacity) -> int:
        boxes.sort()
        left = 0
        n = len(boxes)
        max_boxes = 0
        
        for right in range(n):
            while boxes[right] > boxes[left] * capacity:
                left += 1
            max_boxes = max(max_boxes, right - left + 1)
        
        return n - max_boxes

if __name__ == "__main__":
    solution = Solution()
    input, answer = [[3000, 1, 6, 40, 210],5], 4
    start = time.time()
    result = solution.minBoxes(input[0], input[1])
    end = time.time()
    print(f"Elapsed time for minBoxes to run was : {end - start:.10f} seconds")
    assert result == answer
    input, answer = [[1, 2, 3, 4],2], 1
    start = time.time()
    result = solution.minBoxes(input[0], input[1])
    end = time.time()
    print(f"Elapsed time for minBoxes to run was : {end - start:.10f} seconds")
    assert result == answer
    input, answer = [[2, 3, 5, 20, 25, 40, 80, 200, 400, 500],4], 6
    start = time.time()
    result = solution.minBoxes(input[0], input[1])
    end = time.time()
    print(f"Elapsed time for minBoxes to run was : {end - start:.10f} seconds")
    assert result == answer