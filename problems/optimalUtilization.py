'''Description:
Given 2 lists a and b. Each element is a pair of integers where the first integer represents the unique id and the second integer represents a value.

Your task is to find an element from a and an element form b such that the sum of their values is less or equal to target and as close to target as possible. Return a list of ids of selected elements. If no pair is possible, return an empty list.

Example 1

Input:
a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7

Output: [[2, 1]]

Explanation:
There are only three combinations [1, 1], [2, 1], and [3, 1], which have a total sum of 4, 6 and 8, respectively.
Since 6 is the largest sum that does not exceed 7, [2, 1] is the optimal pair.
'''

import heapq
from collections import Counter, defaultdict
import time
class Solution:
    def optimalUtilization(self, a, b, limit) -> int:
        answer = []
        max_sum = float('-inf')
        a.sort(key=lambda x:x[1])
        b.sort(key=lambda x:x[1])
        
        for aId, aVal in a:
            for bId, bVal in b:
                curr_sum = aVal + bVal
                if curr_sum > limit: continue
                elif curr_sum > max_sum:
                    max_sum = curr_sum
                    answer = [[aId, bId]]
                elif curr_sum == max_sum:
                    answer.append([aId, bId])
        return answer

if __name__ == "__main__":
    solution = Solution()
    input, answer = [[[1, 2], [2, 4], [3, 6]], [[1,2]], 7], [[2,1]]
    start = time.time()
    result = solution.optimalUtilization(input[0], input[1], input[2])
    end = time.time()
    print(f"Elapsed time for optimalUtilization to run was : {end - start:.10f} seconds")
    assert result == answer
    
    input, answer = [ [[1, 3], [2, 5], [3, 7], [4, 10]], [[1, 2], [2, 3], [3, 4], [4, 5]], 10],  [[2, 4], [3, 2]]
    start = time.time()
    result = solution.optimalUtilization(input[0], input[1], input[2])
    end = time.time()
    print(f"Elapsed time for optimalUtilization to run was : {end - start:.10f} seconds")
    assert result == answer
    
    input, answer = [ [[1, 8]], [[1,9]], 10], []
    start = time.time()
    result = solution.optimalUtilization(input[0], input[1], input[2])
    end = time.time()
    print(f"Elapsed time for optimalUtilization to run was : {end - start:.10f} seconds")
    assert result == answer
    
    input, answer = [ [[1, 1], [2, 2], [3, 3]], [[1, 1], [2, 2], [3, 3]], 5], [[2, 3], [3, 2]]
    start = time.time()
    result = solution.optimalUtilization(input[0], input[1], input[2])
    end = time.time()
    print(f"Elapsed time for optimalUtilization to run was : {end - start:.10f} seconds")
    assert result == answer
    
    input, answer = [ [[1, 5], [2, 5]],  [[1, 5], [2, 5]] , 10], [[1, 1], [1, 2], [2, 1], [2, 2]]

    start = time.time()
    result = solution.optimalUtilization(input[0], input[1], input[2])
    end = time.time()
    print(f"Elapsed time for optimalUtilization to run was : {end - start:.10f} seconds")
    assert result == answer