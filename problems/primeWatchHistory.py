'''
Prime Video “Watch History” Window: Data analysts at Amazon are studying Prime Video usage. You are given an array watchHistory of size n representing the series (by ID number) watched by a user over n consecutive days. Two specific series IDs are given: series1 and series2 (representing the top critic-rated and top audience-rated series respectively). Find the minimum “watch score,” defined as the length of the smallest contiguous period of days in which both Series 1 and Series 2 have been watched at least once. If the two series never appear together in any period, return –1

Example: If n=6 with watchHistory = [1, 3, 2, 1, 4, 2], series1 = 1, and series2 = 2, the output should be 2 because the shortest contiguous segment containing both series1 and series2 is of length 2 (for instance, days index 2–3 contain series 2 and 1).
'''
from collections import defaultdict
import time
class Solution:
    def watchHistory(self, watchHistory: list[int], s1: int, s2: int) -> int:
        mapping = defaultdict(int)
        minimum_days = float('inf')
        
        for i, series in enumerate(watchHistory):
            mapping[series] = i
            
            if s1 in watchHistory and s2 in mapping:
                minimum_days = min(abs(mapping[s1] - mapping[s2]) + 1, minimum_days)
        return minimum_days

if __name__ == "__main__":
    solution = Solution()
    input, answer = [[1, 3, 2, 1, 4, 2], 1, 2], 2
    start = time.time()
    result = solution.watchHistory(input[0], input[1], input[2])
    end = time.time()
    print(f"Elapsed time for watchHistory to run was : {end - start:.10f} seconds")
    assert result == answer
    
    input, answer = [[1, 3, 0, 0, 4, 2], 1, 2], 6
    start = time.time()
    result = solution.watchHistory(input[0], input[1], input[2])
    end = time.time()
    print(f"Elapsed time for watchHistory to run was : {end - start:.10f} seconds")
    assert result == answer