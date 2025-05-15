'''
Problem Statement:

Given a list of colors with their chromatic values, select exactly N colors for a
palette so that the difference between the maximum chromatic value and minimum chromatic value is no more than a threshold.
Find the maximum number of palettes that can be made from the given colors.

Example 1
Input
colors = [6, 2, 10, 2, 11, 1, 3, 2]
paletteSize = 3
threshold = 4

Output
2

Explanation
At most 2 palettes can be made: [1, 2, 2], [2, 3, 6] with a difference (max - min) no more than 4.

Example 2
Input
colors = [10, 15, 9, 10, 9, 1, 3, 3]
paletteSize = 4
threshold = 2

Output
1

Explanation
The only palette [9, 9, 10, 10] with max difference no more than 2.


'''

import time
class Solution:
    def maxPalette(self, colors, paletteSize, threshold) -> int:
        colors.sort()
        count = 0
        i, n = 0, len(colors)
                
        while i <= n - paletteSize:
            if colors[i + paletteSize - 1] - colors[i] <= threshold:
                count += 1
                i += paletteSize
            else:
                i += 1
            
        
        return count

if __name__ == "__main__":
    solution = Solution()
    input, answer = [[10, 15, 9, 10, 9, 1, 3, 3], 4, 2], 1
    start = time.time()
    result = solution.maxPalette(input[0], input[1], input[2])
    end = time.time()
    print(f"Elapsed time for maxPalette to run was : {end - start:.10f} seconds")
    assert result == answer