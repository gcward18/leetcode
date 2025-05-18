'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 
 '''
from collections import Counter
import time
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCounts = Counter(t)
        start = 0
        ans = [-1,-1]
        windowCount = {}
        need = len(tCounts)
        have = 0
        
        for end, c in enumerate(s):
            windowCount[c] = windowCount.get(c, 0) + 1
            
            if windowCount[c] == tCounts[c]:
                have += 1
            
            while have == need:
                startChar = s[start]
                if ans == [-1, -1] or ans[1] - ans[0] > end - start:
                    ans = [start, end]
                
                windowCount[startChar] -= 1
                
                if startChar in tCounts and windowCount[startChar] < tCounts[startChar]:
                    have -= 1
                
                start += 1
                
            
        return s[ans[0]: ans[1] + 1] if ans != [-1, -1] else ""

if __name__ == "__main__":
    solution = Solution()
    input, answer = ["ADOBECODEBANC","ABC"], "BANC"
    start = time.time()
    result = solution.minWindow(input[0], input[1])
    end = time.time()
    print(f"Elapsed time for minWindow to run was : {end - start:.10f} seconds")
    assert result == answer