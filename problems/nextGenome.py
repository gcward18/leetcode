'''
It goes like (As per what I remember) : You are given a String s, convert it into a special string where there will be no repeating adjacent characters. The generated String should be lexicographically larger than the String s. If there are multiple Strings that are larger than S, return the smallest of those.

Eg : “abbc” can be “abca”, “abcb”, “abcd” ….. but final answer is “abcdda” which is lexicographically larger than “abbc” and smaller than the generated words. If there is ‘zz’ in the word return “-1” as we cannot generate a character larger than z.
'''

from collections import Counter, defaultdict
import time
class Solution:
    def nextGenome(self, s: str) -> int:
        n = len(s)
        start = 0
        new_s = list(s)
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        
        for i in range(1, n):
            if s[i] == s[i-1]:
                start = i
                break
        
        if start == 0:
            for i in range(n - 1, -1, -1):
                for candidate in range(ord(s[i]) + 1, ord('z') + 1):
                    c = chr(candidate)
                    
                    if i > 0 and c == s[i-1]:
                        continue        
                    
                    new_str = s[:i] + [c]
                    
                    for j in range(i + 1, n):
                        for fill in alphabet:
                            if fill != new_s[-1]:
                                new_str.append(fill)
                                break
                    result = ''.join(new_str)
                    if result > s:
                        return result
        else:
            count = 0
            for i in range(start, len(s)):
                if new_s[i] == 'z': return "-1"
                if count == 0:
                    new_s[i] = chr(ord(new_s[i]) + 1) 
                    count += 1
                else:
                    new_s[i] = chr(ord('a') + count - 1)
                    count += 1
        
        new_str = ''.join(new_s)
        return new_str if new_str != s else "-1"

if __name__ == "__main__":
    solution = Solution()
    input, answer = "abbace", "abcabc"
    start = time.time()
    result = solution.nextGenome(input)
    end = time.time()
    print(f"Elapsed time for nextGenome to run was : {end - start:.10f} seconds")
    
    assert result == answer
    input, answer = "zzab", "-1"
    start = time.time()
    result = solution.nextGenome(input)
    end = time.time()
    print(f"Elapsed time for nextGenome to run was : {end - start:.10f} seconds")
    assert result == answer
    
    assert result == answer
    input, answer = "abcdeffabd", "abcdefgabc"
    start = time.time()
    result = solution.nextGenome(input)
    end = time.time()
    print(f"Elapsed time for nextGenome to run was : {end - start:.10f} seconds")
    assert result == answer