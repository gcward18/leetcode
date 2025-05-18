'''
Smallest Lexicographical Palindrome (Access Key Identifier): Your team is building a key-management utility. Every access key is a string that is a palindrome (reads the same forward and backward). The system groups keys by a “group identifier.” The group identifier is defined as a reordering of the characters of one of the keys in the group such that it forms the lexicographically smallest possible palindrome

 Given a palindromic string key, determine the lexicographically smallest palindrome that can be formed by rearranging its characters. This result is the key’s group identifier

(If the key is already the smallest palindrome permutation, it remains unchanged.)
Example 1: input key = "baab". Output: "abba" (because “abba” is a palindrome and is the smallest in alphabetical order among all rearrangements of “baab”)


Example 2: input key = "pop". Output: "pop" (already the smallest palindrome)


Example 3: input key = "zyxxxyz". Output: "xyzxzyx" (which is the smallest palindrome achievable by rearranging characters of the key).
'''
from collections import Counter, defaultdict
import heapq
import time
class Solution:
    def smallestPalindrome(self, key: str) -> str:
        n = len(key)
        mid = n // 2
        mid_char = key[mid] if n % 2 == 1 else ""
        
        count = [0] * 26
        
        for i in range(mid):
            count[ord(key[i]) - ord('a')] += 1
        
        half = []
        for i in range(26):
            if count[i] > 0:
                half.append(chr(i + ord('a')) * count[i]) 
        return ''.join(half) + mid_char + ''.join(half[::-1])

if __name__ == "__main__":
    solution = Solution()
    input, answer = "baab", "abba"
    start = time.time()
    result = solution.smallestPalindrome(input)
    end = time.time()
    print(f"Elapsed time for smallestPalindrome to run was : {end - start:.10f} seconds")
    assert result == answer
    input, answer = "zyxxxyz", "xyzxzyx"
    start = time.time()
    result = solution.smallestPalindrome(input)
    end = time.time()
    print(f"Elapsed time for smallestPalindrome to run was : {end - start:.10f} seconds")
    assert result == answer