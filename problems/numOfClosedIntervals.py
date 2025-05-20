'''
Number Of Closed Intervals
A librarian would like to count the number of enclosed * in a row that are between two dividers of |. A row is represented by a string s of * and |. A list of range tuples are given that represent each substring to consider, and the number of enclosed items for each substring must be returned in a list.
* = ascii number 42
| = ascii number 124

Example 1:
Input: s = |**|*|*, ranges = [[0, 4], [1, 6]]
Output: [1, 2]
Explanation:
The first range to consider is [0, 4] which corresponds to |**|*. There are 2 items in the first enclosed part.
For the second range, [1, 6], the substring is **|*|*, which contain only one enclosed section with one item in it.
Both of the answers are returned in an array, ie. [2, 1].

Example 2:
Input: s = *|*|, ranges = [[1, 3]]
Output: [1]
Explanation:
The substring from index = 1 to index = 3 is |*|. There is only one item and it is surrounded by two dividers. Therefore, the output is [1].

Constraints:
There are no invalid characters, and each range is non-zero in size and always increasing. The ranges provided are always within the string bounds.
'''

from collections import Counter, defaultdict
import time
class Solution:
    def numberOfItems(self, s: str, queries: list[int]) -> int:
        n = len(s)
        leftbound = [-1] * n
        rightbound = [-1] * n
        prefix = [0] * (n)
        
        # build prefix:
        count = 0
        for i in range(n):
            if s[i] == '|':
                prefix[i] = count
            else:
                count += 1
            
        last = -1
        for i in range(n):
            if s[i] == '|':
                last = i
            leftbound[i] = last
        
        next = -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                next = i
            rightbound[i] = next
        
        res = []
        
        for startIdx, endIdx in queries:
            start = rightbound[startIdx]
            end = leftbound[endIdx-1]
            
            if start != -1 and end != -1 and start < end:
                res.append(prefix[end] - prefix[start])
            else:
                res.append(0)            
        
        return res

if __name__ == "__main__":
    solution = Solution()
    input, answer = ["*|*|", [[1,1],[1,3],[1,4]]], [0, 0, 1]
    start = time.time()
    result = solution.numberOfItems(input[0], input[1])
    end = time.time()
    print(f"Elapsed time for numberOfItems to run was : {end - start:.10f} seconds")
    assert result == answer