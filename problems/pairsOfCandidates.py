'''
There are n candidates with the expense to hire them listed in an array. The expense to hire the i'th candidate is cost[i]. 
The budget for hiring a pair of new members into our team is between min_cost and max_cost, both inclusive.

Given the array cost and two integers min_cost and max_cost , find the number of pairs of people whose total expense is 
between min_cost and max_cost, both inclusive.
Function Description

Complete the function getNumTeams in the editor below.

getNumTeams takes the following arguments:

int cost[n] : the expense of hiring the candidates
int min_cost: the minimum total expense
int max_cost : the maximum total expense

Returns

long int: the number of pairs of candidates with the sum of costs in the given range


Example 1 :

Input: cost = [2, 3, 4, 5], min_cost = 5, max_cost = 7
Output: 4
Explanation:
cost 1 | cost 2 | cost Sum

2 | 3 | 5

2 | 4 | 6

2 | 5 | 7

3 | 4 | 7

Thus there are 4 possible pairs of employees.


Example 2 :

Input: cost = [1, 3, 5, 3, 8, 7, 2, 10], min_cost = 11, max_cost = 15
Output: 10


Constraints:

1≤n≤10^5
1≤cost[i]≤n
0≤min_cost≤max_cost≤10^5
'''
from bisect import bisect_left, bisect_right

import time
class Solution:
    def bisect(self, cost: list[int], min_cost: int, max_cost: int) -> int:
        cost.sort()
        n = len(cost)
        count = 0
        
        for i in range(n):
            low, high = min_cost - cost[i], max_cost - cost[i]
            
            l = bisect_left(cost, low, i + 1, n)
            r = bisect_right(cost, high, i + 1, n)

            count += (r - l)
            
        return count

    def optimal(self, cost: list[int], min_cost: int, max_cost: int) -> int:
        cost.sort()
        i, min_index, max_index = 0, len(cost) - 1, len(cost) - 1
        
        count_teams = 0
        
        while max_index > i:
            if min_index > i and cost[i] + cost[min_index] >= min_cost:
                min_index -= 1
            elif cost[i] + cost[max_index] > max_cost:
                max_index -= 1
            else:
                count_teams += max_index - min_index
                i += 1
                min_index = max(min_index, i + 1)
        return count_teams
    
if __name__ == "__main__":
    solution = Solution()
    input, answer = [[2, 3, 4, 5], 5, 7], 4
    start = time.time()
    result = solution.bisect(input[0], input[1], input[2])
    end = time.time()
    print(f"runtime for bisect was: {end - start:.10f} seconds")
    assert result == answer
    
    start = time.time()
    result = solution.optimal(input[0], input[1], input[2])
    end = time.time()
    print(f"runtime for optimal was: {end - start:.10f} seconds")
    assert result == answer
    
    
    input, answer = [[
        53, 91, 19, 77, 47, 85, 33, 69, 95, 25,
        58, 20, 14, 17, 12, 79, 21, 36, 93, 70,
        74, 23, 90, 28, 35, 49, 45, 84, 16, 82,
        98, 40, 11, 94, 30, 60, 41, 15, 27, 26,
        54, 96, 32, 88, 87, 80, 92, 31, 38, 29,
        56, 55, 86, 46, 43, 13, 59, 67, 37, 64,
        63, 78, 44, 51, 62, 24, 22, 50, 39, 42,
        34, 99, 83, 48, 100, 65, 97, 18, 10, 68,
        66, 76, 81, 71, 75, 52, 73, 61, 57, 19,
        87, 89, 35, 14, 20, 72, 26, 16, 31, 53
    ], 100, 150], 2148
    start = time.time()
    result = solution.bisect(input[0], input[1], input[2])
    end = time.time()
    print(f"runtime for bisect was: {end - start:.10f} seconds")
    assert result == answer
    
    start = time.time()
    result = solution.optimal(input[0], input[1], input[2])
    end = time.time()
    print(f"runtime for optimal was: {end - start:.10f} seconds")
    assert result == answer